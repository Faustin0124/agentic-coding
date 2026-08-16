# Animation & Dial Technical Reference

Canonical code skeletons and dial definitions. Load this when implementing scroll-driven or
physics-based motion — the scroll-hijack patterns in particular are easy to get subtly wrong
(pinning at the wrong offset, missing cleanup, jank on mobile).

---

## Dial Definitions

### `DESIGN_VARIANCE` (1–10)
* **1–3 (Predictable):** symmetrical CSS Grid (12-col, equal fr-units), equal padding, centered
  alignment.
* **4–7 (Offset):** `margin-top: -2rem` overlaps, varied image aspect ratios (4:3 next to
  16:9), left-aligned headers over center-aligned data.
* **8–10 (Asymmetric):** masonry layouts, fractional grid columns (`2fr 1fr 1fr`), large empty
  zones (`padding-left: 20vw`).
* **Mobile override:** for levels 4–10, asymmetric layouts above `md:` must collapse to a
  strict single column (`w-full`, `px-4`, `py-8`) below 768px.

### `MOTION_INTENSITY` (1–10)
* **1–3 (Static):** no automatic animations, `:hover`/`:active` CSS states only.
* **4–7 (Fluid CSS):** `transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1)`, `animation-delay`
  cascades for load-ins, restricted to `transform`/`opacity`.
* **8–10 (Advanced choreography):** scroll-triggered reveals, parallax, scroll-driven CSS
  (`animation-timeline`) or GSAP ScrollTrigger. Use Motion hooks —
  `window.addEventListener('scroll')` is a hard ban here, not a preference (see Forbidden
  Patterns below).

### `VISUAL_DENSITY` (1–10)
* **1–3 (Art gallery):** generous white space, `py-32` to `py-48` section gaps.
* **4–7 (Daily app):** standard web-app spacing, `py-16` to `py-24`.
* **8–10 (Cockpit):** tight padding, no card boxes, 1px lines separating data,
  `font-mono` mandatory for numbers.

---

## Forbidden Animation Patterns

* `window.addEventListener("scroll", ...)` — runs on every scroll frame, jank-prone, no
  batching. Use `useScroll()` (Motion), GSAP `ScrollTrigger`, `IntersectionObserver`, or CSS
  scroll-driven animations (`animation-timeline: view()`).
* Custom scroll-progress calculations using `window.scrollY` in React state — same problem,
  re-renders on every frame.
* `requestAnimationFrame` loops that touch React state — use `useMotionValue`/`useTransform`
  instead.
* For visible state changes (list reordering, expanding modals, shared elements between
  routes), use Motion's `layout`/`layoutId` props — but don't wrap static content in `layout`
  "for safety," it costs measurement work for nothing.
* For staggered reveals where sequence matters, use `staggerChildren` (Motion) or CSS cascade
  (`animation-delay: calc(var(--index) * 100ms)`). `staggerChildren` requires parent
  (`variants`) and children to share the same Client Component tree.

## Never Track Continuous Values in `useState`

Never use `useState` for continuous values driven by user input — mouse position, scroll
progress, pointer physics, magnetic hover. Use Motion's `useMotionValue`/`useTransform`/
`useScroll` instead. `useState` re-renders the React tree on every change and visibly
collapses on mobile.

---

## Sticky-Stack — Canonical Skeleton

```tsx
"use client";
import { useRef, useEffect } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useReducedMotion } from "motion/react";

gsap.registerPlugin(ScrollTrigger);

export function StickyStack({ cards }: { cards: React.ReactNode[] }) {
  const ref = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();

  useEffect(() => {
    if (reduce || !ref.current) return;
    const ctx = gsap.context(() => {
      const cardEls = gsap.utils.toArray<HTMLElement>(".stack-card");
      cardEls.forEach((card, i) => {
        if (i === cardEls.length - 1) return;
        ScrollTrigger.create({
          trigger: card,
          start: "top top",                              // pin at viewport top
          endTrigger: cardEls[cardEls.length - 1],
          end: "top top",
          pin: true,
          pinSpacing: false,
        });
        gsap.to(card, {
          scale: 0.92,
          opacity: 0.55,
          ease: "none",
          scrollTrigger: {
            trigger: cardEls[i + 1],
            start: "top bottom",
            end: "top top",
            scrub: true,
          },
        });
      });
    }, ref);
    return () => ctx.revert();
  }, [reduce]);

  return (
    <div ref={ref} className="relative">
      {cards.map((card, i) => (
        <div
          key={i}
          className="stack-card sticky top-0 min-h-[100dvh] flex items-center justify-center"
        >
          {card}
        </div>
      ))}
    </div>
  );
}
```

Critical points: `start: "top top"` (not `"top center"` or `"top 80%"` — those fire the pin
halfway through the scroll instead of at the viewport top), every card except the last is
pinned, and the scale/opacity transform on a card is driven by the *next* card's scroll
trigger, so the previous card shrinks as the next one arrives.

## Horizontal-Pan — Canonical Skeleton

```tsx
"use client";
import { useRef, useEffect } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useReducedMotion } from "motion/react";

gsap.registerPlugin(ScrollTrigger);

export function HorizontalPan({ children }: { children: React.ReactNode }) {
  const wrap = useRef<HTMLDivElement>(null);
  const track = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();

  useEffect(() => {
    if (reduce || !wrap.current || !track.current) return;
    const ctx = gsap.context(() => {
      const distance = track.current!.scrollWidth - window.innerWidth;
      gsap.to(track.current, {
        x: -distance,
        ease: "none",
        scrollTrigger: {
          trigger: wrap.current,
          start: "top top",                              // pin starts when section top hits viewport top
          end: () => `+=${distance}`,                    // scroll distance = track width minus viewport
          pin: true,
          scrub: 1,
          invalidateOnRefresh: true,
        },
      });
    }, wrap);
    return () => ctx.revert();
  }, [reduce]);

  return (
    <section ref={wrap} className="relative overflow-hidden">
      <div ref={track} className="flex h-[100dvh] items-center">
        {children}
      </div>
    </section>
  );
}
```

Critical points: `start: "top top"`, `end: "+=${distance}"` (scroll length equals the
horizontal travel needed), `scrub: 1`. The wrapper is pinned, the inner track slides
horizontally as the user scrolls vertically. Common failure mode: the animation starts before
the section is pinned, so the user sees half a slide — the fix is the same `start: "top top"`.

## Scroll-Reveal Stagger — Lighter Alternative (No Pinning)

For simple "items appear as they enter viewport" without pinning, prefer Motion's
`whileInView` over GSAP — lighter, no ScrollTrigger needed:

```tsx
"use client";
import { motion, useReducedMotion } from "motion/react";

export function RevealStagger({ items }: { items: string[] }) {
  const reduce = useReducedMotion();
  return (
    <ul className="grid gap-6">
      {items.map((item, i) => (
        <motion.li
          key={item}
          initial={reduce ? false : { opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.3 }}
          transition={{
            duration: 0.6,
            delay: i * 0.06,
            ease: [0.16, 1, 0.3, 1],
          }}
        >
          {item}
        </motion.li>
      ))}
    </ul>
  );
}
```

Use this for feature lists, testimonial grids, and logo walls — anything that just needs "enter
on scroll." Save GSAP for actual pin/scrub work.

---

## Performance Details

* Apply grain/noise filters exclusively to fixed, `pointer-events-none` pseudo-elements
  (`fixed inset-0 z-[60] pointer-events-none`) — never on scrolling containers, which causes
  continuous GPU repaints and destroys mobile frame rate.
* Watch bundle size: Motion isn't tiny, Three.js is large. Lazy-load anything not
  above-the-fold.
* Never spam arbitrary `z-50`/`z-10` — reserve z-index for systemic layer contexts (sticky
  navbars, modals, overlays, grain) and document the scale in a project constants file.
* Core Web Vitals targets: LCP < 2.5s (hero image `priority`/preloaded), INP < 200ms (heavy
  work off the main thread), CLS < 0.1 (reserve space for images/fonts/embeds). Run Lighthouse
  before declaring a page done.
* Never mix GSAP/Three.js with Motion in the same component tree — they fight over the same
  animation frames. Isolate each in its own Client Component leaf.
