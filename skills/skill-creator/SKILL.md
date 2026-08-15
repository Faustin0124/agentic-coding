---
name: skill-creator
description: A skill for creating new skills and iteratively improving them through drafting, test prompts, evaluation, and revision. Use this skill whenever the user wants to create a new Claude skill, turn a workflow they just described into a reusable skill, improve/iterate on an existing skill's SKILL.md, or optimize a skill's description for better triggering — even if they don't use the word "skill" explicitly (e.g. "can you make this repeatable", "automate this for next time", "this should trigger automatically when I do X").
---

# Skill Creator

A skill for creating new skills and iteratively improving them. At a high level, the process of creating a skill goes like this:

* Decide what you want the skill to do and roughly how it should do it
* Write a draft of the skill
* Create a few test prompts and run claude-with-access-to-the-skill on them
* Help the user evaluate the results both qualitatively and quantitatively
  * While the runs happen in the background, draft some quantitative evals if there aren't any (if there are some, you can either use as is or modify if you feel something needs to change about them). Then explain them to the user (or if they already existed, explain the ones that already exist)
  * Use the `eval-viewer/generate_review.py` script to show the user the results for them to look at, and also let them look at the quantitative metrics
* Rewrite the skill based on feedback from the user's evaluation of the results (and also if there are any glaring flaws that become apparent from the quantitative benchmarks)
* Repeat until you're satisfied
* Expand the test set and try again at larger scale

Your job when using this skill is to figure out where the user is in this process and then jump in and help them progress through these stages. So for instance, maybe they're like "I want to make a skill for X". You can help narrow down what they mean, write a draft, write the test cases, figure out how they want to evaluate, run all the prompts, and repeat. On the other hand, maybe they already have a draft of the skill. In this case you can go straight to the eval/iterate part of the loop. Of course, you should always be flexible and if the user is like "I don't need to run a bunch of evaluations, just vibe with me", you can do that instead.

Then after the skill is done (but again, the order is flexible), you can also run the skill description improver (Step "Description Optimization" below) to optimize the triggering of the skill.

> **Note on this repo's installation**: the bundled helper resources referenced below (`agents/grader.md`, `agents/comparator.md`, `agents/analyzer.md`, `references/schemas.md`, `scripts/aggregate_benchmark.py`, `scripts/package_skill.py`, `scripts/run_loop.py`, `eval-viewer/generate_review.py`, `assets/eval_review.html`) are **not present** in this repository — only this workflow document was ported over. The qualitative loop (interview → draft → run test prompts → discuss results → revise) works fully without them. Anything that depends on a missing script (benchmark aggregation, the HTML eval viewer, automated description optimization, packaging) should be flagged to the user as unavailable, with the option to do it manually/inline instead, or to source the original files from the upstream skill-creator package if the user has access to it.

## Communicating with the user

The skill creator is liable to be used by people across a wide range of familiarity with coding jargon. Pay attention to context cues to understand how to phrase your communication! In the default case, just to give you some idea:

* "evaluation" and "benchmark" are borderline, but OK
* for "JSON" and "assertion" you want to see serious cues from the user that they know what those things are before using them without explaining them

It's OK to briefly explain terms if you're in doubt, and feel free to clarify terms with a short definition if you're unsure if the user will get it.

## Creating a skill

### Capture Intent

Start by understanding the user's intent. The current conversation might already contain a workflow the user wants to capture (e.g., they say "turn this into a skill"). If so, extract answers from the conversation history first — the tools used, the sequence of steps, corrections the user made, input/output formats observed. The user may need to fill the gaps, and should confirm before proceeding to the next step.

1. What should this skill enable Claude to do?
2. When should this skill trigger? (what user phrases/contexts)
3. What's the expected output format?
4. Should we set up test cases to verify the skill works? Skills with objectively verifiable outputs (file transforms, data extraction, code generation, fixed workflow steps) benefit from test cases. Skills with subjective outputs (writing style, art) often don't need them.

Suggest the appropriate default based on the skill type, but let the user decide.

### Interview and Research

Proactively ask questions about edge cases, input/output formats, example files, success criteria, and dependencies. Wait to write test prompts until you've got this part ironed out. Check available MCPs — if useful for research (searching docs, finding similar skills, looking up best practices), research in parallel via subagents if available, otherwise inline. Come prepared with context to reduce burden on the user.

### Write the SKILL.md

Based on the user interview, fill in these components:

* **name**: Skill identifier
* **description**: When to trigger, what it does. This is the primary triggering mechanism — include both what the skill does AND specific contexts for when to use it. All "when to use" info goes here, not in the body. Note: currently Claude has a tendency to "undertrigger" skills — to not use them when they'd be useful. To combat this, make the skill description a little bit "pushy". So for instance, instead of "How to build a simple fast dashboard to display internal data.", write "How to build a simple fast dashboard to display internal data. Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'"
* **compatibility**: Required tools, dependencies (optional, rarely needed)
* the rest of the skill :)

#### Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Files used in output (templates, icons, fonts)
```

#### Progressive Disclosure

Skills use a three-level loading system:

1. Metadata (name + description) — Always in context (~100 words)
2. SKILL.md body — In context whenever skill triggers (<500 lines ideal)
3. Bundled resources — As needed (unlimited, scripts can execute without loading)

These word counts are approximate and you can feel free to go longer if needed. Key patterns:

* Keep SKILL.md under 500 lines; if you're approaching this limit, add an additional layer of hierarchy along with clear pointers about where the model using the skill should go next to follow up.
* Reference files clearly from SKILL.md with guidance on when to read them.
* For large reference files (>300 lines), include a table of contents.

Domain organization — when a skill supports multiple domains/frameworks, organize by variant:

```
cloud-deploy/
├── SKILL.md (workflow + selection)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

Claude reads only the relevant reference file.

#### Principle of Lack of Surprise

A skill must not contain malware, exploit code, or any content that could compromise system security. A skill's contents should not surprise the user in their intent if described. Don't go along with requests to create misleading skills or skills designed to facilitate unauthorized access, data exfiltration, or other malicious activities. Things like "roleplay as an XYZ" are OK though.

#### Writing Patterns

Prefer the imperative form in instructions.

Defining output formats:

```markdown
## Report structure
ALWAYS use this exact template:
# [Title]
## Executive summary
## Key findings
## Recommendations
```

Examples pattern:

```markdown
## Commit message format
**Example 1:**
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

#### Writing Style

Explain to the model *why* things are important in lieu of heavy-handed musty MUSTs. Use theory of mind and try to make the skill general and not super-narrow to specific examples. Start by writing a draft and then look at it with fresh eyes and improve it.

### Test Cases

After writing the skill draft, come up with 2-3 realistic test prompts — the kind of thing a real user would actually say. Share them with the user: "Here are a few test cases I'd like to try. Do these look right, or do you want to add more?" Then run them.

Save test cases as a simple JSON list (e.g. `evals/evals.json` next to the skill, or inline if the user prefers no extra files):

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": []
    }
  ]
}
```

Don't write assertions yet — just the prompts. Draft assertions in the next step while the runs are in progress.

### Running and evaluating test cases

This section is one continuous sequence — don't stop partway through.

**Step 1 — Spawn all runs (with-skill AND baseline) in the same turn.** For each test case, spawn two subagents in the same turn (if subagents are available) — one with the skill, one without. Don't spawn the with-skill runs first and come back for baselines later; launch everything at once so it all finishes around the same time.

* With-skill run: give it the skill path, the eval prompt, any input files, and tell it where to save outputs.
* Baseline run: same prompt, no skill (for a brand-new skill) or the previous version of the skill (for an iteration — snapshot it first).

If subagents aren't available (e.g. on Claude.ai), run test cases yourself, one at a time, skipping baselines.

**Step 2 — While runs are in progress, draft assertions.** Don't just wait — draft quantitative, objectively-verifiable assertions for each test case and explain them to the user. Subjective skills (writing style, design quality) are better evaluated qualitatively — don't force assertions onto things that need human judgment.

**Step 3 — Capture timing data as runs complete**, if subagent task notifications expose `total_tokens` / `duration_ms`.

**Step 4 — Grade, aggregate, and present results.**

1. Grade each run against its assertions (inline, or via a dedicated grading pass if the user wants rigor).
2. If the bundled `scripts/aggregate_benchmark.py` and `eval-viewer/generate_review.py` are available in this installation, use them to produce a benchmark summary and an interactive viewer. **In this repo, those scripts are not bundled** — instead, present each test case's prompt + output directly in the conversation (or save outputs to files and point the user at them), and summarize pass/fail per assertion in a short table.
3. Do an analyst pass: read the results and surface patterns the aggregate might hide — assertions that always pass regardless of skill (non-discriminating), high-variance evals (possibly flaky), time/token tradeoffs.

**Step 5 — Read the feedback.** Ask the user directly: "How do these look? Anything you'd change?" Focus improvements on the test cases where the user had specific complaints. Empty/positive feedback means that case was fine.

## Improving the skill

This is the heart of the loop. You've run the test cases, the user has reviewed the results, and now you need to make the skill better based on their feedback.

How to think about improvements:

1. **Generalize from the feedback.** The big picture is that we're trying to create skills that can be used many times across many different prompts. The user is iterating on only a few examples because it's quick to assess — but if the skill only works for those examples, it's useless. Rather than fiddly overfitted changes or oppressively constrictive MUSTs, if there's a stubborn issue, try branching out with different metaphors or recommending different patterns of working.
2. **Keep the prompt lean.** Remove things that aren't pulling their weight. If it looks like the skill is making the model waste time on unproductive things, try removing the parts causing that and see what happens.
3. **Explain the why.** Try hard to explain the reasoning behind every instruction. If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag — reframe and explain the reasoning instead.
4. **Look for repeated work across test cases.** If multiple test runs independently took the same multi-step approach or wrote similar helper code, that's a signal the skill should bundle a script for it instead of having the model reinvent it every time.

### The iteration loop

After improving the skill:

1. Apply your improvements to the skill.
2. Rerun all test cases (including baselines, if using subagents).
3. Present the new results alongside the previous iteration's, so the user can compare.
4. Wait for the user's feedback, improve again, repeat.

Keep going until: the user says they're happy, the feedback is all empty/positive, or you're not making meaningful progress.

### Advanced: Blind comparison

For a more rigorous comparison between two versions of a skill (e.g., "is the new version actually better?"), you can give two outputs to an independent subagent without telling it which is which, and let it judge quality, then analyze why the winner won. This requires subagents, is optional, and most users won't need it — the human review loop is usually sufficient.

## Description Optimization

The `description` field in SKILL.md frontmatter is the primary mechanism that determines whether Claude invokes a skill. After creating or improving a skill, offer to optimize the description for better triggering accuracy.

**Step 1 — Generate trigger eval queries.** Create ~20 eval queries — a mix of should-trigger and should-not-trigger:

```json
[
  {"query": "the user prompt", "should_trigger": true},
  {"query": "another prompt", "should_trigger": false}
]
```

Queries must be realistic — concrete and specific, with file paths, personal context, names, a little backstory. Mix lengths, casual phrasing, typos.

Bad: `"Format this data"`, `"Create a chart"`
Good: `"ok so my boss just sent me this xlsx file (its in my downloads, called something like 'Q4 sales final FINAL v2.xlsx') and she wants me to add a column that shows the profit margin as a percentage. The revenue is in column C and costs are in column D i think"`

For should-trigger queries (8-10): cover different phrasings of the same intent, formal and casual, cases where the user doesn't explicitly name the skill, uncommon use cases, and cases where this skill competes with another but should win.

For should-not-trigger queries (8-10): focus on genuine near-misses — adjacent domains, ambiguous phrasing a naive keyword match would wrongly trigger on, cases where another tool is more appropriate. Avoid obviously-irrelevant negatives; they test nothing.

**Step 2 — Review with the user.** Present the eval set for review and let them edit/add/remove entries before proceeding.

**Step 3 — Run the optimization loop.** The original skill-creator package automates this with a `scripts/run_loop.py` script (splits queries into train/test, evaluates the current description via the live model, proposes improvements, iterates up to 5 times, selects by test score to avoid overfitting). **That script is not bundled in this repo.** As a manual substitute: for each query, reason about whether the current description would plausibly cause Claude to consult the skill, identify the false positives/negatives, and propose a revised description; repeat 2-3 times with the user reviewing each revision.

**Step 4 — Apply the result.** Update the skill's SKILL.md frontmatter with the improved description. Show the user before/after.

## Updating an existing skill

The user might be asking you to update an existing skill, not create a new one. In this case:

* Preserve the original name and directory — don't rename `research-helper` to `research-helper-v2`.
* If iterating on a packaged/installed skill in a read-only location, copy it to a writable scratch location first, edit there, then write back.

## Packaging

The original skill-creator package includes a `scripts/package_skill.py` that bundles a skill folder into a distributable `.skill` file, plus a `present_files`-gated step to hand it to the user. **Neither is bundled in this repo.** For this project, skills simply live under `.claude/skills/<name>/SKILL.md` and are used directly from the repo — no packaging step is needed.

---

Core loop, for emphasis:

* Figure out what the skill is about
* Draft or edit the skill
* Run claude-with-access-to-the-skill on test prompts
* With the user, evaluate the outputs and iterate until satisfied
* Leave the finished skill in place (or package it, if the user is exporting it elsewhere)
