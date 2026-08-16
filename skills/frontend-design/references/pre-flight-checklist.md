# Marketing-Page Pre-Flight Checklist

The core checklist every task runs lives in `SKILL.md` Section 6. This is the extended version
for landing pages, portfolios, and other marketing-style surfaces — mechanical checks that are
easy to skip by accident because nothing about them "feels wrong" while writing the code.

Run this before calling a marketing page done. If a box fails, fix it before shipping.

- [ ] **Hero fits the viewport:** headline ≤ 2 lines, subtext ≤ 20 words and ≤ 4 lines, CTA
      visible without scrolling, font scale planned around the hero asset size.
- [ ] **Hero top padding** caps at `pt-24` at desktop — content doesn't float halfway down the
      viewport.
- [ ] **Hero stack discipline:** max 4 text elements (eyebrow OR brand strip, headline, subtext,
      CTAs). No tiny tagline below the CTAs, no trust micro-strip inside the hero.
- [ ] **Eyebrow count (mechanical):** count `uppercase tracking`-style micro-labels above
      section headlines across all components. Count ≤ `ceil(sectionCount / 3)`, hero counts
      as 1.
- [ ] **Split-header ban:** no "left big headline + right small explainer paragraph" section
      header pattern (vertical stack instead, unless the right column carries something real).
- [ ] **Zigzag alternation cap:** no 3+ consecutive sections sharing the same image+text-split
      layout.
- [ ] **No duplicate CTA intent:** no two CTAs on the page share the same underlying intent
      with different labels ("Get in touch" + "Let's talk" both present = fail).
- [ ] **Logo wall is logo-only:** no industry/category label printed underneath each logo, real
      SVG logos used (Simple Icons/devicon or a generated mark), not plain text wordmarks.
- [ ] **Bento background diversity:** at least 2–3 cells in any multi-cell grid have real
      visual variation, not all white-on-white text cells.
- [ ] **Bento cell count** matches content count exactly — no empty cell in the middle or end.
- [ ] **Marquee max-one-per-page:** no two horizontal marquees on the same page.
- [ ] **Section-layout repetition:** no layout family repeats more than twice; an 8-section page
      uses at least 4 different families.
- [ ] **Long lists use the right component:** no default `<ul>`/`divide-y` for lists over 5
      items — a card grid, tabs, scroll-snap pills, or carousel instead.
- [ ] **Navigation renders on one line** at desktop, height ≤ 80px.
- [ ] **Real images used:** gen-tool first, then Picsum-seed placeholders, then explicit
      labeled placeholder slots — no div-based fake screenshots, no hand-rolled decorative SVGs,
      no pure-text page standing in for "minimalism."
- [ ] **No pills/labels overlaid directly on images** as decoration.
- [ ] **No photo-credit captions** unless crediting a real photographer for a real, permitted
      photo.
- [ ] **No version footers** (`v1.4.2`, `Build 0048`) on marketing pages — those are
      devtool/CLI fixtures, not landing-page content.
- [ ] **No micro-meta-sentences** under eyebrows explaining what the section is about.
- [ ] **No decoration text strip** at the hero bottom unless it carries real navigable links or
      real status info.
- [ ] **No floating top-right sub-text** in section headings with no clear alignment to
      anything else.
- [ ] **No progress bars with filled background tracks** used purely as decorative comparison
      visuals — prefer a number + small icon, or a bar with no background track.
- [ ] **No locale/time/weather strips** unless the brief is genuinely globally-distributed or
      place-focused.
- [ ] **No scroll cues** (`Scroll`, `↓ scroll to explore`).
- [ ] **No version labels in the hero** (`V0.6`, `BETA`, `INVITE-ONLY`) unless the brief is
      genuinely a product launch.
- [ ] **No section-numbering eyebrows** (`00 / INDEX`, `001 · Capabilities`).
