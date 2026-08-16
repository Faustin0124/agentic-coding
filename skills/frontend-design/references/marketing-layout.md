# Marketing & Landing Page Layout Discipline

Load this when building a landing page, hero section, portfolio, or other marketing-style
surface. These rules are about first-impression, above-the-fold, scroll-driven composition —
they don't apply to dashboards or dense product UI, where `design.md` and the chosen component
system (see `SKILL.md` Section 3) should drive layout instead.

---

## Hero Discipline (Hard Rules)

* **The hero must fit the initial viewport.** Headline max 2 lines on desktop, subtext max 20
  words and max 3–4 lines, CTAs visible without scrolling. If copy is too long, reduce the font
  scale or cut copy — don't let the hero overflow and force a scroll just to find the CTA.
* **Plan font size and image size together.** If the hero asset is large and the headline is
  more than 6 words, don't start at `text-7xl`/`text-8xl`. Sensible default:
  `text-4xl md:text-5xl lg:text-6xl` for most heroes, `text-6xl md:text-7xl` only for 3–5 word
  headlines. A 4-line hero headline is a font-size error, not a copy-length problem.
* **Hero top padding caps at `pt-24` (~6rem) at desktop.** More than that and the content
  floats halfway down the viewport, reading as a layout bug rather than intentional space. Need
  more breathing room? Increase font/asset scale, not top padding.
* **Hero stack: max 4 text elements.** The hero is one moment, not a feature list:
  1. Eyebrow OR brand strip — pick zero or one, never both.
  2. Headline (max 2 lines).
  3. Subtext (max 20 words, max 4 lines).
  4. CTAs (1 primary + max 1 secondary).
  Banned inside the hero: a tiny tagline below the CTAs, a trust micro-strip ("Used by
  engineering teams at..."), a pricing teaser, a feature bullet list, a social-proof avatar row.
  All of those belong in a dedicated section directly below the hero.
* **A "Trusted by" logo wall belongs under the hero, never inside it.**
* Hero needs a real visual — text plus a gradient blob is a placeholder, not a hero (see the
  Image Strategy section below).

## Section-Level Repetition

* **Once a layout family is used for a section, it can appear at most once more on the page.**
  "Selected commissions" and "What we do" shouldn't look like the same template. A page with 8
  sections should use at least 4 different layout families.
* **Zigzag alternation cap:** alternating left-image/right-text then left-text/right-image is
  fine for two sections in a row; a third consecutive image+text split is a failure — break the
  pattern with a full-width section, a vertical stack, a bento grid, or a marquee.
* **Split-header ban:** "left big headline + right small explainer paragraph" as a section
  header pattern is discouraged by default — it reads as filler on the right. If both a
  headline and an explainer genuinely belong together, stack them vertically instead
  (headline, then body, max-width 65ch). Reach for the split only when the right column carries
  something real — a visual or interactive element, not filler text.

## Eyebrow Restraint

An eyebrow is the small uppercase label above a section headline
(`text-[11px] uppercase tracking-[0.18em]`). Every AI-built site tends to put one above *every*
section, producing the same templated rhythm.

* **Max 1 eyebrow per 3 sections** (hero counts as 1). A 9-section page uses at most 3 total.
* If section A has an eyebrow, the next 2 sections can't have one.
* Check mechanically: count `uppercase tracking`-style micro-labels across all section
  components; if the count exceeds `ceil(sectionCount / 3)`, cut some.
* What to do instead: drop it. The headline alone is enough — the section's position on the
  page already categorizes it.
* Also avoid: version labels in the hero (`V0.6`, `BETA`, `EARLY ACCESS`) unless the brief is
  genuinely a product launch; section-number eyebrows (`00 / INDEX`, `001 · Capabilities`); and
  micro-meta-sentences under eyebrows explaining what the section is about — the headline
  already does that.

## Bento Grids

* **Cell count matches content count.** 3 items → 3 cells (asymmetric split, not a leftover
  empty tile). 5 items → 5 cells. An empty cell in the middle or at the end means the grid was
  planned wrong — reshape it, don't paste a blank tile.
* **Rhythm, not one-sided repetition** — vary composition: alternate full-width feature rows,
  asymmetric tile sizes, vertical breaks. Six identical left-image/right-text rows in a row is
  the same problem as the zigzag cap above, just inside one grid.
* **Background diversity:** at least 2–3 cells in a multi-cell grid need real visual variation
  (a real image, a brand-appropriate gradient, a pattern, a tinted background) — an all-white,
  text-only bento grid reads as boring AI-default even when the rest of the page is good.

## Marquees & Motion-as-Filler

* **Max one horizontal marquee per page.** Scrolling logo strips, "manifesto scrolling
  sideways", kinetic word strips — pick the one section that actually benefits and give
  everything else a different layout.
* **No decorative status dots** before nav items, list rows, or badges unless the dot conveys
  real semantic state (live server status, an actual availability flag), and even then limit it
  to one per section.
* **No scroll cues** (`Scroll`, `↓ scroll`, animated mouse-wheel icons) — if the user hasn't
  scrolled yet, they're looking at the hero; they know what scrolling is.
* **No locale/time/weather strips** ("Lisbon 14:23 · 18°C") unless the brief is genuinely about
  a globally-distributed studio, a travel brand, or a real physical venue.
* **No decoration text strip at the hero bottom** (`BRAND. MOTION. SPATIAL.`) unless it carries
  real, navigable links or real status info.

## Image & Visual Asset Strategy

Landing pages and portfolios are visual products — text-only pages with fake-screenshot divs
read as unfinished, not minimal.

1. **Use an image-generation tool first**, if one is available in the environment, to create
   section-specific assets (hero photography, product shots, textures). Generate at the right
   aspect ratio for the section.
2. **Real web images second** when no gen tool is available:
   `https://picsum.photos/seed/{descriptive-seed}/{w}/{h}` for placeholder photography (the
   seed should describe the section), or actual stock/brand URLs the brief provides, or
   open-license sources when explicitly allowed.
3. **Last resort: say so.** If neither is possible, don't fill the page with hand-rolled SVG
   illustrations or div-based fake screenshots — leave clearly labeled placeholder slots
   (`<!-- TODO: hero product photo, 1600x1200 -->`) and tell the user what images are needed and
   where.

Even a restrained, minimalist site needs real images — at least 2–3 (hero, one product/lifestyle
shot, one supporting image). A pure-text page is incomplete work, not minimalism.

**Real logos for social proof:** when the brief calls for a "Trusted by" logo wall, don't
default to plain styled text wordmarks. Use real SVG logos from Simple Icons
(`https://cdn.simpleicons.org/{slug}/ffffff`) or devicon for tech-stack logos. For invented
brand names, generate a simple monogram SVG rather than a plain text wordmark. Ensure logos
render in both light and dark mode. **Logo-only rule:** the logo wall is logos and nothing
else — no industry/category label printed underneath each one.

**Div-based fake product previews are banned** — a "hand-built product preview" made of styled
`<div>` rectangles simulating a task list, terminal, or dashboard is one of the most recognizable
LLM-design tells. Use a real screenshot, a generated image, a real component preview, or skip
the preview and use editorial photography instead.

## Content Presentation for Long Data

A long product-spec table with a hairline under every row is a common default for
cookware/hardware/apparel briefs — and the laziest layout choice available. Alternatives:
- **2-col card grid** — each spec gets a card with the spec name, a large display value, and a
  one-line "why it matters."
- **Scroll-snap horizontal pills** — each spec is a pill the user flicks through.
- **Grouped chunks** — cluster related specs (e.g. "Materials", "Cooking", "Warranty") under one
  soft divider and heading per cluster.
- **Featured-vs-rest** — 3–4 hero specs as large display tiles, the rest under a "view full
  specifications" disclosure.
