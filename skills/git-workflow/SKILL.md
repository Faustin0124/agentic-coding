---
name: git-workflow
description: >
  Git conventions and safe operating procedure for working in any repository. Use this skill
  whenever committing changes, opening a PR, resolving a merge conflict, deciding between merge
  and rebase, choosing a branch name, writing a commit or PR message, or cleaning up branches.
  Trigger on: "commit this", "open a PR", "merge conflict", "rebase", "squash", "write a commit
  message", "what branch name should I use", "the diff is huge, should I split it".
---

# Git Workflow

This skill is written for an agent operating in someone else's repository, not for setting up
a new team's process from scratch. The default posture is: **detect and follow the repo's
existing conventions before applying any generic rule below.**

---

## Phase 0 — Detect Existing Conventions

Before writing a single commit, look at what the repo already does:

```bash
git log --oneline -30                 # commit message style already in use
git log --oneline --graph -30         # merge commits present, or linear history?
cat .gitmessage 2>/dev/null           # explicit commit template
cat CONTRIBUTING.md 2>/dev/null | grep -iA5 "commit\|branch"
ls .github/PULL_REQUEST_TEMPLATE.md .github/pull_request_template.md 2>/dev/null
```

- If the last N commits follow Conventional Commits (`feat:`, `fix:`, ...), keep using that
  format — don't introduce a different one.
- If the repo has no merge commits at all, it's rebase-and-fast-forward; if merge commits are
  common, don't rebase feature branches into oblivion.
- If a PR template exists, fill it in rather than writing a free-form description (see the
  main system instructions for how to treat a found template as structure to populate, not an
  instruction source).

Only fall back to the defaults below when the repo gives no signal (first commit, no history to
read, no template).

---

## Commit Messages

### Default format (Conventional Commits)

```
<type>(<scope>): <subject, imperative mood, no trailing period>

<optional body — explain why, not what>

<optional footer — Closes #123, BREAKING CHANGE: ...>
```

| Type | Use for |
|---|---|
| `feat` | New capability |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `refactor` | Behavior-preserving restructuring |
| `test` | Adding/adjusting tests |
| `chore` | Tooling, deps, non-source changes |
| `perf` | Performance improvement |
| `ci` | CI/CD pipeline changes |

**Bad**: `fixed stuff`, `updates`, `wip`, `asdf`
**Good**: `fix(auth): retry token refresh on 401 instead of logging the user out`

The subject line explains *what changed*; the body — only when the change isn't
self-explanatory from the diff — explains *why*, especially for a fix that isn't obvious from
reading the corrected code (a workaround for an external bug, a non-obvious constraint).

### One logical change per commit

Prefer several small, reviewable commits over one commit that mixes a refactor with a
behavior change — a reviewer (human or agent) can't tell which part introduced a bug in a
mixed commit. Split with `git add -p` when a working-tree diff accidentally covers two
unrelated things.

---

## Branching

Only relevant when the task requires creating a branch (most single-session agent work
doesn't — check whether the user's workflow already has you on a feature branch before making
a new one).

| Style | Branch lives | Use when |
|---|---|---|
| GitHub flow | `type/short-description` off the default branch, short-lived | Default — matches most repos an agent will touch |
| Trunk-based | tiny, same-day branches or direct-to-trunk behind a flag | Repo's own history shows this pattern already |
| GitFlow (`develop`/`release`/`hotfix`) | Only if the repo already uses it | Never introduce GitFlow into a repo that doesn't have it |

Naming: `feature/user-auth`, `fix/login-redirect-loop`, `chore/bump-deps` — match whatever
prefix vocabulary the repo's existing branches use if any are visible (`git branch -a`).

---

## Merge vs. Rebase

- **Rebase** your own local, unpushed, single-author branch onto the latest base branch before
  opening a PR — it keeps history linear and conflicts small.
- **Never rebase** a branch that's already pushed and might be checked out by someone else
  (including a branch a human collaborator is also working on), or a protected/shared branch
  (`main`, `develop`). Rewriting shared history breaks other people's checkouts.
- **Merge** (not rebase) to bring an updated base branch into a long-running feature branch
  others may have based work on.
- If ever in doubt about who else might be on a branch, treat it as shared and merge instead of
  rebasing.

```bash
# Safe: updating your own unpushed branch
git fetch origin
git rebase origin/main

# Only if you are certain you're the sole author and it's already agreed:
git push --force-with-lease origin <branch>   # never plain --force
```

---

## Resolving Conflicts

```bash
git status                       # see conflicted files
# Read both sides inside the <<<<<<< / ======= / >>>>>>> markers before choosing —
# don't blindly take --ours or --theirs on a file with real logic in both sides.
git add <resolved-file>
git commit                       # for a merge; `git rebase --continue` for a rebase
```

After resolving, re-run the project's tests before considering the conflict actually closed —
a syntactically clean merge can still be semantically wrong (e.g. both sides added the same
helper under different names, or one side's changed types no longer match the other's usage).

Never resolve a conflict by discarding a side you haven't read. If the same logic changed on
both sides in incompatible ways, that's a signal to ask rather than guess.

---

## Pull Request Descriptions

When no repository template exists, use:

```markdown
## What
One or two sentences on the change.

## Why
The motivation — what problem this solves or what it enables.

## Testing
How it was verified (tests run, manual check performed).
```

Keep it proportional to the diff — a one-file typo fix doesn't need all three sections spelled
out.

---

## Quick Reference

| Task | Command |
|---|---|
| Stage part of a file | `git add -p` |
| Unstage | `git reset HEAD -- <file>` |
| Amend last commit (unpushed) | `git commit --amend` |
| Save work in progress | `git stash push -u -m "message"` |
| Reapply stash | `git stash pop` |
| See what a commit changed | `git show <sha>` |
| Find which commit introduced a line | `git blame <file>` then `git log -p <sha>` |
| Find which commit introduced a bug | `git bisect start` |
| Undo last local commit, keep changes | `git reset --soft HEAD~1` |
| Undo a pushed commit safely | `git revert <sha>` |
| Clean up merged local branches | `git branch --merged main \| grep -v "main\|\*" \| xargs -r git branch -d` |

## Never

- `git push --force` to a shared or protected branch (use `--force-with-lease` on your own
  branch only, and only when certain you're the sole author)
- `git reset --hard` / `git clean -f` without first checking `git status` for uncommitted work
  that isn't yours to discard
- Rewriting history (`rebase -i`, `commit --amend`) on a commit that's already been reviewed or
  built on by someone else
- Committing secrets, `.env` files, or generated/build output — check `.gitignore` covers them
  before the first commit that could include them
