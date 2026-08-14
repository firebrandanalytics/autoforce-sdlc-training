# C11 — Advanced Claude Code: The Power Tools

**Where the course stops, and what's past it.** Everything in the course ran in
one interactive session: you ask, you read, you approve. These features are
what's beyond that — and every one of them is the same discipline you already
practice (gates, contracts, review), running with less of you in the room.

**You've already used three of them.** `/subtask` fanned out the three magic-value
decodes in Session 3; `/goal` drove the build to green in Session 4; `/agents`
turned your clean-context reviewer into a reusable one in Session 5. So this card
isn't a list of things to try someday — it's mostly the *next size up* of moves
you've made.

Surfaces evolve quickly: treat this card as the map, and check `/help` and
**code.claude.com/docs** in *your* installed version before leaning on anything.
(Checked against **2.1.232**.)

---

## Which one do I reach for?

| I want to… | Reach for |
|---|---|
| Keep going until something is **true** | `/goal` |
| Check back on a **timer**, still in this session | `/loop` |
| Keep running **after I close the laptop** | `/schedule` or cron + headless |
| Make the **same edit across many files**, fast | `/batch` |
| Hand off **one scoped piece** and get a summary back | `/subtask` |
| Keep a **reusable** specialist (a reviewer, a migrator) | `/agents` |
| See what's **running right now** | `/tasks` |

> Two distinctions people get wrong: **`/goal` runs on a condition, `/loop` runs
> on a timer.** And **`/loop` dies when you close the session; a scheduled run
> doesn't.**

---

## 1 · Make the status line yours

**What it is.** The strip at the bottom of Claude Code is configurable: a
`statusLine` entry in `settings.json` runs a small script whose output is your
status bar — model, git branch, context usage, cost, whatever you decide you
should never have to ask about.

**Why you'd bother.** Session 2's levers (model, context, mode) only help if you
*notice* them. Knowing you're on the expensive model, or that context is nearly
full, **before** the big ask is operator awareness made permanent.

**First step.** Type **`/statusline`** and describe what you want — Claude Code
sets it up for you (it writes the script and the setting). Docs:
*code.claude.com/docs → Settings*.

---

## 2 · Agents on a clock — scheduled runs

**What it is.** Three shapes, least to most plumbing:

- **`/schedule`** — recurring or one-off tasks on Anthropic's cloud
  infrastructure ("routines"; manage at *claude.ai/code/routines*). Runs
  without your machine on. *Research preview — expect change.*
- **Headless mode** — `claude -p "<prompt>" --permission-mode acceptEdits`
  prints a result and exits, so your ordinary OS scheduler (cron, Task
  Scheduler) can run an agent like any other job. Stable, works anywhere — and
  the agent will happily write its own crontab entry if you ask it to.
- **Scheduled wake-ups inside a session** — ask Claude Code to check back on
  something periodically and it can put itself on a clock; see *Scheduled
  tasks* in the docs.

**Why you'd bother — cadences we actually run:**

- **The monitor.** Your Session 4 done-gate — tests, reconcile, log ↔ database
  — is a prompt. Run nightly against the volumes service it's a monitor:
  silence while the numbers hold, a morning message when they drift.
- **The maintainer.** A weekly routine checks whether OpenAI, Anthropic, or
  Google shipped a new SDK; when one lands, it upgrades the affected codebase,
  runs the full test suite, fixes what the upgrade broke, and opens a PR. Not
  "bump the version" — *prove it still works*. The human's whole job is
  merging a green PR. (The same cadence keeps docs and diagrams current with
  the code they describe.)
- **The chief of staff.** Our most common pattern: several Claude Code
  sessions working in parallel — one per tmux window — and one orchestrator
  session that wakes on a cron, checks the others' progress, nudges the
  stalled ones, and reports. Agents managing agents, with the same gates you'd
  give a team.

**First step.** Run your validation prompt once via `claude -p` and read the
output; *then* put it on a clock. Docs: *Routines*, *Headless mode*,
*Scheduled tasks*.

---

## 3 · Loops and goals — iterate without re-prompting

**What it is.**

- **`/goal <condition>`** keeps the session working **until a condition is
  met**. Sets the finish line, not the steps.
- **`/loop [interval] <prompt>`** re-runs a prompt on an interval inside your
  session (or `/loop <prompt>` and it picks its own pacing). Good for polling a
  deploy or babysitting CI while you work on something else.

**You did this.** Session 4, Step 4: `/goal keep working until python -m pytest
is green` drove the build from red to green without you nudging it. Remember the
order you did it in, because it's the whole discipline — **you read the tests and
cross-checked the anchor numbers against the legacy script's printed output
BEFORE you set the goal.**

> A goal of *"until tests pass"* against tests you never read is the automation of
> a mistake. It will get there. It will be wrong. And it will be wrong faster and
> more confidently than if you'd done it by hand.

**The step up.** Chain them: a goal whose condition is a *validation gate* rather
than a test run — *"keep working until pytest passes AND the CLI output reconciles
to vol_report.py"*. That's your Session 4 done-gate, automated, and it's only
sound because you built the gate first.

**Next step.** Try `/loop` on something you currently babysit: *"`/loop 5m` check
whether the deploy finished and report status."* Docs: *Scheduled tasks*, *Goal*.

---

## 4 · Subagents, and orchestrating many of them

**What it is.**

- **`/subtask <prompt>`** — hand one scoped piece to a subagent with its own
  clean context; it reports a summary back into your conversation.
- **`/agents`** — define **reusable** subagents. They live in `.claude/agents/`,
  which means they're committed, shared, and reviewable like any other code.
- **`/batch <instruction>`** — one prompt, many files, in parallel. *"Rename this
  symbol across 40 files." "Migrate every import path."* The tool for breadth,
  where the work is repetitive and the same rule applies everywhere.
- **Agent view** (`claude agents`) — dispatch and monitor several independent
  background sessions from one screen. *Research preview.*
- **Dynamic workflows** — script the orchestration itself: distinct phases (find,
  fix, verify), tens of agents, rerunnable later. Try the built-in
  `/deep-research` for the pre-built research version. *Research preview.*

**You did this, twice.** Session 3, Step 2a: three magic-value profiles fanned out
with `/subtask` — and the thing that made it work was that you could state each
scope in two sentences and the pieces couldn't contaminate each other. Session 5,
Step 9: your clean-context reviewer became a saved `volume-reviewer` that loads
your `autoforce-volume-rules` skill.

Carry the split you practised: **you delegated the gathering and kept the
judgment.** A subagent that hands you a confident conclusion has done the part
you were supposed to do.

**The step up — and the honest caveat.** `/batch` is the one you haven't used,
because this course built *one* service and batch is for breadth. It earns its
keep on the fifty-file jobs: a rename across a legacy codebase, a migration, an
audit of every query in a repo. **The failure mode scales with it** — fifty files
changed by a rule that was subtly wrong is worse than five, and no single diff
review will catch it. The contract and the verification step are what decide
whether scale helps or just produces wrong answers faster. Batch the mechanical;
verify the result the way you verified your service.

**Next step.** Point `/batch` at something genuinely repetitive and low-stakes
first — adding a missing docstring to every module, normalising a log format —
and diff the whole result before you commit. Docs: *Subagents*, *Agent view*,
*Workflows*.

---

## 5 · The browser is a tool too — test it like a user

**What it is.** Your dashboard tests call routes in-process — fast, but no
browser ever opens, so nothing proves the chart renders or the dropdown
actually filters. **Playwright** closes that gap, and two routes are equally
acceptable:

- **Directly, as code** (the way we use it ourselves): the agent installs it
  like any package (`pip install playwright && playwright install chromium`),
  writes a pytest that opens the page, picks a month, clicks DAL, and asserts
  what a *user* would see — then runs it headless like any other test. No new
  plumbing; this is Session 2's "Claude Code is also a shell," pointed at a
  browser.
- **Playwright MCP** (`claude mcp add playwright npx @playwright/mcp@latest`):
  wires the browser in as a tool the agent drives step by step — navigate,
  click, read, screenshot. Especially handy in Claude Desktop, or for
  exploratory "watch it click around" debugging before you ask for durable
  test code.

There's also **Claude in Chrome** — the extension (`claude --chrome`) that
drives the browser you're already logged into. GA on direct Anthropic plans
but beta and Chrome/Edge-only: check your plan and your browser policy first.

**Why you'd bother.** Half of what your team owns has a UI in front of it, and
"click through it like a user" is currently a human's job — Move 3 of the
extra credit is literally you, clicking. This makes that a test that runs
without you.

**The thought to leave with.** Your acceptance criteria were checkable all
course. The step past that — one we're exploring ourselves — is writing the
**test plan itself in natural language** (*"pick 2025-08, open DAL, the
numbers match the service"*) and letting the agent execute the *same plan*
against the JSON API or through the browser against the GUI. One plan, two
surfaces: the plan becomes the artifact, and the executor is fungible. If that
idea grabs you, you're ready for what comes after this course.

**First step.** Ask the agent to write one Playwright test for your
extra-credit dashboard's month filter and run it headless. Docs:
*playwright.dev* · *code.claude.com/docs → MCP, Chrome*.

---

## The rule that doesn't change

Every feature on this card removes a moment where you'd naturally be watching.
None of them removes your ownership. The Session 1 rule scales with the
automation: **an agent is exactly as trustworthy as the gates you put around
it** — least permission, checkable criteria, evidence before "done." Automate
the loop only after you've run it by hand and trust its gates. (You have. You
did. Start small.)
