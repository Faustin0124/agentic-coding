#!/usr/bin/env python3
"""
Mechanical audit for AI-slop "tells" in generated frontend code.

Self-auditing is the weakest link in the pre-flight check in SKILL.md: the same
model that just wrote the code is asking itself to notice its own reflexes,
which is exactly the failure mode it's checking for. This script catches
whatever is objectively string-matchable so that pass only needs to catch what
a regex can't: structural judgment calls (section repetition, "does this
copy sound cute-but-wrong").

Usage:
    python3 audit_ai_tells.py <file-or-directory> [<file-or-directory> ...]
    python3 audit_ai_tells.py <file-or-directory> --design-md <path/to/design.md>

Two checks need a project's design.md to do anything useful:

  - hardcoded-hex-not-in-design-md: flags hex colors used in code that don't
    appear anywhere in design.md. Without --design-md, the script searches
    upward from each scanned file's directory for design.md/DESIGN.md and
    uses whatever it finds; if none exists anywhere above a file, that file
    is scanned for every other check but skipped for this one (there's
    nothing to compare against, not a violation).
  - contrast checks work regardless of design.md, but only for text/background
    pairs expressed as literal hex or white/black in the same className
    string (`className="bg-[#111] text-[#fff]"`). It cannot see colors that
    come from Tailwind's named palette (`bg-zinc-900`), CSS variables, or
    `clsx`/`cn()` composition — those need the manual WCAG check in the
    pre-flight checklist instead.

Exit code 1 if any HARD violation is found (things this skill treats as
non-negotiable bans). Exit code 0 if only SOFT findings are present (things
with a stated override condition, worth a human/model glance) or nothing at
all. Findings are grouped by category with file:line references.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

SCAN_EXTENSIONS = {".tsx", ".ts", ".jsx", ".js", ".html", ".vue", ".svelte", ".astro"}
SKIP_DIR_NAMES = {"node_modules", ".next", "dist", "build", ".git", ".turbo"}

CONTRAST_THRESHOLD = 4.5  # WCAG AA for body text; large text (18px+/bold 14px+) only needs 3:1


@dataclass
class Finding:
    severity: str  # "HARD" or "SOFT"
    category: str
    file: Path
    line: int
    snippet: str
    note: str


# ---------------------------------------------------------------------------
# Pattern tables — kept close to the rules documented in references/anti-cliches.md
# and references/marketing-layout.md so the two stay in sync. If you add a rule
# there that's mechanically checkable, add it here too.
# ---------------------------------------------------------------------------

EM_EN_DASH = re.compile(r"[—–]")

# Banned premium-consumer "beige+brass+oxblood+espresso" palette (anti-cliches.md).
BANNED_HEX = {
    "#f5f1ea", "#f7f5f1", "#fbf8f1", "#efeae0", "#ece6db", "#faf7f1", "#e8dfcb",
    "#b08947", "#b6553a", "#9a2436", "#9c6e2a", "#bc7c3a", "#7d5621",
    "#1a1714", "#1a1814", "#1b1814",
}

# Display serifs specifically called out as banned defaults.
BANNED_SERIF_FONTS = re.compile(r"\b(Fraunces|Instrument[_ ]?Serif)\b")

FILLER_VERBS = re.compile(
    r"\b(Elevate|Unleash|Revolutioniz(?:e|ing)|Supercharge|Empower(?:ing)?|"
    r"Transform(?:ing)?|Effortless(?:ly)?|Unlock(?:ing)?|Streamlin(?:e|ing)|"
    r"Next-Gen(?:eration)?)\b"
)

PUFFERY_WORDS = re.compile(
    r"\b(cutting-edge|state-of-the-art|world-class|industry-leading|"
    r"best-in-class|game-changing|unparalleled|groundbreaking|revolutionary|"
    r"seamless(?:ly)?|robust|comprehensive solution|innovative solution)\b",
    re.IGNORECASE,
)

GENERIC_PLACEHOLDER_NAMES = re.compile(
    r"\b(John Doe|Jane Doe|Sarah Chan|Jack Su|Acme(?: Corp| Inc)?|Nexus(?: Inc)?|"
    r"SmartFlow|Cloudly|TechCorp|Lorem Ipsum)\b"
)

# "Not just X, but Y" / "It's not X, it's Y" — the single most common AI
# headline/tagline construction (see the anti-ai-writing skill's "Negative
# parallelisms" section for the deep dive).
NEGATIVE_PARALLELISM = re.compile(
    r"\b(not\s+(?:just|only)\b[^.!?\n]{0,60}(?:\bbut\b|it'?s\b)|"
    r"it'?s\s+not\b[^.!?\n]{0,40}\bit'?s\b)",
    re.IGNORECASE,
)

LUCIDE_IMPORT = re.compile(r"""from\s+["']lucide-react["']""")

VERSION_FOOTER = re.compile(r"\bv\d+\.\d+\.\d+(?:-\w+)?\b|\bBuild\s+\d+\b|\blast sync\b", re.IGNORECASE)

SCROLL_CUE = re.compile(r"scroll to explore|↓\s*scroll|scroll down\b", re.IGNORECASE)

SECTION_NUMBER_EYEBROW = re.compile(r">\s*0?\d{1,2}\s*[/·]\s*[A-Z]")

LOCALE_TIME_STRIP = re.compile(r"\b\d{1,2}:\d{2}\s*·\s*\d{1,2}°[CF]\b")

EYEBROW_CLASS = re.compile(r"uppercase\s+tracking-\[")
SECTION_TAG = re.compile(r"<section\b|<Section\b")

# Longest-alternative-first so greedy matching doesn't truncate an 8-digit hex to 6.
HEX_TOKEN = re.compile(r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b")

CLASSNAME_ATTR = re.compile(r"""className\s*=\s*["']([^"']*)["']""")
BG_COLOR_IN_CLASS = re.compile(r"\bbg-\[(#[0-9a-fA-F]{3,8})\]|\bbg-(white|black|transparent)\b")
TEXT_COLOR_IN_CLASS = re.compile(r"\btext-\[(#[0-9a-fA-F]{3,8})\]|\btext-(white|black)\b")
HAS_BORDER_CLASS = re.compile(r"\bborder(?:-|\b)")

NAMED_HEX = {"white": "#ffffff", "black": "#000000"}


# ---------------------------------------------------------------------------
# Color math
# ---------------------------------------------------------------------------

def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    h = hex_str.lstrip("#")
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h[:3])
    elif len(h) == 8:
        h = h[:6]
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def _channel_luminance(c: int) -> float:
    c_norm = c / 255
    return c_norm / 12.92 if c_norm <= 0.03928 else ((c_norm + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    r, g, b = rgb
    return 0.2126 * _channel_luminance(r) + 0.7152 * _channel_luminance(g) + 0.0722 * _channel_luminance(b)


def contrast_ratio(hex_a: str, hex_b: str) -> float:
    lum_a = relative_luminance(hex_to_rgb(hex_a))
    lum_b = relative_luminance(hex_to_rgb(hex_b))
    lighter, darker = max(lum_a, lum_b), min(lum_a, lum_b)
    return (lighter + 0.05) / (darker + 0.05)


# ---------------------------------------------------------------------------
# design.md discovery + token extraction
# ---------------------------------------------------------------------------

@lru_cache(maxsize=None)
def _find_design_md_upward(start_dir: str) -> str | None:
    current = Path(start_dir).resolve()
    for _ in range(10):
        for name in ("design.md", "DESIGN.md", "Design.md"):
            candidate = current / name
            if candidate.is_file():
                return str(candidate)
        docs_candidate = current / "docs" / "design.md"
        if docs_candidate.is_file():
            return str(docs_candidate)
        if current.parent == current:
            break
        current = current.parent
    return None


@lru_cache(maxsize=None)
def _load_declared_hex(design_md_path: str) -> frozenset[str]:
    try:
        text = Path(design_md_path).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return frozenset()
    return frozenset(m.group(0).lower() for m in HEX_TOKEN.finditer(text))


def resolve_design_md_tokens(file_path: Path, explicit_design_md: str | None) -> frozenset[str] | None:
    """Returns the declared hex set, or None if no design.md applies to this file."""
    if explicit_design_md:
        return _load_declared_hex(explicit_design_md)
    found = _find_design_md_upward(str(file_path.parent))
    if found is None:
        return None
    return _load_declared_hex(found)


# ---------------------------------------------------------------------------
# Scanning
# ---------------------------------------------------------------------------

def iter_scan_files(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_file():
            files.append(p)
        elif p.is_dir():
            for sub in p.rglob("*"):
                if sub.is_file() and sub.suffix in SCAN_EXTENSIONS:
                    if any(part in SKIP_DIR_NAMES for part in sub.parts):
                        continue
                    files.append(sub)
    return sorted(set(files))


def check_contrast_in_line(line: str, path: Path, i: int) -> list[Finding]:
    findings: list[Finding] = []
    for attr_match in CLASSNAME_ATTR.finditer(line):
        attr = attr_match.group(1)
        bg_match = BG_COLOR_IN_CLASS.search(attr)
        text_match = TEXT_COLOR_IN_CLASS.search(attr)
        if not bg_match and not text_match:
            continue

        bg_hex: str | None
        bg_transparent = False
        if bg_match:
            if bg_match.group(1):
                bg_hex = bg_match.group(1).lower()
            elif bg_match.group(2) == "transparent":
                bg_hex, bg_transparent = None, True
            else:
                bg_hex = NAMED_HEX[bg_match.group(2)]
        else:
            bg_hex = None

        text_hex: str | None = None
        if text_match:
            text_hex = (text_match.group(1) or NAMED_HEX.get(text_match.group(2) or "")).lower() \
                if text_match.group(1) else NAMED_HEX.get(text_match.group(2) or "")

        if bg_hex and text_hex:
            ratio = contrast_ratio(bg_hex, text_hex)
            if ratio < CONTRAST_THRESHOLD:
                findings.append(Finding(
                    "SOFT", "low-contrast-text", path, i, line.strip(),
                    f"Contrast ratio {ratio:.2f}:1 between text {text_hex} and background {bg_hex} "
                    f"is below WCAG AA 4.5:1 for body text (3:1 is enough for 18px+/bold-14px+ text — "
                    f"fine if this is large display type, otherwise fix it)."
                ))
        elif bg_transparent and text_hex and not HAS_BORDER_CLASS.search(attr):
            findings.append(Finding(
                "SOFT", "transparent-bg-no-border", path, i, line.strip(),
                "Text on an explicitly transparent background with no border class. Can't compute contrast "
                "against whatever's actually behind it statically — verify manually, especially over images."
            ))
    return findings


def collect_hardcoded_hex_findings(files: list[Path], explicit_design_md: str | None) -> list[Finding]:
    """One Finding per unique off-token hex value, not per occurrence.

    A project that consistently derives dark-mode variants from its design.md
    tokens might reuse the same "new" hex 20 times across a file — that's one
    design decision to review, not 20 separate problems. Aggregating keeps the
    report proportional to the number of decisions, not the number of lines.
    """
    occurrences: dict[str, list[tuple[Path, int, str]]] = {}
    for path in files:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        declared_hex = resolve_design_md_tokens(path, explicit_design_md)
        if declared_hex is None:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            for hm in HEX_TOKEN.finditer(line):
                hex_val = hm.group(0).lower()
                if hex_val in BANNED_HEX or hex_val in declared_hex:
                    continue
                occurrences.setdefault(hex_val, []).append((path, i, line.strip()))

    findings: list[Finding] = []
    for hex_val, occ in sorted(occurrences.items(), key=lambda kv: -len(kv[1])):
        first_path, first_line, first_snippet = occ[0]
        distinct_files = len({p for p, _, _ in occ})
        note = (
            f"{hex_val} doesn't appear in design.md — used {len(occ)} time(s) across "
            f"{distinct_files} file(s). Use a declared token, or if this is a deliberate, "
            f"systematic addition (e.g. a consistent dark-mode variant of an existing token), "
            f"add it to design.md so it becomes the source of truth."
        )
        findings.append(Finding("SOFT", "hardcoded-hex-not-in-design-md", first_path, first_line, first_snippet, note))
    return findings


def scan_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return findings
    lines = text.splitlines()

    for i, line in enumerate(lines, start=1):
        if EM_EN_DASH.search(line):
            findings.append(Finding("HARD", "em-dash-ban", path, i, line.strip(),
                "Em-dash/en-dash found. Rewrite with a period, comma, or hyphen — zero tolerance, see anti-cliches.md."))

        lowered = line.lower()
        for hex_code in BANNED_HEX:
            if hex_code in lowered:
                findings.append(Finding("HARD", "banned-premium-palette", path, i, line.strip(),
                    f"{hex_code} is in the banned beige/brass/oxblood/espresso palette. Rotate to a different family."))

        if BANNED_SERIF_FONTS.search(line):
            findings.append(Finding("HARD", "banned-serif", path, i, line.strip(),
                "Fraunces / Instrument Serif used as a default. Only acceptable with explicit brand justification noted in a comment."))

        if m := FILLER_VERBS.search(line):
            findings.append(Finding("SOFT", "filler-verb", path, i, line.strip(),
                f"'{m.group(0)}' is a generic SaaS filler verb. Say concretely what the thing does instead."))

        if m := PUFFERY_WORDS.search(line):
            findings.append(Finding("SOFT", "puffery", path, i, line.strip(),
                f"'{m.group(0)}' is unsupported puffery (see anti-ai-writing skill's 'Promotional language' section). Back it with a specific claim or cut it."))

        if m := GENERIC_PLACEHOLDER_NAMES.search(line):
            findings.append(Finding("HARD", "generic-placeholder", path, i, line.strip(),
                f"'{m.group(0)}' is a generic placeholder name/brand. Use something specific and realistic."))

        if m := NEGATIVE_PARALLELISM.search(line):
            findings.append(Finding("SOFT", "negative-parallelism", path, i, line.strip(),
                "Not-just-X-but-Y / it's-not-X-it's-Y construction. The single most common AI tagline pattern — say the thing directly instead."))

        if LUCIDE_IMPORT.search(line):
            findings.append(Finding("SOFT", "lucide-icons", path, i, line.strip(),
                "lucide-react imported. Fine if the project already commits to it or design.md says so; otherwise prefer Phosphor/HugeIcons/Radix/Tabler."))

        if VERSION_FOOTER.search(line):
            findings.append(Finding("SOFT", "version-footer", path, i, line.strip(),
                "Version-footer-style string on what looks like marketing content. CLI/devtool fixture, not landing-page content — confirm this is intentional."))

        if SCROLL_CUE.search(line):
            findings.append(Finding("SOFT", "scroll-cue", path, i, line.strip(),
                "Explicit scroll cue. Usually unnecessary — the user knows what scrolling is."))

        if SECTION_NUMBER_EYEBROW.search(line):
            findings.append(Finding("SOFT", "section-number-eyebrow", path, i, line.strip(),
                "Looks like a section-number eyebrow ('00 / INDEX' style). Name the topic in plain language instead."))

        if LOCALE_TIME_STRIP.search(line):
            findings.append(Finding("SOFT", "locale-time-strip", path, i, line.strip(),
                "Locale/time strip pattern. Only justified for globally-distributed studios, travel brands, or real venues."))

        findings.extend(check_contrast_in_line(line, path, i))

    # Eyebrow-frequency heuristic: needs the whole file, not line-by-line.
    eyebrow_count = len(EYEBROW_CLASS.findall(text))
    section_count = len(SECTION_TAG.findall(text)) or 1
    max_allowed = -(-section_count // 3)  # ceil(section_count / 3)
    if eyebrow_count > max_allowed:
        findings.append(Finding(
            "SOFT", "eyebrow-frequency", path, 0, "",
            f"{eyebrow_count} eyebrow-style labels across ~{section_count} sections "
            f"(max recommended: {max_allowed}, roughly 1 per 3 sections). Cut some.",
        ))

    return findings


def print_report(findings: list[Finding], design_md_used: bool) -> int:
    if not findings:
        print("No mechanical AI-tell patterns found. This does not clear the structural/")
        print("judgment checks (section repetition, copy quality, bento cell count, etc.)")
        print("in SKILL.md Section 6 and references/pre-flight-checklist.md — run those too.")
        if not design_md_used:
            print("\nNote: no design.md was found for any scanned file, so the hardcoded-hex-")
            print("not-in-design-md check didn't run. Pass --design-md explicitly if one exists")
            print("but isn't a filesystem ancestor of the scanned files.")
        return 0

    hard = [f for f in findings if f.severity == "HARD"]
    soft = [f for f in findings if f.severity == "SOFT"]

    for label, group in (("HARD (must fix)", hard), ("SOFT (worth a look, has override conditions)", soft)):
        if not group:
            continue
        print(f"\n=== {label}: {len(group)} finding(s) ===\n")
        by_category: dict[str, list[Finding]] = {}
        for f in group:
            by_category.setdefault(f.category, []).append(f)
        for category, items in sorted(by_category.items()):
            print(f"[{category}] ({len(items)})")
            for f in items:
                loc = f"{f.file}:{f.line}" if f.line else str(f.file)
                print(f"  {loc}")
                if f.snippet:
                    print(f"    > {f.snippet}")
                print(f"    {f.note}")
            print()

    print(f"Total: {len(hard)} hard, {len(soft)} soft.")
    if not design_md_used:
        print("\nNote: no design.md was found for any scanned file, so hardcoded-hex-not-in-")
        print("design-md checks didn't run for those files. Pass --design-md to force one.")
    return 1 if hard else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="+", help="Files or directories to scan.")
    parser.add_argument("--design-md", dest="design_md", default=None,
                         help="Explicit path to design.md, overriding upward auto-discovery.")
    args = parser.parse_args()

    files = iter_scan_files(args.paths)
    if not files:
        print("No matching source files found under the given path(s).")
        return 0

    all_findings: list[Finding] = []
    design_md_used = False
    for f in files:
        if resolve_design_md_tokens(f, args.design_md) is not None:
            design_md_used = True
        all_findings.extend(scan_file(f))

    all_findings.extend(collect_hardcoded_hex_findings(files, args.design_md))

    return print_report(all_findings, design_md_used)


if __name__ == "__main__":
    raise SystemExit(main())
