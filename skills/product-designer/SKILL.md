---
name: product-designer
description: >
  Expert Product Designer: user flow strategy, information architecture, and UI code execution.
  Use this skill for: designing user flows, navigation architecture, or cross-screen journeys;
  planning what screens a feature needs; reviewing and critiquing existing UI/UX for structural,
  functional, or conversion issues; making design-system decisions when no design.md exists yet;
  building interfaces with React/Tailwind/shadcn/ui; vibecoding in Lovable; writing Lovable
  prompts for UI screens. ALWAYS trigger for: "design the flow", "map the user journey", "what
  screens do I need", "how does the user get from X to Y", "review my UI", "improve UX", "this
  feels off", "what's wrong with this design". Also trigger for: wireframe → code, component
  design, design-system setup, accessibility review. Every UI decision has product impact —
  trigger broadly.
---

# Product Designer Skill

Full-spectrum product design: from strategic design decisions (flows, information architecture,
navigation) to production-grade UI code. This skill owns the **structural and strategic** layer
— what screens exist, how users move between them, what a component's API and states need to
be, whether the flow actually works.

**For visual taste and anti-"AI slop" execution** — typography choices, color calibration,
layout diversification, motion, the mechanical pre-flight audit — use the `frontend-design`
skill. The two are complementary, not overlapping: plan the flow and structure here, then hand
visual polish to `frontend-design` once you know what you're building. On a small task where
both matter, load both; don't duplicate one skill's rules inside the other.

**Primary stack**: React + Tailwind CSS + shadcn/ui
**Secondary stacks**: Next.js, Vue, HTML/CSS, React Native, Flutter

---

## 0. Design Process: When to Do What

Before touching code, choose the right mode:

| Situation | Mode | First Step |
|-----------|------|-----------|
| New product / new screen | **Discovery → Flow → Build** | Section 1 → 1.3 → 3 |
| "What screens do I need?" | **Flow Mapping** | Section 1.3 |
| User journey / navigation | **Flow Design** | Section 1.3 |
| Existing UI to improve | **Review → Decide → Fix** | Section 4 → 3 |
| Specific component request | **Component Design** | Section 3 |
| "This looks off" feedback | **Diagnosis** | Section 4, then `frontend-design` for the fix |
| No design system yet | **Design System Setup** | Section 2 |

---

## 1. Discovery & Design Decisions (Strategic Layer)

Do this before building anything non-trivial.

### 1.1 — Understand the Context

Answer these before designing:
- **Who is the user?** (persona, tech level, emotional state at arrival)
- **What is the job to be done?** (primary action this screen/flow enables)
- **What does success look like?** (conversion, comprehension, task completion, trust)
- **What device context?** (mobile-first? dashboard on desktop? both?)
- **What brand signal does this need to emit?** (trust, innovation, warmth, authority)

### 1.2 — Information Architecture

Before layout, define:
- **Content inventory**: What must exist on this screen?
- **Priority ranking**: What must the user see/do first?
- **Navigation model**: Where does this screen fit in the flow? What comes before/after?
- **Empty/loading/error states**: Define all 5 states per component: default, loading, empty, error, success

### 1.3 — User Flow & Product Navigation

Use this when: designing a new product, planning screens for a feature, or auditing navigation coherence.

#### Flow Mapping Process

1. **Identify entry points** — where does the user enter? (direct URL, email CTA, onboarding, nav)
2. **Map the critical path** — the shortest path from entry to primary value delivery
3. **Identify decision points** — where does the user choose? (branch points in the flow)
4. **Define exits** — success exit, abandonment exit, error exit, and where they go
5. **Mark friction points** — where do users get confused, blocked, or lost?

#### Flow Documentation Format

```
FLOW: [Feature/Journey name]
Entry: [How user arrives]
Goal: [What user needs to accomplish]

Step 1: [Screen name]
  → Primary action: [CTA label]
  → Secondary action: [Optional path]
  → Exit/abandon: [What if user leaves?]

Step 2: [Screen name]
  → ...

Success: [Where user lands after completing goal]
Error path: [What happens on failure]
```

Apply this format to whatever the product actually is — an onboarding flow, a checkout, a
multi-step form, a settings journey. There's no universal screen inventory; the flow mapping
process above is what generalizes, not a fixed list of screens.

#### Navigation Architecture Principles

- **Max 3 levels deep** — if a user needs 4+ taps to reach a feature, restructure
- **One primary nav** — sidebar (desktop) or bottom nav (mobile), not both simultaneously
- **Persistent home** — always one tap back to dashboard from anywhere
- **Breadcrumbs** for 3+ level hierarchies on desktop
- **No dead ends** — every empty state has a CTA to the next action
- **Back = previous screen** always; never unexpected resets

#### Flow Review Checklist

- [ ] Every screen has one clear primary action
- [ ] No screen requires more than 3 taps to reach from home
- [ ] All error states have recovery paths (not just "go back")
- [ ] Onboarding flow ends at first value moment (not at account creation)
- [ ] Navigation is consistent: same menu in same position on every screen
- [ ] Confirmation dialogs used for destructive actions only (not for navigation)
- [ ] Deep links work for all primary screens (shareable URLs)

### 1.4 — Design Decisions (Log them)

For any non-trivial screen, document:
```
DESIGN DECISION LOG
Screen: [Name]
Primary job: [User's goal]
Comes from: [Previous screen/entry point]
Goes to: [Next screen on success]
Layout choice: [Why this structure]
Visual tone: [Style rationale]
Key trade-offs: [What was sacrificed for simplicity/performance/clarity]
```

---

## 2. Design System (Visual Foundation)

### 2.0 — Check for design.md First

If the project has a `design.md` (or `DESIGN.md`, `docs/design.md`) at its root, **that's the
design system** — tokens, typography, spacing, and component conventions all come from there,
not from this section. `frontend-design` documents the same rule and the exhaustive taste rules
that go with it; this section is only for the gap `frontend-design` doesn't cover: **setting up
a design system from scratch** when none exists yet.

### 2.1 — No design.md Yet? Establish One

Rather than picking colors and spacing ad hoc per screen, define a minimal system once and
write it down as the project's `design.md` so every future task — by this skill, by
`frontend-design`, by a human — has one source of truth. A minimal system needs:

- **Semantic color tokens**, not raw hex scattered through components. A common starting set:

  | Token | Purpose |
  |-------|---------|
  | `primary` | Action CTAs, accents |
  | `success` | Positive confirmations, gains |
  | `destructive` | Warnings, deletes, errors |
  | `warning` | Alerts, cautions |
  | `foreground` / `background` | Text and page base |
  | `card` / `border` | Surface and divider colors |

  How many semantic colors and how they map to actual hex values is a brand decision — this
  skill doesn't prescribe a number or a palette. What matters is that they're *semantic*
  (named by purpose) rather than raw hex reused inconsistently, and that they're written down.

- **A typography scale** — pick a small, deliberate set of sizes (e.g. 12/14/16/18/24/32/48)
  rather than arbitrary values per component. Body text 16px minimum, line-height 1.5–1.75,
  60–72 characters per line for prose.
- **A spacing grid** — almost always a 4px or 8px base multiple (Tailwind's default scale works
  for most projects). Consistency matters more than which base you pick.
- **Touch targets** — minimum 44×44px (iOS) / 48×48px (Android) for anything tappable.

Once these are decided, write them into `design.md` at the project root before building more
screens — that turns a one-time decision into a reusable contract instead of something that has
to be re-derived (or silently drifts) on every new component.

**What this section deliberately doesn't decide:** exact colors, exact font families, icon
library, motion style, or any of the taste/anti-cliché judgment calls. Once `design.md` exists
(even a first draft), hand those to `frontend-design` — it's built for exactly that layer and
has the anti-slop discipline this skill doesn't duplicate.

---

## 3. Component Implementation

### 3.1 — shadcn/ui (Primary Layer)

Prefer shadcn primitives over hand-rolled components when the project already uses shadcn/ui
(check `components.json` or an existing `components/ui/` folder) or when starting fresh with no
constraint against it.

```tsx
// Preferred: shadcn primitive, semantic tokens, no custom button
import { Button } from "@/components/ui/button"

<Button variant="default" className="gap-2">
  <Plus className="h-4 w-4" />
  Add item
</Button>

// Avoid: hand-rolled button styling when a shadcn primitive already exists
<button className="bg-blue-600 text-white px-4 py-2 rounded">
```

If the project uses a different component library or none at all, apply the same principle —
reuse existing primitives before writing new ones — rather than forcing shadcn/ui in.

### 3.2 — Component API

All components should have:
- `variant` prop (default, destructive, ghost, outline)
- `size` prop (sm, md, lg)
- `isLoading` state (disable + spinner)
- `disabled` state
- Forwarded `ref` for form integration
- TypeScript props interface

### 3.3 — Tailwind Patterns

```tsx
// Colors: semantic tokens, not raw hex
className="bg-card border border-border hover:bg-background"

// Callouts: accent left-border rather than a full tinted background
className="bg-card border border-border border-l-[3px] border-l-success"

// Numeric/tabular data (financial figures, metrics tables): tabular, right-aligned
className="font-mono tabular-nums text-right"

// Spacing: consistent grid, not arbitrary pixels
className="gap-4 p-6 mb-6"
```

Icon library, exact color values, and whether gradients/tinted backgrounds are acceptable are
taste calls that belong to `design.md` and `frontend-design`, not fixed rules here — this skill
only asserts that whatever the choice is, it should be applied consistently via semantic
classes/tokens rather than one-off values per component.

### 3.4 — State Hierarchy

All interactive elements need:
```
default → hover → focus → active → loading → disabled → error → success
```

### 3.5 — React Performance

- `useMemo` for expensive computations only
- `React.memo` for 10+ list items
- Lazy load: `const Chart = lazy(() => import('./Chart'))`
- Virtualize lists > 50 items (tanstack/virtual)

---

## 4. UI Review & Critique Framework

This framework checks **structure and function** — whether the UI works, is consistent, and is
accessible. It deliberately does not check visual taste (font pairing, color sophistication,
"does this look templated") — that's `frontend-design`'s pre-flight check and mechanical audit
script. Run both when reviewing a finished screen; they don't overlap.

### 4.0 — Quick Audit

1. What's the ONE thing the user does here? Obvious in <3 seconds?
2. What dominates visually? Should it?
3. What would a first-timer misunderstand?
4. What's the friction point?

### 4.1 — Full Critique Checklist

#### 🔴 Critical (block delivery)

- [ ] **design.md compliance** — tokens, spacing, and component conventions actually used, not
      ad-hoc values (if `design.md` exists; otherwise flag that one should be written per
      Section 2)
- [ ] **Contrast** — 4.5:1 minimum for body text (WCAG AA)
- [ ] **Touch targets** — 44×44px minimum on mobile
- [ ] **No horizontal scroll** — ever, on any breakpoint
- [ ] **Loading/error states** — all defined
- [ ] **Primary action** — one clear CTA per screen

#### 🟠 High Priority (fix before launch)

- [ ] **Spacing** — consistent grid; no arbitrary pixels
- [ ] **Colors** — semantic tokens used consistently; no raw hex scattered through components
- [ ] **Typography** — sticks to the project's declared scale
- [ ] **All states defined** — empty, loading, error, success
- [ ] **Navigation consistent** — same placement, all screens
- [ ] **No dead ends** — every empty state has a next action

#### 🟡 Medium (next sprint)

- [ ] Responsive tested at 375 / 768 / 1280 / 1440px
- [ ] Back navigation restores scroll + filters
- [ ] Animations 150–300ms, transform/opacity only
- [ ] Dark mode tokens mapped
- [ ] Accessibility: keyboard nav, focus rings, alt text

#### ✅ What's working

- [Specific praise]

---

## 5. Lovable Integration

Structure prompts for Lovable:

```
[Component name]
Stack: React + Tailwind + shadcn/ui
Design system: design.md (or: none yet — see Section 2 before prompting)
Variant: [style choice]
Data: [props shape]
States: [all states needed]
Constraints (from design.md, or defaults if none):
  - Semantic color tokens only, no raw hex
  - Consistent spacing grid
  - No emoji icons unless the brief explicitly wants that tone
Do NOT: use emoji icons unless requested, inline styles, custom components when a project
primitive already exists
```

### Common Lovable Pitfalls

- Uses `useState` instead of React Query — **specify data fetching approach**
- Inline styles instead of Tailwind — **"Tailwind only, no inline styles"**
- Custom components over existing primitives — **"reuse the project's existing components"**
- Missing states — **"include loading, error, empty, success states"**
- Tinted backgrounds where the design system forbids them — **state the actual constraint from
  design.md, don't assume**

---

## 6. Accessibility Baseline

Non-negotiable:

```tsx
// Images
<img alt="Description" src={...} />

// Icon buttons
<Button aria-label="Delete">
  <Trash2 className="h-4 w-4" aria-hidden="true" />
</Button>

// Form errors
<Input aria-invalid={!!error} aria-describedby="error-id" />
<p id="error-id" role="alert">{error}</p>

// Focus rings (never removed)
className="focus-visible:ring-2 focus-visible:ring-offset-2"

// Keyboard: Tab order, Escape closes modals, Enter activates
// Dark mode: prefers-color-scheme respected
// Motion: prefers-reduced-motion disables animations
```

---

## References

This skill intentionally doesn't ship a references/ folder of project-specific design-system
docs — that's what each project's own `design.md` is for. If a project has one, it's the source
of truth for Sections 2–5 above. For the visual-taste rules this skill doesn't cover (anti-AI-
slop discipline, animation patterns, redesign protocol), see the `frontend-design` skill's
`references/` folder.
