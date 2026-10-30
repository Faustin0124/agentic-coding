---
name: product-notes
description: >
  Turns a raw note, an offhand remark, a user observation, or an idea dropped mid-conversation
  into a well-structured Epic or User Story in the project's Notion backlog. Trigger whenever
  the user gives an unstructured product note — even short, even informal ("we should...",
  "one thing to add", "note for later", "idea: ...", a user-test comment, an observed bug, an
  offhand product observation — and they haven't explicitly said it's just a discussion. Also
  trigger when they explicitly say "put that in the backlog" or "create a story/epic for that".
  Do NOT trigger for purely technical code questions or design-review requests — other skills
  cover those.
---

# Product Notes — Backlog Capture

Product notes tend to arrive in bulk — one sentence, one paragraph, sometimes several ideas
mixed into a single message. This skill converts them into clean entries in the project's
Notion backlog database, attached to the right Epic.

The value isn't "filling a database" — it's making sure ideas don't get lost in the
conversation, and giving them immediately the shape a backlog needs to be actionable: a clear
title, a type, a parent Epic, a sane starting state.

**This skill doesn't hardcode a database ID or a fixed set of Epics** — every project's backlog
is different, so the first real step is always finding and reading the actual target database
rather than assuming its shape.

## Finding the target database

Don't assume which Notion database is "the" backlog — confirm it, once, then reuse that
knowledge for the rest of the session:

1. If the user has already named a database (or it's obvious from prior context in this
   conversation), use it.
2. Otherwise, use `notion-search` with a query like "backlog", "product backlog", or "roadmap"
   to find candidates. If there are multiple plausible matches, list them and ask the user to
   pick — don't guess.
3. Once identified, `notion-fetch` the database to read its **actual current schema** — property
   names, types, and the select/status options that exist. Don't reuse a schema remembered from
   a previous session; it may have changed, and a slightly different string value on a select
   property creates a stray new option instead of matching the existing one.

## Reading the schema, not assuming it

Every backlog database will have its own property names and vocabulary. Typical shapes look
something like this, but **read the real one before creating anything**:

| Common property | Typical type | Notes |
|---|---|---|
| Title | title | The item's name |
| Type | select | Often `Epic` / `User Story` / `Task` / `Bug` |
| Parent Epic | select or relation | How a Story attaches to its Epic — check which mechanism this database actually uses |
| Status | status | Discovery/planning stage through done |
| Priority | select | If present |
| Sprint / iteration | select | If the project plans in sprints |

A raw note becomes, by default:
- `Type` = `User Story` (use `Bug` if the note clearly describes a malfunction, `Task` for a
  technical action with no direct user value, never `Epic` except the case below)
- `Status` = whatever the database's earliest/discovery-stage option is — never jump straight to
  an active-sprint status without being asked
- Priority and sprint/estimate fields: leave empty unless the note gives a clear signal (urgency
  expressed → high priority; an estimate given → fill it in)

## Attaching to an Epic (or equivalent parent category)

"Which part of the product does this belong to" is answered by matching the note's subject to
an existing Epic (or whatever the project calls its top-level grouping), not by inventing a new
one reflexively.

1. **Look for an existing match first.** Read the note and compare its actual subject to the
   list of current Epics fetched from the database — match on functional topic, not surface
   keyword overlap. A note about a specific sub-feature belongs in the Epic that actually owns
   that sub-feature, not in whichever Epic happens to share a word with it.
2. **If one clearly matches**, create the Story with that Epic set — copy the name character for
   character from the fetched list. A typo on a select property creates a new option instead of
   reusing the existing one, silently forking the taxonomy.
3. **If nothing clearly matches**, don't create a new Epic silently — propose a name to the user
   and ask for confirmation first. Creating an Epic is a backlog-structuring decision, not a
   simple row insert; a bad one pollutes the selection list for every future note. If confirmed,
   create the Epic page first, then the Story pointing to it.
4. **If the note contains several distinct ideas** (common in a bulk message), split it into
   separate Stories, each with its own attachment — don't create one catch-all Story mixing two
   subjects; it becomes unreadable six months later.
5. **If the note is Epic-sized itself** (a genuinely new feature area, not a small improvement)
   rather than Story-sized, say so and propose creating it as an `Epic` instead of a `User
   Story`.

## Writing the Story

A title alone doesn't make a note actionable later. Write real page content, not just the
title:

- A sentence of context if the raw note had one (where the need came from — user feedback, an
  observation, a personal idea)
- The need reformulated clearly, in "As a [role], I want [action] so that [benefit]" format when
  that's natural — don't force the format onto a note too vague to support it; a plain
  description is fine there
- Acceptance criteria as bullet points, **only** if the note gives enough detail to derive them
  without inventing — a short, honest Story beats one padded with assumptions the user never
  stated

The title itself should be short and descriptive (5-10 words), not the raw note copy-pasted.

## Workflow

1. Fetch the current Epic/category list from the target database (`notion-fetch`).
2. For each distinct idea in the note, determine its type and parent attachment per the process
   above.
3. If there's ambiguity on attachment, or a new Epic needs creating, ask the user for
   confirmation before creating anything — one grouped question if several ideas are involved,
   not a back-and-forth per idea.
4. Create the pages via `notion-create-pages`, with `parent` set to the target data source found
   in step 1 of "Finding the target database" above.
5. Confirm what was created — title, type, parent Epic, Notion link — as a short list, not a
   paragraph.
6. If a created Story is clearly small (one user flow, a few days of work, known problem), offer
   in one line to prepare it for dev with `quick-evol`; for anything bigger, mention
   `product-flow`. Don't start either without the user saying yes.

## What this skill does not do

- It doesn't reorganize the existing backlog, and doesn't change the status or priority of
  already-created Stories, except on explicit request.
- It doesn't decide sprint/iteration assignment — that stays a planning decision the user makes
  themselves.
- It never deletes or merges existing Stories, even on an apparent duplicate — it flags the
  potential duplicate and lets the user decide.
