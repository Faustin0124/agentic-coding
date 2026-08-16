# Anti-Cliché Reference

Exhaustive bias-correction rules for frontend output. Every rule is **contextual** — it states
its own override condition. Apply it when it fits the design read from `SKILL.md` Section 1;
skip it when `design.md` already dictates the answer or the brief genuinely calls for the
opposite. This file is dense on purpose — skim for the sections relevant to the current task.

---

## Typography

* **Sans font choice:** Inter is discouraged as the unexamined default. Pick `Geist`,
  `Outfit`, `Cabinet Grotesk`, `Satoshi`, or a brand-appropriate serif first.
  **Override:** Inter is fine when the brief explicitly wants a neutral/standard/Linear-style
  feel, or the brief is public-sector/accessibility-first.
* **Pairings to know:** `Geist` + `Geist Mono`, `Satoshi` + `JetBrains Mono`, `Cabinet Grotesk`
  + `Inter Tight`, `GT America` + `IBM Plex Mono`.
* **Check where a font actually loads from before committing to it.** `Geist` and `Inter Tight`
  are on Google Fonts and drop straight into `next/font/google`. `Satoshi`, `Cabinet Grotesk`,
  and `General Sans` are Fontshare fonts — they need a self-hosted `next/font/local` setup or a
  Fontshare `@import`/CSS link, not `next/font/google`. Don't silently swap in a Google-hosted
  lookalike; either wire up the real loading path or say so in the code comments.
* **Serif discipline (the most-tested AI tell):** "It feels creative/premium/editorial" is not
  a reason to reach for serif. Serif is only justified when the brand brief literally names one,
  or the aesthetic family is genuinely editorial/luxury/publication/heritage and you can
  articulate why this specific serif fits this specific brand. Otherwise: sans-serif display
  (Geist Display, ABC Diatype, Söhne Breit, Cabinet Grotesk Display, PP Neue Montreal).
  **Specifically banned as defaults:** `Fraunces` and `Instrument_Serif` — the two LLM-favorite
  display serifs. If a serif is genuinely justified, rotate rather than reusing the same one
  across projects: PP Editorial New, GT Sectra Display, Cardinal Grotesque, Reckless Neue,
  Tiempos Headline, Recoleta, Cormorant Garamond, Playfair Display, EB Garamond, Canela, Domaine
  Display, Schnyder, Tobias.
* **Emphasis within a headline** (the "and `spatial` design" move): use italic or bold of the
  *same* font family. Injecting a random serif word into a sans headline (or vice versa) reads
  as amateur — mixed-family emphasis is a tell, same-family italic/bold is the right move.
* **Italic descender clearance:** when italic display type includes a descender letter
  (`y g j p q`), `leading-none`/`leading-[1]` clips it. Use `leading-[1.1]` minimum and add
  `pb-1`/`mb-1` reserve on the wrapping element. Audit every italic word in display headlines.
* **Display / headline scale default:** `text-4xl md:text-6xl tracking-tighter leading-none`.
* **Body scale default:** `text-base text-gray-600 leading-relaxed max-w-[65ch]`.
* Avoid oversized H1s that just scream — control hierarchy with weight and color, not raw scale.

## Color Calibration

* Max one *brand* accent color per project, saturation under 80% by default. This is about the
  brand accent, not about color in general — semantic/status colors (a green "available" dot,
  a red error state, an amber warning) are a separate system and don't count against the
  one-accent rule. Keep the semantic palette small and consistent (e.g. always the same green
  for "success"/"available") rather than reusing the brand accent for status meaning.
* **The purple-glow reflex:** the "AI purple/blue glow" aesthetic (automatic purple button
  glows, random neon gradients) is discouraged as a default. Use neutral bases (zinc/slate/stone)
  with a single high-contrast accent (emerald, electric blue, deep rose, burnt orange).
  **Override:** if the brand or brief explicitly wants purple/violet, embrace it — but execute
  with intent: consistent palette, harmonized neutrals, restrained gradients.
* **One palette per project** — don't fluctuate between warm and cool grays within one build.
* **Color consistency lock:** once an accent is chosen, it's used on the whole page. A
  warm-grey site doesn't suddenly get a blue CTA in section 7. Audit every component before
  shipping.
* **Premium-consumer palette ban:** for premium-consumer briefs (cookware, wellness, artisan,
  luxury, heritage craft, DTC home goods) the reflexive palette is warm beige/cream +
  brass/clay/oxblood/ochre + espresso/near-black text. Concretely discouraged as defaults:
  - Backgrounds: `#f5f1ea`, `#f7f5f1`, `#fbf8f1`, `#efeae0`, `#ece6db`, `#faf7f1`, `#e8dfcb`
  - Accents: `#b08947`, `#b6553a`, `#9a2436`, `#9c6e2a`, `#bc7c3a`, `#7d5621`
  - Text: `#1a1714`, `#1a1814`, `#1b1814`
  Every premium-consumer site anyone has ever generated with an LLM uses roughly this palette —
  the brand becomes invisible. Rotate instead: **Cold Luxury** (silver-grey + chrome + smoke),
  **Forest** (deep green + bone + amber), **Black and Tan** (true off-black + warm tan, sharp
  contrast, no beige), **Cobalt + Cream**, **Terracotta + Slate**, **Olive + Brick + Paper**,
  or **pure monochrome + one saturated pop**. Don't ship the same warm-craft palette twice in a
  row. **Override:** acceptable when the brand brief explicitly names those colors, or the
  identity is genuinely vintage/artisan/warm-craft and you can articulate why.

## Layout Diversification

* **Anti-center bias:** centered hero/H1 is avoided when `DESIGN_VARIANCE > 4` — prefer split
  screen (50/50), left-aligned content with a right-aligned asset, or asymmetric whitespace.
  **Override:** centered hero is fine for editorial/manifesto/launch-announcement briefs where
  the message itself is the design.
* **No three identical horizontal feature cards** as the generic default. Use 2-column
  zig-zag, an asymmetric grid, scroll-pinned sections, or horizontal scroll instead.
* Mathematically perfect padding/margins beat floating elements with awkward gaps — but don't
  let "perfect" collapse into "generic": intentional asymmetry above `DESIGN_VARIANCE 4` is a
  feature, not sloppiness.

## Materiality, Shadows, Cards

* Use cards only when elevation communicates real hierarchy; otherwise group with `border-t`,
  `divide-y`, or negative space instead of wrapping everything in a card.
* Tint shadows to the background hue — no pure-black drop shadows on light backgrounds.
* For `VISUAL_DENSITY > 7`, generic card containers are discouraged; let data breathe in a
  plain layout instead.
* **Shape consistency lock:** pick one corner-radius scale for the page (all-sharp, all-soft
  12–16px, or all-pill for interactive elements) and stick to it. Mixed systems are only okay
  with a documented rule ("buttons are full-pill, cards are 16px, inputs are 8px") followed
  everywhere — round buttons in an otherwise square layout is broken, not stylistic.

## Interactive States & Forms

* LLMs default to "static successful state only" — always implement the full cycle: default,
  loading (skeletal loaders matching the final layout's shape, not generic spinners), empty
  (composed, with a clear next action), error (inline for forms, toast only for transient
  messages), and a tactile `:active` state (`-translate-y-[1px]` or `scale-[0.98]`).
* **Button contrast check:** before shipping any button, verify the label is readable against
  its background — white-on-white, `bg-white` CTA with `text-white` label, or a transparent
  button with no border against a matching page background are all broken. WCAG AA minimum
  (4.5:1 body, 3:1 for 18px+ text). Same rule for ghost buttons over photographic backgrounds —
  use a scrim, backdrop, or stroke.
* **CTA text must fit on one line at desktop.** If a label wraps to 2–3 lines, either shorten it
  (3 words max for primary CTAs, ideally 1–2) or widen the button — don't constrain
  `max-width` artificially.
* **No duplicate CTA intent on one page.** "Get in touch" + "Contact us" + "Let's talk" are all
  the same intent — pick one label and reuse it everywhere (nav, hero, footer). Same for
  "Try free"/"Get started"/"Sign up free" (signup intent) and "View work"/"See selected
  work"/"Browse projects" (portfolio intent).
* **Form contrast check:** inputs, placeholders, focus rings, helper text, and error text all
  need to pass WCAG AA against the section background.
* Label above input, helper text present in markup, error text below the input. No
  placeholder-as-label, ever.

## Content Density

* Landing pages live on first impression, not the full read — default content shape per
  section is a short headline (≤8 words), a short sub-paragraph (≤25 words), and one visual
  asset or CTA. Anything more needs to be justified by the section's job.
* No data-dump sections on a marketing page — a 20-row table or 30-row list is the wrong
  layout there. Use top highlights + a "view full list" link, a carousel, or route the data to
  a dedicated page instead.
* Long lists (>5 items) need a component upgrade, not a longer `<ul>` — reach for a 2-column
  split, a card grid, tabs/accordion, scroll-snap pills, or a carousel instead of the default
  bulleted/divided list.
* **Copy self-audit (mandatory before shipping):** re-read every visible string — headlines,
  buttons, captions, alt text, error messages. Flag and rewrite anything grammatically broken,
  with unclear referents, that sounds like an AI hallucination (forced metaphors, cute wordplay
  that doesn't track), or reads like an LLM performing thoughtfulness. Plain functional copy
  beats broken cute copy.
* **Fake-precise numbers are flagged.** `92%`, `4.1×`, `48k` are fine when they come from real
  data or are explicitly labeled as mock/example — banned when they're just invented spec
  aesthetics the brand doesn't actually claim.
* One copy register per page — don't mix technical mono, editorial prose, and marketing punch
  in the same composition unless the brand voice explicitly calls for it.

## Copy Patterns That Read as AI-Written

Beyond the em-dash ban and the filler-verb/puffery list already covered above, a handful of
*sentence-structure* patterns are just as recognizable as an AI tell as any word choice — and
harder to catch by skimming, because each individual sentence reads fine in isolation. These are
adapted from the `anti-ai-writing` skill (a much deeper reference built for detecting AI prose,
originally written for Wikipedia articles — its citation/notability-specific sections don't
apply here, but its vocabulary and structural-pattern sections transfer directly to marketing
and product copy). **If that skill is installed in the current environment, load it for the
full vocabulary and worked examples when doing a serious copy pass** — what follows is the
condensed, UI-relevant subset so this skill doesn't depend on the other one being present.

* **Negative parallelism — "not just X, but Y" / "it's not X, it's Y."** The single most
  common AI tagline construction: *"Not just a tool, it's a movement"*, *"It's not about
  features, it's about outcomes."* It reads as balanced and clever the first time and as a tic
  by the third headline that uses it. Say the thing directly instead of setting up a strawman to
  knock down.
* **Rule-of-three overuse.** "Fast, flexible, and free." "Built for teams, built for scale,
  built for the future." Three-item lists (adjectives or short phrases) make a claim sound more
  substantiated than it is. One well-chosen benefit beats three vague ones stacked for rhythm.
* **Elegant variation.** Renaming the same thing across a page to avoid repetition — "our
  platform... this tool... the solution... what we've built" — reads as evasive rather than
  varied. If it's the product, call it the same thing every time.
* **Unsupported/vague attribution.** "Industry reports show...", "Experts agree...", "Businesses
  everywhere are switching to..." without a name, a number, or a source attached. If there's no
  real data or named source behind a claim, cut the claim rather than dress it up as consensus.
* **Puffery beyond single words** — phrases like *"a testament to our commitment"*, *"plays a
  vital role in"*, *"underscores the importance of"*, *"represents a significant step forward."*
  These inflate significance without adding information; a reader learns nothing they didn't
  already know from the sentence around it.
* **Formulaic hedges and disclaimers** in helper/microcopy — *"it's important to note that..."*,
  *"results may vary"*, *"please note that"* — usually add throat-clearing, not information. Say
  the actual caveat plainly or drop it.
* **Leftover chatbot voice**, if the product includes an AI feature or assistant whose copy you're
  writing: *"I hope this helps!"*, *"Let me know if you have questions"*, *"Here's a breakdown
  of..."* as UI copy (not actual conversational output) reads as an unedited AI draft, not
  product voice.

## Quotes & Testimonials

* Max 3 lines of quote body (a landing-page quote is a snippet, not the full review).
* No em-dash inside quote text as a design flourish (see the global em-dash ban below).
* Attribution: name + role + optionally company — never name alone.
* Use real typographic quote marks (" ") or none — never straight ASCII quotes.

## Dark Mode

* Design for both modes from the start; never ship light-only or dark-only without explicit
  instruction.
* Pick one token strategy per project and stick to it: Tailwind `dark:` variant paired on every
  color utility, or CSS variables (`--surface`, `--text-primary`, etc.) swapped under
  `[data-theme="dark"]`/`prefers-color-scheme`.
* This skill doesn't prescribe specific dark-mode colors — the brief/`design.md` decides. It
  enforces contrast (WCAG AA body, AAA hero copy target), hierarchy parity (whatever pops in
  light must pop in dark), and brand fidelity (the primary brand color stays recognizable, not
  desaturated away).
* No pure `#000000` or `#ffffff` — use off-black/off-white for depth.
* **Page theme lock:** the page has one theme. If it's dark, all sections are dark — no
  light-mode-warm-paper section sandwiched between dark ones. The one exception: a deliberate,
  brief-requested "theme switch on scroll" device, done once per page as a real composition, not
  random alternation.
* Open the page in both modes before calling it done — don't ship having only checked one.

## The Em-Dash Ban

**Em-dash (`—`) is completely banned** from all visible UI copy — headlines, eyebrows, labels,
pills, button text, captions, nav items, body copy, quote attribution. No "limited use"
allowance, no "it's fine in body copy" exception. It's the single most common LLM writing tell.
Rewrite with a period, a comma, parentheses, a colon, or a regular hyphen. En-dash (`–`) used as
a separator is banned too — date and number ranges use a hyphen (`2018-2026`, `€40-80k`). The
only permitted dash characters are the regular hyphen and the math minus sign. If a `—` or `–`
appears anywhere in visible output, treat it as a pre-flight failure and rewrite before shipping.

## Other AI Tells Worth Knowing

* No neon/outer glows by default — use inner borders or subtle tinted shadows instead.
* No custom mouse cursors — outdated, accessibility-hostile, and a performance cost for no
  real benefit.
* No generic placeholder names ("John Doe", "Sarah Chan") — use creative, realistic,
  locale-appropriate names. No generic "egg" avatar icons — use believable photo placeholders.
* No startup-slop brand names ("Acme", "Nexus", "SmartFlow", "Cloudly") — invent something that
  sounds like it could be real.
* No filler verbs in copy ("Elevate", "Seamless", "Unleash", "Next-Gen", "Revolutionize") —
  write concretely about what the thing actually does.
* No hand-rolled SVG icons — use an icon library (Section 3 of `SKILL.md`); compose from
  primitives or add a second library rather than drawing icon paths by hand.
* No div-based fake screenshots simulating a product UI — use a real screenshot, a generated
  image, a real component preview, or skip the preview entirely.
* shadcn/ui components are fine, but never in their untouched default state — customize radii,
  color, shadow, and typography to the project's actual aesthetic.
