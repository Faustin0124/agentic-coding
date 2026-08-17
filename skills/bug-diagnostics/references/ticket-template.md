# Bug Ticket Template

The structure to generate in Phase 5. Reproduce these fields, in this order, regardless of
where the ticket ends up (chat display, Notion, GitHub issue, local file) — only the rendering
mechanics differ per destination, covered below.

---

## Display format (chat / local file)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🐛 BUG TICKET — [SHORT TITLE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 GENERAL INFO
  Severity     : 🔴 P0 Blocking | 🟠 P1 Critical | 🟡 P2 Major | 🟢 P3 Minor
  Status       : 🆕 To do
  Date         : [today's date]
  Environment  : Dev / Staging / Production

🔍 DESCRIPTION
  [Clear description of the bug in 2-3 sentences, understandable without technical context]

💥 REPRODUCTION
  Steps:
    1. [Action 1]
    2. [Action 2]
    3. [Observed result]
  Frequency    : Consistent / Intermittent / One-off
  Regression   : Yes (since [date/commit]) / No / Unknown

🧠 ROOT CAUSE
  [Technical explanation of the cause — 2-4 sentences]
  File(s)      : src/path/to/file.ts (line X)

📡 PROPAGATION
  Isolated impact : Yes / No
  At-risk zones:
    - src/... → [nature of the risk]

🔧 RESOLUTION PLAN
  Fix          : [Description of the correction]
  Files        : [files to modify]
  Tests        : [tests to write/modify]

  Estimate:
    Time       : X minutes / X hours
    Complexity : Low / Medium / High
    Deployable alone : Yes / No

⚠️ POINTS OF ATTENTION
  [Risks, dependencies, things to watch — empty if none]

🏷️ TAGS
  [bug] [relevant-domain-tag] [priority-P0/P1/P2/P3]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Title-writing rules

The title should be:
- Short (< 60 characters)
- Factual and precise
- Format: `[Component/Feature] — [Short description of the problem]`

Good:
- `Auth — Post-login redirect fails in production`
- `PricingTable — Crash sorting the amount column`

Avoid:
- `Bug in the code` — too vague
- `It doesn't work` — not actionable
- A full paragraph as the title — too long, put detail in the description

---

## Filing to Notion (if that's the chosen destination)

Don't assume a specific database or property schema — every project's Notion setup differs.

1. **Find the target database.** Use `notion-search` with a query like "bugs", "tickets", or
   "backlog". If multiple results come back, present them and ask the user to pick. If nothing
   matches, ask for the database URL or name directly.
2. **Read its real schema.** Use `notion-fetch` on the database before creating anything, and
   adapt the mapping below to whatever properties actually exist — don't assume `Severity` or
   `Status` properties exist just because they're common. If a property this template wants
   doesn't exist, put that information in the page body instead of dropping it.

   | Ticket field | Typical Notion property | Type |
   |---|---|---|
   | Title | `Name` (page title) | title |
   | Severity | `Severity` | select |
   | Status | `Status` | status/select |
   | Date | `Reported date` | date |
   | Environment | `Environment` | select |
   | Tags | `Tags` | multi_select |
   | Everything else | Page body | blocks |

3. **Create the page** with `notion-create-pages`, `parent` pointing at the database found in
   step 1, properties mapped per step 2, and the full formatted ticket as the page body.
4. **Confirm and share the link**:
   ```
   ✅ Ticket created in Notion
   🔗 [Title](page-url)
   ```

If the user has no dedicated bugs database yet, offer to create one with
`notion-create-database` using a minimal recommended schema: `Name` (title), `Severity`
(select), `Status` (select), `Reported date` (date), `Environment` (select), `Tags`
(multi_select).

**Error handling:** database not found → ask for the direct URL. Unknown property → put the
info in the body instead of failing. MCP auth error → tell the user the Notion connector needs
reauthorizing. Timeout → retry once, then offer to hand over the ticket text for manual entry.

## Filing to GitHub Issues (if that's the chosen destination)

Use whatever GitHub tooling is available (`gh issue create`, or a GitHub MCP's issue-write
tool). Title and body map directly from the template above — no schema translation needed, it's
just markdown. Apply labels if the repo has a bug label convention; otherwise skip labeling
rather than inventing label names that might not exist.
