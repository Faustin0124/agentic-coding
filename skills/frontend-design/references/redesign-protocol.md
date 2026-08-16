# Redesign Protocol

Load this when the task is a redesign rather than a greenfield build. Misclassifying which mode
you're in — preserve vs. overhaul — is the single biggest source of bad redesign output.

---

## Detect the Mode First

* **Greenfield** — no existing site, or a full overhaul is explicitly approved. Use the dial
  baseline from `SKILL.md` Section 2 directly.
* **Redesign — Preserve** — modernize without breaking the brand. Audit first, extract brand
  tokens, evolve gradually.
* **Redesign — Overhaul** — a new visual language on top of existing content. Treat visuals as
  greenfield; preserve content and information architecture.

If ambiguous, ask exactly one question: *"Should this redesign preserve the existing brand, or
are we starting visually from scratch?"*

## Audit Before Touching Anything

Document the current state before proposing changes:
* **Brand tokens** — primary/accent colors, type stack, logo treatment, radii.
* **Information architecture** — page tree, primary nav, key conversion paths.
* **Content blocks** — what exists, what's doing work, what's filler.
* **Patterns to preserve** — signature interactions, a recognizable hero, the copy voice.
* **Patterns to retire** — AI-slop tells, broken layouts, dead links, generic stock imagery,
  performance traps.
* **Dial reading of the existing site** — infer its current `DESIGN_VARIANCE`/
  `MOTION_INTENSITY`/`VISUAL_DENSITY`. That's the starting point, not the Section 2 baseline.
* **SEO baseline** — current ranking pages, meta titles, structured data, OG cards. SEO
  migration is the #1 redesign risk — get this before touching markup.

**No live artifact to inspect?** If the brief describes the existing product in prose only (no
repo, no URL, no screenshot available), audit against the brief's own language instead —
extract the same categories (what's being preserved, what's explicitly called out as bad) from
what the user said, and say plainly that this is an audit-by-description, not an audit-by-
inspection. Don't skip the audit step just because there's nothing to click through.

## Preservation Rules

* Don't change information architecture unless asked — keep page slugs, anchor IDs, and
  primary nav labels stable for SEO and muscle memory.
* Extract brand colors before applying the color-calibration rules in `anti-cliches.md` — a
  brand that's already purple stays purple; that's the override condition for the purple-glow
  rule, not an exception to work around.
* Preserve copy voice unless a rewrite is explicitly requested — visual modernization is not
  the same task as a content rewrite.
* Honor existing accessibility wins — don't regress focus states, alt text, keyboard nav, or
  contrast that already worked.
* Respect existing analytics events — don't rename buttons, form fields, or section IDs that
  downstream tracking depends on.

## Modernization Levers, in Priority Order

Apply in order and stop once the brief is satisfied — later levers are progressively riskier:
1. **Typography refresh** — the biggest visual lift per unit of risk.
2. **Spacing & rhythm** — increase section padding, fix vertical rhythm.
3. **Color recalibration** — desaturate, unify neutrals, keep the brand accent.
4. **Motion layer** — add dial-appropriate micro-interactions to existing components.
5. **Hero & key-section recomposition** — restructure top-of-funnel using the layout vocabulary
   in `pattern-vocabulary.md`.
6. **Full block replacement** — only when the existing block is genuinely unsalvageable.

## Decision Tree: Targeted Evolution vs. Full Redesign

* IA, content, and SEO are sound → **targeted evolution** (levers 1–4). Roughly 70% of the
  value at 40% of the risk.
* Visual debt is structural (broken IA, no design system, broken mobile) → **full redesign**
  with strict content preservation.
* The brand itself is changing → **greenfield**.

## What Never Changes Silently

Never modify these without explicit user approval, even mid-redesign:
* URL structure / route slugs.
* Primary nav labels.
* Form field names or order (breaks analytics and browser autofill).
* Brand logo or wordmark.
* Existing legal / consent / cookie copy.
