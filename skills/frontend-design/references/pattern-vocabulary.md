# Pattern Vocabulary

A naming reference, not a rulebook — read this when you want a menu of options for a section
type, not as a checklist to satisfy. Knowing these names helps articulate a design read and
reach for a pattern deliberately instead of defaulting to the first thing that comes to mind.

### Hero Paradigms

Note: `marketing-layout.md`'s hard rules always win over a paradigm name here — e.g. "no asset"
below is a description of the visual style (type carries the whole composition), not
permission to skip the "hero needs a real visual" rule. In practice this usually means a
full-bleed background texture, video, or large-scale imagery behind the type, not a bare
gradient.

* **Asymmetric Split Hero** — text on one side, asset on the other, generous white space.
* **Editorial Manifesto Hero** — large type carries the composition, minimal or background-only
  asset, almost a poster.
* **Video / Media Mask Hero** — type cut out as a mask over a video background.
* **Kinetic-Type Hero** — animated typography as the primary visual.
* **Curtain-Reveal Hero** — hero parts on scroll like a curtain.
* **Scroll-Pinned Hero** — hero stays pinned while content scrolls behind it.

### Navigation & Menus
* **Dock Magnification** — edge nav, icons scale fluidly on hover.
* **Magnetic Button** — pulls toward the cursor.
* **Gooey Menu** — sub-items detach like viscous liquid.
* **Dynamic Island** — morphing pill for status/alerts.
* **Contextual Radial Menu** — circular menu expanding at the click point.
* **Floating Speed Dial** — FAB springing into curved secondary actions.
* **Mega Menu Reveal** — full-screen dropdown, stagger-fade content.

### Layout & Grids
* **Bento Grid** — asymmetric tile grouping (see `marketing-layout.md` for the cell-count rule).
* **Masonry Layout** — staggered grid, no fixed row height.
* **Chroma Grid** — borders/tiles with subtle animating gradients.
* **Split-Screen Scroll** — two halves sliding in opposite directions.
* **Sticky-Stack Sections** — sections that pin and stack on scroll (code in
  `animation-code.md`).

### Cards & Containers
* **Parallax Tilt Card** — 3D tilt tracking mouse coordinates.
* **Spotlight Border Card** — border illuminates under the cursor.
* **Glassmorphism Panel** — frosted glass with inner refraction.
* **Holographic Foil Card** — iridescent rainbow shift on hover.
* **Tinder Swipe Stack** — physical card stack, swipe-away.
* **Morphing Modal** — button expands into its own dialog.

### Scroll Animations
* **Sticky Scroll Stack** — cards stick and physically stack.
* **Horizontal Scroll Hijack** — vertical scroll drives horizontal pan.
* **Locomotive / Sequence Scroll** — video or 3D sequence tied to the scrollbar.
* **Zoom Parallax** — central background image zooms on scroll.
* **Scroll Progress Path** — SVG line drawing along scroll.
* **Liquid Swipe Transition** — page transition like viscous liquid.

### Galleries & Media
* **Dome Gallery** — 3D panoramic gallery.
* **Coverflow Carousel** — 3D carousel with angled edges.
* **Drag-to-Pan Grid** — boundless draggable canvas.
* **Accordion Image Slider** — narrow strips expand on hover.
* **Hover Image Trail** — mouse leaves a popping image trail.
* **Glitch Effect Image** — RGB-channel shift on hover.

### Typography & Text
* **Kinetic Marquee** — endless text bands reversing on scroll (max one per page, see
  `marketing-layout.md`).
* **Text Mask Reveal** — massive type as a transparent window onto video.
* **Text Scramble Effect** — matrix-style decoding on load/hover.
* **Circular Text Path** — text curving along a spinning circle.
* **Gradient Stroke Animation** — outlined text with a running gradient.
* **Kinetic Typography Grid** — letters dodging the cursor.

### Micro-Interactions & Effects
* **Particle Explosion Button** — CTA shatters into particles on success.
* **Liquid Pull-to-Refresh** — reload indicator like detaching droplets.
* **Skeleton Shimmer** — shifting light reflection across placeholders.
* **Directional Hover-Aware Button** — fill enters from the cursor's exact side.
* **Ripple Click Effect** — wave from the click coordinates.
* **Animated SVG Line Drawing** — vectors drawing themselves in real time.
* **Mesh Gradient Background** — organic lava-lamp blobs.
* **Lens Blur Depth** — background UI blurred to focus the foreground action.

### Animation Library Choice
* **Motion (`motion/react`)** — default for UI, bento, and state-change motion.
* **GSAP + ScrollTrigger** — for full-page scrolltelling and scroll hijacks. Isolate in
  dedicated leaf components with `useEffect` cleanup.
* **Three.js / WebGL** — for canvas backgrounds and 3D scenes. Same isolation rule.
* Never mix GSAP/Three.js with Motion in the same component tree — they fight over frames.
