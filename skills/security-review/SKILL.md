---
name: security-review
description: >
  Security review for any codebase and any stack. Use this skill whenever the user adds
  authentication or authorization, handles user input or file uploads, creates a new API
  endpoint or route handler, works with secrets/credentials/tokens, implements payments, stores
  or transmits sensitive data, integrates a third-party API, or is about to deploy to
  production. Also trigger on: "security review", "is this safe", "audit for vulnerabilities",
  "can this be exploited", "pentest", "before we ship this", "handle user input", "secrets",
  "auth", "RLS", "SQL injection", "XSS", "CSRF", "rate limiting".
---

# Security Review

A **checklist-driven** skill: for each category below, check the repo, report PASS/FAIL with
concrete file:line evidence, and propose the minimal fix. Never guess — grep for the actual
pattern before claiming something is or isn't present.

---

## Phase 0 — Detect the Stack

Before checking anything, work out what's actually being reviewed — the examples throughout
this skill are illustrative; adapt the concrete commands to what's really in the repo:

- **Language/runtime**: `package.json`, `pyproject.toml`/`requirements.txt`, `Cargo.toml`,
  `go.mod`, `Gemfile`, etc.
- **Data layer**: raw SQL, an ORM (Prisma, SQLAlchemy, ActiveRecord, GORM), or a
  backend-as-a-service (Supabase, Firebase). If it's Supabase, use the dedicated
  `supabase-security` skill alongside this one for RLS/multi-tenant depth — this skill covers
  the generic layer, that one covers Supabase-specific policy patterns.
- **Auth mechanism**: sessions, JWT, OAuth provider, platform-managed auth.
- **Entry points**: HTTP API, CLI, background jobs/queues, webhooks — each has a different
  trust boundary and untrusted-input surface.

State the detected stack in one line before starting: *"Detected: Node/Express + PostgreSQL
via raw `pg`, JWT auth, no ORM."*

See `references/checklist.md` for ecosystem-specific grep patterns (JS/TS, Python, Go, Ruby,
Rust) for every category below — this file stays language-agnostic in the main flow.

---

## Review Categories

### 1. Secrets management

**Principle**: no credential ever lives in source, only in environment/secret-manager config,
and never reaches logs or client-side bundles.

- Grep for hardcoded-looking values: API keys, connection strings with embedded passwords,
  private key blocks, tokens matching known vendor prefixes (`sk_live_`, `AKIA`, `ghp_`, etc.)
- Confirm `.env*` (except `.env.example`) is gitignored, and check `git log` for a secret ever
  committed and later "removed" — removal from HEAD doesn't remove it from history
- Confirm secrets aren't interpolated into client-bundled code (anything shipped to the
  browser/app, not just the server process)

### 2. Input validation

**Principle**: validate at every trust boundary (HTTP handler, CLI arg, queue consumer,
webhook) with a schema/whitelist — never a blacklist, never "validate on the frontend only."

- Every entry point that accepts external data should validate shape, type, and bounds before
  using the value
- File uploads: size cap, content-type check, extension check, and — where the framework
  allows it — a magic-byte check, not just the client-reported MIME type
- Look for user input flowing straight into a filesystem path, shell command, template string,
  or query without going through validation first

### 3. Injection (SQL, NoSQL, command, template)

**Principle**: never build a query, command, or template by string-concatenating untrusted
input. Parameterize, or use the ORM/query-builder's parameter binding.

- Grep for string interpolation feeding into a query call or `exec`/`system`/`subprocess` call
- Confirm the ORM/driver in use is actually being called with bound parameters, not
  `.raw()`/`.query(fstring)` shortcuts
- Server-side template rendering with user-controlled template strings is its own class of bug
  (SSTI) — check separately from SQL injection if the stack renders templates

### 4. Authentication & authorization

**Principle**: authentication proves identity; authorization is checked again, explicitly, on
every sensitive operation — never assume "logged in" implies "allowed to do this."

- Tokens: not stored in a place readable by injected script (prefer httpOnly cookies over
  storage APIs the app's own JS can read)
- Every state-changing or data-returning handler that should be restricted has an explicit
  authorization check — not just route-level "requires login," but object-level "requires
  ownership/role" (the classic gap: user A can fetch/mutate user B's resource by ID)
- If the stack has row-level security (Postgres RLS, similar), confirm it's actually enabled on
  every table holding user data, not just the ones someone remembered

### 5. XSS / output encoding

**Principle**: untrusted content is data, not markup, until explicitly and narrowly allowed
otherwise.

- Grep for raw HTML injection sinks (`dangerouslySetInnerHTML`, `v-html`, `.innerHTML =`,
  unescaped template output) and confirm anything feeding them is sanitized with an
  allowlist-based sanitizer, not hand-rolled escaping
- Check whether a Content-Security-Policy is set, and whether it still contains
  `unsafe-inline`/`unsafe-eval` — those are compatibility debt, not acceptable defaults

### 6. CSRF / session handling

**Principle**: state-changing requests must be provably intentional, not just authenticated.

- Cookie-based sessions: `SameSite` set (Strict or Lax as appropriate), `Secure`, `HttpOnly`
- Token-based APIs consumed only by first-party JS are naturally CSRF-resistant (no
  ambient credential); confirm that assumption actually holds before skipping CSRF tokens

### 7. Rate limiting & abuse surface

**Principle**: any endpoint that's expensive, security-sensitive (login, password reset,
OTP/token verification), or user-facing-public needs a limit, or it's a free amplification or
brute-force vector.

- Confirm rate limiting exists on auth endpoints specifically, not just globally
- Check for unbounded loops or unbounded fan-out driven by user input (pagination without a
  max page size, batch endpoints without a max batch size)

### 8. Sensitive data exposure (logs & errors)

**Principle**: logs and error responses are a leak surface — treat them like any other output.

- Grep logging calls for password/token/card/PII fields passed directly instead of redacted
- Confirm error responses returned to the client don't include stack traces or internal
  exception messages in production; detailed errors go to server-side logs only

### 9. Dependency security

**Principle**: known-vulnerable dependencies are a supply-chain risk regardless of how good the
first-party code is.

- Run the ecosystem's audit tool (`npm audit`, `pip-audit`, `cargo audit`, `bundler-audit`) and
  report anything above low severity
- Confirm a lockfile is committed and CI installs from it exactly (`npm ci`, not `npm install`)

### 10. Cloud / infra configuration (if applicable)

**Principle**: the blast radius of a leaked cloud credential or an over-broad IAM policy is
usually larger than any single application bug.

- Storage buckets/containers: default-private, not publicly listable/readable unless that's an
  explicit product requirement
- Service credentials scoped to least privilege, not an account-wide admin key reused
  everywhere
- Infra-as-code files (Terraform, CloudFormation, k8s manifests) checked for hardcoded secrets
  the same way application code is

---

## Severity & Reporting

For each finding, classify:

- **Critical** — directly exploitable now (hardcoded secret, missing authz on a data-mutating
  endpoint, SQL built by concatenation): **never auto-fix**, always flag and get explicit
  confirmation before touching it, since the fix may need coordinated secret rotation or a
  behavior change the user needs to approve
- **High** — exploitable under realistic conditions (missing rate limit on login, XSS sink
  with weak sanitization): propose the fix, apply it if it's a small, local, non-behavior-
  changing patch
- **Medium/Low** — hardening, defense-in-depth, missing headers: note them, fix opportunistically

Report format:

```markdown
## [Severity] Short title

**Category**: Secrets | Input Validation | Injection | AuthN/AuthZ | XSS | CSRF |
Rate Limiting | Data Exposure | Dependencies | Infra
**Location**: `path/to/file:line`

Evidence — the actual code/config found.

Fix — the minimal change that closes the gap.
```

## Output

At the end of a review, produce:

1. A prose summary (max 15 lines): stack detected, categories checked, count of findings by
   severity, and the single highest-priority item to fix first
2. The findings list in the format above, most severe first
3. If fixes were applied: which files changed and what specifically was fixed — never claim a
   category is "clean" without having actually grepped/read for it
