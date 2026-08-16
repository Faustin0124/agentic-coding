---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics — landing pages, portfolios, marketing sites, dashboards, components, redesigns, or any web UI. ALWAYS check the project root (and common doc locations) for a design.md file first: when present it is the binding design system (tokens, palette, typography, components, principles) and every visual choice must comply with it; only fall back to inferring taste from the brief when design.md is silent on a given point. Use this skill whenever the user asks to build, style, redesign, or critique any web page, component, or application, or mentions "design system", "design.md", "landing page", "portfolio", "make this look better", "this feels off", or wants creative/premium/polished UI — even if they don't say "design" explicitly.
license: Complete terms in LICENSE.txt
---

# Frontend Design

Guides creation of distinctive, production-grade frontend interfaces that avoid generic
"AI slop" aesthetics: templated layouts, cliché palettes, and copy-paste component patterns
that make every AI-built site look the same. Implement real, working code with exceptional
attention to aesthetic detail — never a mockup or a description of what the UI should look like.

This skill covers **greenfield builds, redesigns, and one-off components** — landing pages,
portfolios, marketing sites, dashboards, and product UI alike. It is not a substitute for
`product-designer` (user flows, information architecture, cross-screen journeys) — reach for
that skill first when the task is about *what screens exist and how users move between them*.
This skill takes over once you know what you're building and need it to look and feel right.

---

## 0. The Design System Is Not a Guess — Check design.md First

Most anti-slop advice for LLMs assumes the model has to infer a design direction from vibe
words alone. That is the *fallback* here, not the default. In this repo's projects, the design
system is almost always already written down.

**Before anything else, look for a `design.md`** (or `DESIGN.md`, `docs/design.md`,
`wiki/design/*.md`) at the project root. If a file like `pradio-design-review` or another
project-specific design-system skill is also installed, that skill's rules take precedence —
this skill fills the gaps it doesn't cover (taste judgment, anti-cliché discipline, motion,
copy quality), it does not override a project's own design-system enforcement.

**If `design.md` exists, it is the source of truth.** Extract and follow, in this order of
authority:
1. **Design tokens** — colors, spacing scale, radii, typography scale, shadows.
2. **Component library** — which primitives to use (shadcn/ui, a custom kit, etc.) and how.
3. **Stated principles** — voice, tone, density, motion philosophy, anything written in prose.

Treat every rule below (dials, palette bans, layout discipline) as **applying only where
`design.md` is silent**. A documented design system always wins over this skill's defaults —
that's the whole point of writing one down. If `design.md` conflicts with a rule below, follow
`design.md` and don't flag it as a violation.

**If `design.md` is missing, incomplete, or this is a genuinely new project** with no system
yet, fall back to Section 1 (Brief Inference) below — and consider telling the user that
writing a `design.md` once the direction is settled would save this inference step on every
future task.

**"Silent" and "contradicting" are different.** If `design.md` simply doesn't mention something
(e.g. no dark-mode tokens given, but nothing says light-only either), extend it consistently
with what it does specify and say so explicitly — that's filling a gap, not overriding the
doc. Only treat this skill's defaults as fully overridden when `design.md` actually states a
conflicting rule.

---

## 1. Brief Inference (Only for What design.md Doesn't Cover)

Before touching code, read the room. Most bad LLM design output happens because the model
jumps to a default aesthetic instead of reading what's actually being asked for.

**Read these signals:**
1. **Page/component kind** — landing (SaaS/consumer/agency/event), portfolio, dashboard,
   redesign (preserve vs. overhaul), a single component.
2. **Vibe words** the user used — "minimalist", "calm", "Linear-style", "brutalist", "premium
   consumer", "playful", "serious B2B", "editorial", "glassy", "dark tech".
3. **Reference signals** — URLs, screenshots, named products or competitors.
4. **Copy language** — write UI copy in the language the brief itself was written in (or the
   language the audience clearly speaks) unless told otherwise. Don't default to English.
5. **Audience** — B2B procurement panel vs. design-conscious consumer vs. recruiter scanning a
   portfolio. The audience picks the aesthetic, not your taste.
6. **Quiet constraints** — accessibility-first audiences, regulated industries, trust-first
   commerce. These override aesthetic preference.

**State a one-line "Design Read" before generating anything**, even when `design.md` covers
most of it — it confirms your interpretation and gives the user one cheap chance to correct
you before you've written code:

> "Reading this as: B2B SaaS landing for technical buyers, tokens from design.md, leaning
> toward restrained motion and a Linear-style layout for the parts design.md doesn't specify."

If genuinely ambiguous, ask **exactly one** clarifying question — never a multi-question dump.
If you can confidently infer, don't ask, just declare the read and proceed.

**Don't default to:** AI-purple gradients, a centered hero over a dark mesh background, three
equal feature cards, glassmorphism applied to everything, Inter + slate-900 as the unexamined
choice. These are the LLM's reflexes — reach past them deliberately.

---

## 2. The Three Dials

Once you know what `design.md` fixes and what's still open, set three dials for the open parts.
These gate every layout, motion, and density decision that isn't already pinned by the design
system.

* **`DESIGN_VARIANCE` (1–10)** — 1 = perfect symmetry, 10 = artsy asymmetric chaos.
* **`MOTION_INTENSITY` (1–10)** — 1 = static, 10 = cinematic/physics-driven.
* **`VISUAL_DENSITY` (1–10)** — 1 = art-gallery/airy, 10 = cockpit/packed data.

**Baseline: `7 / 5 / 4`** unless the brief or `design.md` overrides it.

| Signal | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| Minimalist / calm / editorial / Linear-style | 5–6 | 3–4 | 2–3 |
| Premium consumer / Apple-y / luxury | 7–8 | 5–7 | 3–4 |
| Playful / experimental / agency / Awwwards | 9–10 | 8–10 | 3–4 |
| Landing page / marketing site (default) | 7–9 | 6–8 | 3–5 |
| Trust-first / regulated / accessibility-critical | 3–4 | 2–3 | 4–5 |
| Dashboard / dense product UI | 3–5 | 2–3 | 7–9 |
| Redesign — preserve existing feel | match existing | +1 | match existing |
| Redesign — overhaul | +2 | +2 | match existing |

Use these as global variables for the session; don't invent aliases. Full technical definitions
(what VARIANCE 8 actually looks like in CSS) are in `references/animation-code.md`.

---

## 3. Pick a Real Foundation, Don't Invent One

If `design.md` already names a component library or design system, use it — skip this section.
Otherwise, match the brief to a real foundation instead of hand-rolling CSS for something that
already has an official package:

| Brief reads as… | Reach for |
|---|---|
| Enterprise SaaS / Microsoft-adjacent | `@fluentui/react-components` |
| Material-flavored product | `@material/web` + Material 3 tokens |
| IBM-style B2B / dense analytics | `@carbon/react` |
| Public-sector (UK / US) | `govuk-frontend` / `uswds` |
| Modern accessible React foundation | `@radix-ui/themes` |
| Modern SaaS where you own the components | shadcn/ui — **never ship it in default state** |
| Default for indie/small-team builds | Tailwind v4 utilities + `dark:` variant |

**Honesty rule:** if a real system applies, install and use the *official* package — don't
recreate its CSS by hand, and don't import its tokens then override 90% of them. If the brief
is an aesthetic (glassmorphism, bento, brutalism) rather than a system, say so — there is no
official package for a vibe, build it with native CSS/Tailwind and be upfront about what's
borrowed inspiration vs. official material. One system per project; never mix two component
libraries in the same tree. **This table is a suggestion, not an obligation** — if the brief
explicitly asks to avoid a formal/heavy system ("no design system yet", "keep it simple"), that
explicit request wins over the table's suggestion.

**Default stack** (unless `design.md` or the project says otherwise): React/Next.js with
Server Components by default, **Tailwind v4**, **Motion** (`motion/react`) for UI animation,
GSAP + ScrollTrigger only for full-page scroll-hijacking, isolated in Client Component leaves.
Icons: prefer `@phosphor-icons/react`, `hugeicons-react`, `@radix-ui/react-icons`, or
`@tabler/icons-react` over `lucide-react` — unless `design.md` or the project already commits
to Lucide, in which case follow that. Never hand-roll SVG icon paths.

---

## 4. Design Engineering Directives (Bias Correction)

LLMs default to clichés — an unexamined purple-gradient, Inter-everywhere, three-equal-cards
sameness that makes every generated site look related. Override these defaults proactively,
but treat every rule here as **contextual**: apply it when it fits the design read, override it
when the brief genuinely calls for the opposite, and always defer to `design.md` first.

The highest-impact ones to hold in mind by default:

* **Typography** — avoid Inter as the unexamined default; pick something with more character
  unless the brief is neutral/public-sector, where Inter is fine. Serif is discouraged as a
  default "creative = serif" reflex — reserve it for genuinely editorial/luxury/heritage briefs.
* **Color** — max one accent color per project, used identically everywhere (no drifting to a
  different accent in section 7). Avoid the reflexive AI-purple glow. For premium-consumer
  briefs, avoid the beige+brass+oxblood "artisan" palette everyone else also ships.
* **Layout** — vary section layouts across the page; don't repeat the same 3-column or
  image-text-split pattern more than twice in a row.
* **Motion must be motivated** — every animation should be justifiable in one sentence
  (hierarchy, storytelling, feedback, state transition). "It looked cool" is not a reason.
* **Em-dash (`—`) is banned** from all visible UI copy — headlines, labels, body, captions,
  buttons. It's the single most common LLM writing tell. Use a period, comma, or hyphen instead.
* **Real content, not filler** — no "John Doe" placeholder names, no fake-perfect numbers
  (`99.99%`), no `Acme`/`Nexus`-style startup-slop brand names, no filler verbs ("Elevate",
  "Unleash", "Revolutionize"), no "not just X, but Y" taglines or rule-of-three padding.

The exhaustive version of this — typography pairings, the full banned-palette hex list, form
and interactive-state rules, dark-mode protocol, and the full catalog of AI writing/visual
"tells" — lives in **`references/anti-cliches.md`**. Load it before shipping anything
non-trivial; it's dense but each rule states its own override condition. That file's "Copy
Patterns That Read as AI-Written" section also covers sentence-level tells beyond vocabulary —
negative parallelism ("not just X, but Y"), rule-of-three padding, unsupported puffery — and
points to the `anti-ai-writing` skill for a deeper pass when it's installed.

**Building a landing page, hero, portfolio, or other marketing surface?** Load
**`references/marketing-layout.md`** first — it covers hero viewport discipline, eyebrow/label
frequency caps, bento grid rules, marquee limits, and image/logo strategy. These rules are
specific to marketing-style pages; they don't apply to dashboards or dense product UI, where
`design.md` and Section 3's chosen system should drive layout instead.

**Adding scroll-driven or physics-based animation?** Load **`references/animation-code.md`**
for canonical, correct GSAP/Motion skeletons (sticky-stack, horizontal-pan, scroll-reveal) —
scroll-hijack animations are easy to get subtly wrong (pinning at the wrong scroll offset,
missing cleanup) and these skeletons are copy-correct.

**Working on a redesign rather than a greenfield build?** Load
**`references/redesign-protocol.md`** — misclassifying "preserve the brand" vs. "overhaul it"
is the single biggest source of bad redesign output, and there are hard rules about what should
never change silently (URL structure, form field names, nav labels).

Want inspiration or a shared vocabulary for describing patterns (bento grid, sticky-stack,
magnetic button, kinetic marquee)? **`references/pattern-vocabulary.md`** is a naming reference,
not a rulebook — read it when you want a menu of options, not as a checklist to satisfy.

---

## 5. Performance & Accessibility (Non-Negotiable)

Regardless of dials or aesthetic:
- Animate only `transform` and `opacity` — never `top`/`left`/`width`/`height`.
- Any motion above `MOTION_INTENSITY 3` must honor `prefers-reduced-motion` and degrade to
  static, not just slow down.
- Design for light and dark mode from the start unless the brief is explicitly single-mode.
  WCAG AA contrast minimum (4.5:1 body text), AAA target for hero copy. No pure `#000000` or
  `#ffffff` — use off-black/off-white for depth.
- Every interactive element needs the full state cycle: default → hover → focus → active →
  loading → disabled → error → success. No "static successful state only."
- Every image needs `alt` text; every icon-only button needs `aria-label`; focus rings are
  never removed.

---

## 6. Pre-Flight Check (Run Before Calling Anything Done)

This is the last filter before shipping. Run through it; if something fails, fix it, don't
just note it.

**Run the mechanical check first, not last.** Self-auditing your own output for tells is the
weakest link here — you're asking the model that just wrote the code to notice its own
reflexes. Before the checklist below, run:

```bash
python3 <path-to-this-skill>/scripts/audit_ai_tells.py <file-or-directory-you-just-wrote> \
  --design-md <path-to-design.md>   # omit to let it auto-search upward for one
```

It catches everything that's mechanically string-matchable (em-dashes, banned hex codes, banned
fonts, filler verbs, puffery, generic placeholder names, negative-parallelism taglines, eyebrow
over-frequency), plus two checks that need real color math rather than a keyword list: **any
hardcoded hex not declared in `design.md`** (aggregated per unique color, so one repeated
dark-mode extension reads as one finding, not fifty), and **WCAG contrast ratio** for any
text/background pair expressed as literal hex or white/black in the same `className` — catching
the white-on-white button tell for real instead of asking the model to eyeball it. It exits
non-zero on anything hard-banned. It does **not** catch structural or judgment calls — section
repetition, whether copy actually sounds right, bento cell counts, or contrast for colors that
come from Tailwind's named palette or CSS variables rather than literal hex — the checklist
below still needs a real read-through for those.

- [ ] **Design Read** stated (Section 1), and `design.md` checked first if it exists.
- [ ] Every token that `design.md` specifies (color, spacing, type scale, components) is
      actually used — no ad-hoc hex codes or arbitrary spacing when a token exists.
- [ ] Dial values are reasoned from the brief/design.md, not silently defaulted.
- [ ] Zero em-dashes anywhere in visible copy.
- [ ] One accent color, one corner-radius system, one light/dark theme — used consistently
      across every section, not drifting partway through.
- [ ] Every CTA/button text is readable against its background (no white-on-white).
- [ ] Every visible string re-read for grammatical breakage or AI-sounding filler copy.
- [ ] Both light and dark mode actually opened and checked, not just assumed to work.
- [ ] Real images/icons used — no div-based fake screenshots, no hand-rolled decorative SVGs
      standing in for real assets.

Building a marketing/landing page? Also run the marketing-specific checklist in
`references/pre-flight-checklist.md` (hero viewport, eyebrow count, bento cell count, CTA
duplication, and more) — it's mechanical and easy to skip by accident.

---

## Out of Scope

This skill is about visual/interaction execution and taste. It does not:
- Design user flows, IA, or cross-screen navigation — use `product-designer` for that first.
- Replace a project's own enforced design system — if a project-specific design-review skill
  exists (checking compliance against its own DS spec), that skill's checklist is authoritative
  for compliance; this skill handles what it doesn't cover.
- Skin code editors, native mobile apps, or realtime collaboration UIs (cursors, presence) —
  those need their platform's own conventions (Monaco/CodeMirror, Apple HIG/Material, etc.).
