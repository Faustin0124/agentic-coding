---
name: tech-debt-manager
description: >
  Expert technical debt management for any codebase. Use this skill for anything related to
  technical debt: full codebase audits, code smell detection, outdated or vulnerable
  dependencies, architectural issues, missing tests, security debt, and generating an
  executable action backlog for the agent to work through. Trigger whenever the user mentions
  "technical debt", "refactoring", "code audit", "code smell", "outdated dependencies",
  "security", "performance", "test coverage", "cleanup", "improve the architecture", "dead
  code", "duplication", or asks for a state-of-the-codebase assessment. Also trigger on
  implicit phrasing: "the code has gotten heavy", "we've accumulated some ugly stuff", "we
  need to clean this up", "this is legacy", "this is going in every direction".
---

# Tech Debt Manager

An **action-oriented** skill. The goal isn't to produce a report — it's to produce an
**executable backlog** that the agent then works through directly in the repo.

---

## Phase 0 — Detect the Stack

Before running any audit command, work out what's actually in the repo — the commands below
are illustrative for a JS/TS project because that's the most common case, but every command
needs adapting to what's really there:

- **Package manager / language**: `package.json` → npm/pnpm/yarn; `pyproject.toml`/`requirements.txt`
  → pip/poetry/uv; `Cargo.toml` → cargo; `go.mod` → go modules.
- **Framework**: read `package.json` dependencies (React/Vue/Next/etc.) or the equivalent
  manifest for other languages.
- **Test runner**: look for `vitest.config`, `jest.config`, `pytest.ini`, etc.
- **Backend/data layer**: does the project talk to a database directly, through an ORM, or
  through a backend-as-a-service (Supabase, Firebase)? This changes what Phase 1.5 looks like —
  see `references/debt-patterns.md`.

State the detected stack in one line before starting the audit, so the rest of the run is
legible: *"Detected: React + TypeScript + Vite, npm, Vitest, Supabase backend."*

---

## Phase 1 — Repo Audit

Before proposing anything, **read the repo** to build an accurate picture of its current state.

### 1.1 Dependency audit

For a JS/TS project:
```bash
npm outdated --json
npm audit --json
npx depcheck --json   # unused dependencies
```
For other ecosystems, use the equivalent: `pip list --outdated` + `pip-audit` (Python),
`cargo outdated` + `cargo audit` (Rust), `go list -u -m all` (Go).

### 1.2 Static analysis

For TypeScript:
```bash
npx tsc --noEmit --strict 2>&1 | head -100
grep -rn ": any" src/ --include="*.ts" --include="*.tsx" -l
grep -rn "TODO\|FIXME\|HACK\|XXX\|@ts-ignore\|@ts-expect-error" src/
```
For other typed/linted languages, run the project's own type checker/linter in strict mode and
grep for the equivalent suppression comments (`# type: ignore`, `#[allow(...)]`, etc.).

### 1.3 Code smell detection

These greps are language-agnostic in spirit — adjust the file extensions and root directory:

```bash
# Files that are too long (candidates for decomposition)
find src/ -name "*.tsx" -o -name "*.ts" | xargs wc -l | sort -rn | head -20

# Components/functions with too many parameters (proxy: lines in a Props/params interface)
grep -r "interface.*Props" src/ -A 30 --include="*.tsx" | grep -c "  [a-z]"

# Duplication: the same import repeated across many files (candidate for a shared hook/util)
grep -r "^import" src/ --include="*.tsx" | sed 's/.*from //' | sort | uniq -c | sort -rn | head -20
```

### 1.4 Test coverage

```bash
npx vitest run --coverage 2>&1 | tail -30   # substitute the project's actual test runner
```
Cross-reference pure-logic files (a `lib/`, `utils/`, or `domain/` directory) against test files
to flag anything untested — that's usually the highest-value gap to close first, since pure
logic is the cheapest thing to test and often the most consequential to get wrong.

### 1.5 Backend / infrastructure audit (conditional)

Only run this if Phase 0 detected a matching backend. See `references/debt-patterns.md` for the
Supabase-specific version (RLS coverage, migration hygiene, edge function error handling,
generated-types drift) — the same categories apply to any backend-as-a-service or direct-DB
setup, just with different concrete commands.

### 1.6 Security audit

```bash
# Secrets/keys committed to source
grep -rn "sk_live\|sk_test\|service_role\|password.*=.*['\"]" src/ 2>/dev/null | grep -v ".env"

# Untyped/unvalidated environment variable access
grep -rn "process\.env\.\|import\.meta\.env\." src/ | head -20
```
Extend the secret-pattern grep with whatever third-party services the project actually
integrates (payment providers, cloud SDKs) rather than assuming a fixed list.

---

## Phase 2 — Scoring and Prioritization

For each item detected, apply this scoring grid:

| Criterion | Low (1) | Medium (2) | High (3) |
|---|---|---|---|
| **Security impact** | Cosmetic | Data exposure | Exploitable flaw |
| **User impact** | Invisible | Degraded UX | Error/crash |
| **Fix effort** | < 30 min | 30 min – 2h | > 2h |
| **Propagation** | 1 file | Module | Cross-domain |
| **Occurrence frequency** | Isolated | A few occurrences | Systemic pattern |

**Priority = (Security impact × 2) + User impact + (4 - Effort) + Propagation + Frequency**

Tiers:
- **P0** (score ≥ 14): Blocking — address immediately
- **P1** (score 10–13): High priority — current sprint
- **P2** (score 6–9): Normal — planned backlog
- **P3** (score < 6): Nice-to-have — opportunistic

---

## Phase 3 — Backlog Generation

Produce a `TECH_DEBT_BACKLOG.md` file at the repo root.

### Item structure

```markdown
## [TD-XXX] Short, actionable title

**Priority**: P0 / P1 / P2 / P3
**Category**: Security | Types | Tests | Architecture | Dependencies | Performance | Backend
**Estimated effort**: XS (< 30min) / S (30min–2h) / M (2h–4h) / L (4h–8h) / XL (> 8h)
**Files involved**: `src/...`

### Problem
Factual description of what was detected. Include metrics (file count, line count, occurrences).

### Impact
What happens if this isn't fixed (security risk, accumulating debt, potential bug).

### Fix actions

- [ ] Step 1 — precise description (file, function, transformation)
- [ ] Step 2 — ...

### Acceptance criteria
How to verify it's done (a passing test, a command returning 0, an improved metric).

---
```

### Backlog header

```markdown
# Tech Debt Backlog

> Generated: {DATE}
> Commit analyzed: {GIT_HASH}
> Overall debt score: {X}/100 (100 = no detected debt)

## Executive summary

| Category | P0 | P1 | P2 | P3 | Total |
|---|---|---|---|---|---|
| Security | | | | | |
| Types | | | | | |
| Tests | | | | | |
| Architecture | | | | | |
| Dependencies | | | | | |
| Backend | | | | | |
| **Total** | | | | | |

## P0 Items — Address immediately
...

## P1 Items — Current sprint
...

## P2 Items — Planned backlog
...

## P3 Items — Nice-to-have
...
```

---

## Phase 4 — Agent Execution

After the user approves the backlog, work through items **in this strict order**:

1. **P0 Security** — never auto-execute, always explicit confirmation first
2. **P0 other** — execute directly if non-destructive (adding types, removing `any`, etc.)
3. **P1** — execute directly for XS/S fixes
4. **P2/P3** — execute only if the user explicitly asks

### Execution rules

**Execute directly, no need to ask:**
- Patch/minor dependency updates that aren't breaking
- Removing a type-suppression comment and replacing it with the correct type
- Extracting a constant/function into a shared module
- Adding a unit test for a pure function
- Adding input validation to an endpoint/handler that's missing it

**Always confirm before:**
- Major dependency updates (framework, build tool, major state-management libs)
- A refactor that touches multiple functional domains
- Any change to database migrations (irreversible)
- Folder structure changes
- Changes to files the project flags as high-risk business logic (financial/legal calculations,
  auth, payments) — check CLAUDE.md or ask the user once which files fall in this category if
  it isn't already documented

**Never touch without explicit human review:**
- Core business-critical calculation files, once identified
- Database migrations
- Payment webhooks / payment-provider integration code

---

## Reference: Common Debt Patterns

`references/debt-patterns.md` covers stack-specific patterns worth checking for beyond the
generic greps above — currently written for a React/TypeScript + Supabase-style backend stack,
since that's the best-understood example. Extend it with additional sections the same way if
the project uses a different stack; the categories (typing debt, data-fetching debt,
backend/RLS debt, test-coverage priorities, build/perf debt, CI debt) generalize even where the
exact commands don't.

---

## Output

At the end of each run, produce:

1. **`TECH_DEBT_BACKLOG.md`** — full backlog with all items scored
2. **A prose summary** in chat (max 15 lines): overall score, item count per priority, the top
   3 P0 items if any, a recommendation on what to tackle first
3. **If fixes were applied**: a list of modified files with a one-line description each
