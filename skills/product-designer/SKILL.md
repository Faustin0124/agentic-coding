---
name: product-designer
description: >
  Expert Product Designer: UI/UX code execution + user flow strategy. Use this skill for: building or designing any interface (landing page, dashboard, SaaS app, mobile, component); designing user flows, navigation architecture, or cross-screen journeys; reviewing and critiquing existing UI/UX for quality, consistency, or conversion issues; making design system decisions (colors, tokens, typography, spacing); working with React/Tailwind/shadcn/ui; vibecoding in Lovable; writing Lovable prompts for UI screens. ALWAYS trigger for: "design the flow", "map the user journey", "what screens do I need", "how does the user get from X to Y", "review my UI", "improve UX", "make this look better", "this feels off", "what's wrong with this design", "add dark mode". Also trigger for: wireframe → code, component design, design system audit, accessibility review. Every UI decision has product impact — trigger broadly.
---

# Product Designer Skill

Full-spectrum product design: from strategic design decisions to pixel-perfect, production-grade UI code. Covers discovery, information architecture, visual design system, component implementation, and quality review.

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
| "This looks off" feedback | **Diagnosis** | Section 4 |
| Choosing style / color / font | **Design System** | Section 2 |

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

#### Screen Inventory for Common Pradio Flows

| Flow | Minimum Screens |
|------|----------------|
| Onboarding | Landing → Register → Email confirm → Profile setup → First bien |
| Ajouter un bien | Form multi-step: Adresse → Caractéristiques → Acquisition → Simulations |
| Simulation fiscale | Bien selection → Paramètres → Résultats → Export/Save |
| Dashboard principal | Vue globale → Détail bien → Simulation → Actions |

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

### 2.1 — Pradio Design System — DS V3.1

Pradio uses a **strict design system** (V3.1) optimized for fintech/proptech clarity and trust. All UI must comply with DS V3.1 checklist.

**Reference:** `wiki/design/DESIGN-SYSTEM-V3.1.md`

Key constraints:
- **Max 5 semantic colors** (primary, success, destructive, warning, foreground) + greys
- **No tinted backgrounds** — use `bg-card` or `bg-background` only
- **Tabular numbers** for financial data (right-aligned, monospace)
- **Lucide icons only** — 4-5px sizes, stroke 1.75, zero emojis
- **Typography scale** — 12/14/16/18/20/24/32/40/48px only
- **Spacing grid** — 4px multiples (Tailwind scale)

### 2.2 — Color System (Semantic Tokens)

Use Tailwind CSS variables mapped to semantic meaning:

| Token | Purpose | Tailwind |
|-------|---------|----------|
| `primary` | Action CTAs, accents | `btn-primary`, `border-primary` |
| `success` | Positive confirmations, gains | Green tones |
| `destructive` | Warnings, deletes, errors | Red tones |
| `warning` | Alerts, cautions | Orange/yellow tones |
| `foreground` | Text, icons | High contrast |
| `bg-background` | Page background | Off-white |
| `bg-card` | Component/card surfaces | White |
| `border-border` | Dividers, edges | Subtle gray |

**Rules:**
- Never use raw hex in components — always semantic tokens
- Minimum 4.5:1 WCAG AA contrast for body text
- Callouts/banners: `border-l-[3px]` (accent color) only — never full bg
- No gradients, no tinted backgrounds (`bg-primary/10`, `bg-blue-50`, forbidden)

### 2.3 — Typography System

```
Scale:        12 / 14 / 16 / 18 / 20 / 24 / 32 / 40 / 48
Body:         16px minimum, line-height 1.5–1.75
Line length:  60–72 chars for prose
Financial:    Font-mono, tabular-nums, right-aligned
Headings:     Cal Sans or DM Sans; 600–700 weight
```

### 2.4 — Spacing & Grid

4px base grid:

| Token | Value | Use |
|-------|-------|-----|
| `gap-1` | 4px | Icon padding |
| `gap-2` | 8px | Tight spacing |
| `gap-3` | 12px | Element gaps |
| `gap-4` | 16px | Component padding |
| `gap-6` | 24px | Section spacing |

**Touch targets:** min 44×44px (iOS) / 48×48px (Android)

---

## 3. Component Implementation

### 3.1 — shadcn/ui (Primary Layer)

Always prefer shadcn primitives. Never reinvent.

```tsx
// ✅ Correct
import { Button } from "@/components/ui/button"

<Button variant="default" className="gap-2">
  <Plus className="h-4 w-4" strokeWidth={1.75} />
  Ajouter un bien
</Button>

// ❌ Wrong: custom button when shadcn exists
<button className="bg-blue-600 text-white px-4 py-2 rounded">
```

### 3.2 — Component API

All components must have:
- `variant` prop (default, destructive, ghost, outline)
- `size` prop (sm, md, lg)
- `isLoading` state (disable + spinner)
- `disabled` state
- Forwarded `ref` for form integration
- TypeScript props interface

### 3.3 — Tailwind Patterns (DS V3.1 Compliant)

```tsx
// Colors: semantic tokens only
className="bg-card border border-border hover:bg-background"

// Callouts: special accent left-border rule
className="bg-card border border-border border-l-[3px] border-l-success"

// Financial numbers: tabular, right-aligned
className="font-mono tabular-nums text-right"

// Icons: Lucide, strict sizing
<Plus className="h-4 w-4" strokeWidth={1.75} />

// Spacing: 4px grid
className="gap-4 p-6 mb-6"

// No emojis, gradients, tinted backgrounds
```

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

### 4.0 — Quick Audit

1. What's the ONE thing the user does here? Obvious in <3 seconds?
2. What dominates visually? Should it?
3. What would a first-timer misunderstand?
4. What's the friction point?

### 4.1 — Full Critique: DS V3.1 Checklist

#### 🔴 Critical (block delivery)

- [ ] **DS V3.1 compliance** — see `wiki/design/DESIGN-SYSTEM-V3.1.md`
  - Max 5 colors + greys only
  - No tinted backgrounds (`bg-primary/10` forbidden)
  - Tabular numbers on financial data
  - Lucide icons 4–5px, stroke 1.75
  - Zero emojis, gradients, decorative animations
  
- [ ] **Contrast** — 4.5:1 minimum for body text (WCAG AA)
- [ ] **Touch targets** — 44×44px minimum on mobile
- [ ] **No horizontal scroll** — ever, on any breakpoint
- [ ] **Loading/error states** — all defined
- [ ] **Primary action** — one clear CTA per screen

#### 🟠 High Priority (fix before launch)

- [ ] **Spacing** — 4px grid only; no arbitrary pixels
- [ ] **Colors** — all semantic tokens; no raw hex
- [ ] **Typography** — scale 12/14/16/18/20/24/32/40/48 only
- [ ] **Icons** — Lucide only; consistent stroke width
- [ ] **All states defined** — empty, loading, error, success
- [ ] **Navigation consistent** — same placement, all screens
- [ ] **No dead ends** — every empty state has next action

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
Design system: Pradio DS V3.1 — see DESIGN-SYSTEM-V3.1.md
Variant: [style choice]
Data: [props shape]
States: [all states needed]
DS V3.1 constraints:
  - Max 5 colors + greys
  - No tinted backgrounds
  - Tabular numbers for financial data
  - Lucide icons only (4–5px, stroke 1.75)
  - No emojis, gradients, animations
Do NOT: use emoji icons, inline styles, custom components when shadcn exists
```

### Common Lovable Pitfalls

- Uses `useState` instead of React Query — **specify data fetching approach**
- Inline styles instead of Tailwind — **"Tailwind only, no inline styles"**
- Custom components over shadcn — **"use shadcn/ui primitives"**
- Missing states — **"include loading, error, empty, success states"**
- Emoji icons — **"use Lucide icons only"**
- Tinted backgrounds — **"never use `bg-primary/10` or colored backgrounds"**

---

## 6. Accessibility Baseline

Non-negotiable:

```tsx
// Images
<img alt="Description" src={...} />

// Icon buttons
<Button aria-label="Supprimer">
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

**Design System:**
- `wiki/design/DESIGN-SYSTEM-V3.1.md` — Complete V3.1 spec (mandatory checklist)
- `wiki/design/design-system-v3.html` — Visual reference

**Product:**
- `wiki/product/PRD-PRODUCTION.md` — Pradio v3.0 product requirements
- `wiki/product/SPEC-FONCTIONNELLE.md` — Feature specs

**UX Rules:**
- `.claude/skills/product-designer/references/ux-rules-pradio.md` — 99 rules adapted to Pradio + DS V3.1
- `wiki/operations/TROUBLESHOOTING.md` — Common UI issues & diagnosis
