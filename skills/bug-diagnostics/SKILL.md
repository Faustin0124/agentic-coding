---
name: bug-diagnostics
description: >
  Expert bug diagnosis and resolution workflow for any codebase. Use this skill for any bug
  report, error, or unexpected behavior — a raw stack trace, a console error message, or a
  plain-language description ("it crashes when I click X", "the page won't load", "the
  calculation gives the wrong result"). Trigger whenever the user mentions a bug, an error, a
  crash, abnormal behavior, a regression, or pastes any kind of error trace. Also trigger on:
  "I have a problem with", "it stopped working", "it's broken", "I'm getting an exception",
  "TypeError", "Cannot read properties", "404", "500", "undefined is not a function", "build
  failed", "a test is failing". Produces a structured 5-phase diagnosis: triage → root cause →
  propagation → resolution plan → ticket/decision.
---

# Bug Diagnostics

A 5-phase diagnosis workflow. Run them in order, don't skip a phase — each one feeds the next,
and skipping straight to a fix is exactly how a bug comes back with a sibling three files over.

---

## Phase 1 — Triage & Severity

### 1.1 Capture the minimal context

If the user hasn't already provided these, ask for them **all at once** (not one question at a
time):

- The exact error (stack trace, console message, screenshot)
- The reproduction scenario: "What were you doing when it happened?"
- Frequency: consistent / intermittent / one-off
- Environment: local dev / staging / production
- Regression: did it work before? Since when?

### 1.2 Classify severity

Apply this matrix as soon as there's enough information. Adapt the concrete examples to the
project — the categories transfer, the specific business-logic examples won't:

| Level | Label | Criteria |
|-------|-------|----------|
| 🔴 P0 | **Blocking** | Production down, data loss, core business calculation returns a wrong result shown to the user, authentication broken, a critical backend endpoint is down |
| 🟠 P1 | **Critical** | A main feature is unusable, user-visible error, regression on a key business flow, crash on a core user journey |
| 🟡 P2 | **Major** | Feature degraded but has a workaround, error in logs with no visible impact, broken rendering on a secondary screen |
| 🟢 P3 | **Minor** | Cosmetic, typo, unlikely edge case, UX polish |

**Show the severity level and its justification immediately** before moving on.

---

## Phase 2 — Root Cause Analysis

### 2.1 Read and interpret the error

- Identify the error type: runtime / compile / network / database / business logic / framework
  state / type error
- Trace the execution path from user input to the crash point
- Identify the file and line implicated, if the stack trace gives one

### 2.2 Explore the code

Use the available bash/grep/read tools to trace it down:

```bash
# Locate the file or function involved
grep -rn "functionName\|ComponentName" src/ -l

# Read the implicated file
cat src/path/to/file.ts

# Trace imports and usages
grep -rn "import.*ModuleName\|from.*path" src/
```

Adjust file extensions and the root directory (`src/`, `app/`, `lib/`, etc.) to match the
project's actual layout.

### 2.3 State the root cause

Write a clear explanation in 2-4 sentences:
- **What happened**: the precise mechanism of the failure
- **Why**: the condition or state that triggered it
- **When**: the exact context (which data, which flow, which race condition...)

---

## Phase 3 — Propagation Analysis

### 3.1 Identify the potential blast radius

Actively search the repo for other places the same failing pattern might exist:

```bash
# Search for other usages of the same pattern
grep -rn "theProblematicPattern" src/

# Search for structurally similar files
find src/ -name "*SimilarName*" -type f
```

Adapt these to the language/stack — e.g. check the schema/types file if the bug is data-shaped,
or list backend function/handler directories if it's a backend bug.

### 3.2 List affected zones

For each zone found, state:
- 📍 **File / component**
- ⚠️ **Nature of the risk**: same bug / similar bug / indirect risk
- 🎯 **Probability**: high / medium / low

```
| File | Risk nature | Probability | Notes |
|------|-------------|-------------|-------|
| src/... | Same pattern | High | ... |
```

If no propagation is found, say so explicitly: "Bug isolated to file X, no propagation
identified." Don't imply you searched more broadly than you did.

---

## Phase 4 — Resolution Plan

### 4.1 Propose the fix

- Describe the precise correction to make (with code if useful)
- If multiple approaches exist, present the trade-offs
- Flag when high-risk files are involved and confirmation is needed before touching them. What
  counts as high-risk is project-specific — common categories worth checking for: core
  financial/legal calculation logic, auth code, payment webhooks, database migrations. If the
  project has a CLAUDE.md or similar convention doc naming these files, defer to it; otherwise
  ask the user once rather than guessing.

### 4.2 Estimate the effort

| Dimension | Estimate |
|-----------|----------|
| ⏱️ Time | X minutes / X hours |
| 🔧 Complexity | Low / Medium / High |
| 🧪 Tests needed | Yes/No — which ones |
| 🔄 Impact on other features | Yes/No — which ones |
| 🚀 Deployable alone | Yes/No (dependencies) |

### 4.3 Recommended order

If multiple zones are affected, prioritize by severity and propose an order:

```
1. [URGENT] Fix src/X.ts — direct cause of the crash
2. [IMPORTANT] Check src/Y.ts — same pattern, high risk
3. [OPTIONAL] Refactor src/Z.ts — preventive improvement
```

---

## Phase 5 — Ticket & Decision

### 5.1 Generate the ticket

Format the diagnosis as a ticket using the template in `references/ticket-template.md` — it's
tool-agnostic (renders as chat text first, tracker mapping is a separate step).

### 5.2 Offer the choice

**Always ask this after generating the ticket:**

```
📋 Diagnosis complete. What do you want to do?

A) 🚀 Fix it now — I start the correction directly
B) 📤 File it — I create a ticket/issue and stop there
C) 📤 + 🚀 Both — file it AND start the fix
```

### 5.3 Filing the ticket (if B or C chosen)

Where the ticket goes depends on what's actually available in the project — don't assume a
specific tracker. Check, in order:
1. Is a Notion MCP connected? → see `references/ticket-template.md`'s tracker-mapping section
   for the generic Notion workflow (find the database, read its real schema, don't assume
   property names).
2. Is this a GitHub repo with issue tooling available (`gh`, a GitHub MCP)? → file it as a
   GitHub issue with the same content.
3. Neither available, or the user doesn't specify? → save the formatted ticket as a local
   markdown file (e.g. `BUG-<short-slug>.md`) and tell the user where it is.

Confirm after filing:
```
✅ Ticket filed: [link or file path]
```

---

## General Rules

- **Never modify** high-risk files (Section 4.1), database migrations, or do an architectural
  refactor without explicit user confirmation.
- **Always show severity** from Phase 1 before continuing.
- **Be factual about propagation**: if you don't have access to the full codebase, say so
  clearly rather than implying a complete search.
- **Always offer** the fix/file choice in Phase 5 — never skip straight to fixing without asking,
  even if the fix seems obvious.
- If the bug is P0 🔴, flag it immediately and offer to treat it as urgent before even finishing
  the full analysis.
