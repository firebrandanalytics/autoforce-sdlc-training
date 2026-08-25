# Claude Code Commands — Muscle-Memory Card

Autoforce Developer AI Training · Instructor request — highest-frequency commands only

These are the commands, shortcuts, and features you'll reach for every day. Not
exhaustive — just the ones worth memorising. A few keyboard shortcuts differ on
Windows; those are noted inline.

> **Surfaces move fast.** This card was checked against the Claude Code docs on
> **August 25, 2026**.
> Run **`/help`** in *your* installed version before leaning on anything here —
> and if a command below isn't in your `/help` list, you're on an older build.

**Commands you'll actually practise in this course are marked ▶.** Each one has a
five-minute drill in a session; the rest are here for when you need them.

---

## Starting a Session

Run these in your terminal (Git Bash on Windows) to start Claude Code.

| What you want | How to do it |
|--------------|-------------|
| Start Claude Code in the current directory | `claude` |
| Start with a specific model | `claude --model claude-haiku-4-5` |
| Start in planning mode (plan before executing) | `claude --permission-mode plan` |
| Resume the previous session | `claude --continue` |
| Pick an earlier session to resume | `claude --resume` |
| Run one prompt and exit (scriptable) | `claude -p "<prompt>"` |

---

## Knowing Where You Are

The four questions you should never have to guess at. **Cheap, read-only, and
the fastest way to catch a session that's drifting.**

| Command | What it does |
|---------|-------------|
| ▶ `/status` | Session info at a glance — model, approval mode, working directory |
| ▶ `/context` | Visualise context usage as a coloured grid. *Look at this before a big ask.* |
| ▶ `/usage` | Token usage and cost for this session (`/cost` is the same command) |
| `/tokens [path]` | Count tokens in a file, a directory, or the conversation |

> **The habit worth building:** `/context` before you start something large, and
> again after `/compact`. Watching the grid empty is what turns "manage your
> context" from advice into a control you can actually feel.

---

## During a Session — Slash Commands

Type these at the Claude Code prompt (the `>` line).

| Command | What it does |
|---------|-------------|
| `/help` | List available slash commands |
| ▶ `/btw <question>` | Ask a quick **side question — even while Claude is mid-task**. The answer appears in a dismissible overlay (`Esc` closes) and never enters the conversation, so it can't derail the work. It sees the whole session but can't run tools: perfect for *"what are you doing right now?"* or *"what does that term mean?"* while a build runs. |
| `/plan` | Ask Claude to write a plan for what it's about to do, and pause for your approval before executing anything |
| ▶ `/compact` | Summarise and compress the conversation context. Use before context fills up and quality degrades. Does NOT start a new conversation — history is summarised, not cleared. |
| `/clear` | Clear the conversation entirely and start fresh. Use when you are done with a task and starting something unrelated, or when the context has drifted far from the current task. |
| ▶ `/rewind` | **Roll code *and* conversation back to an earlier checkpoint.** The undo button under "let it run" — see the box below. |
| `/model <name>` | Switch the model mid-session |
| `/diff` | Interactive viewer for uncommitted changes and per-turn diffs |
| `/todo` | Manage a task list for the session (`add`, `list`, `check`, …) |
| `/doctor` | Diagnose a broken setup — checks your install, config, and environment, and can offer fixes |
| `/permissions` | Review and edit the allow / ask / deny rules for tool use |

### ▶ `/rewind` — the undo you didn't know you had

Approved something you shouldn't have? Let a refactor run three files too far?
`/rewind` rolls **both** the code and the conversation back to a checkpoint, so
the session forgets the detour instead of arguing with it.

```
/rewind                     # pick a checkpoint from the list
/rewind <description>       # jump back to a described point
```

> **Why this matters more than it sounds.** Every approval decision you make is
> a bet on how hard the mistake is to undo. `/rewind` makes a whole class of
> mistakes cheap — which means you can safely operate in a faster mode than you
> otherwise would. It's not a recovery tool; it's a *permission* tool. Note
> what it does **not** cover: anything already pushed, deployed, or run against
> a real system. Those still deserve Manual mode and a careful read of the
> permission prompt.

---

## Beyond One Reply

Everything above runs inside one back-and-forth. These get Claude working past
the end of your turn. **Reach for them only once you've run the loop by hand and
trust its gate** — an unattended agent is exactly as good as the check you put
around it.

| Command | What it does | Don't confuse it with |
|---------|-------------|----------------------|
| ▶ `/goal <condition>` | Sets a **measurable finish line**, constraints, and a turn/time bound. Claude keeps working across turns until the condition is true. *"Audit these three files without editing; stop after 6 turns."* | `/loop` — a goal runs on a **condition**; a loop runs on a **timer** |
| `/loop [interval] <prompt>` | Re-runs a prompt on an interval while the session stays open. *"check if the deploy finished."* | `cron` — a loop dies when you close the session |
| `/schedule` | Recurring or one-off runs on Anthropic's cloud, so they survive you closing the laptop. *Research preview.* | `/loop` — this one outlives the session |
| `/batch <instruction>` | One prompt, **many files, in parallel**. *"rename this symbol across 40 files."* | `/goal` — batch is about breadth, not persistence |
| ▶ `/agents` | Create and manage reusable **subagents** — scoped workers with their own clean context. Give one your review rubric and point it at your PR. | `/subtask` — `/agents` defines them; `/subtask` fires a one-off |
| `/subtask <prompt>` | Hand a side task to a subagent that reports back into this conversation | a new session — this one comes back to you |
| `/tasks` | What's actually running right now in this session | `/context` — that's memory, this is work in flight |

> **The rule that governs all of them:** a goal of *"until tests pass"* against
> tests you never read is the automation of a mistake. Read the gate first.

---

## Keyboard Shortcuts

These work *inside* a Claude Code session — no slash, just the keys.

**Controlling the session**

| Keys | What it does |
|------|-------------|
| `Ctrl+C` | Cancel the current input or generation; press twice to exit |
| `Esc` | Interrupt Claude while it is working; press twice or use `/rewind` to jump to an earlier checkpoint |
| `Ctrl+D` | Exit Claude Code |
| `↑` / `↓` | Scroll back through your previous prompts |
| `Ctrl+R` | Search your prompt history |

**Writing a prompt**

| Keys | What it does |
|------|-------------|
| `Ctrl+J` | New line *without* submitting — for multi-line prompts |
| `Ctrl+G` | Open your prompt in an external editor (handy for long prompts) |
| `Ctrl+V` | Paste an image — e.g. a screenshot (Windows / Git Bash: `Alt+V`) |

**Seeing what happened**

| Keys | What it does |
|------|-------------|
| `Ctrl+O` | Toggle the full transcript — every tool call and the full output |
| `Ctrl+T` | Toggle the task / to-do list |

> Shortcuts are customisable — run `/keybindings` to see or change them.

---

## Permission & Approval

Two things to know here: which *mode* you are in, and what you press when
Claude *asks*.

**Cycle the approval mode** — press `Shift+Tab` to rotate through the modes
available in your build. Watch the mode indicator in the input box; some current
builds start in Auto mode.

1. **Manual** — Claude asks before actions that need permission
2. **Accept edits** — file edits apply automatically; other actions can still ask
3. **Plan mode** — Claude analyzes and plans without modifying the project
4. **Auto mode** — Claude handles routine permissions automatically within its safety boundaries

The current mode is shown in the input box as you work.

**At a permission prompt** — when Claude stops to ask before running something:

| Keys | What it does |
|------|-------------|
| `↑` / `↓` | Move through the available choices |
| `Enter` | Select the highlighted choice |
| `Esc` | Decline or dismiss the prompt |
| `Tab` | Add a comment or constraint before Claude proceeds |

> On anything you are not sure about — an unfamiliar command or a multi-file
> edit — read the proposed action and use `Tab` to add a constraint before you
> approve it. You can also ask Claude in plain English before approving (see
> Useful One-Liners below).

> **Quick discipline:** start a new codebase in Manual mode. Move to
> Auto-accept once you have seen a few actions and trust the direction. Knowing
> `/rewind` has your back is what makes that step up reasonable.

---

## Context Management — When to Use Which

| Situation | Right move |
|-----------|-----------|
| Context is filling up but you're mid-task | `/compact` — preserves the task, compresses history |
| Task is complete; starting something unrelated | `/clear` — start fresh |
| New day, new task, unclear what's in context | Start a new `claude` session entirely |
| Context has drifted (agent is giving stale answers) | `/clear` and re-state the task cleanly |
| You want to *see* the problem before deciding | `/context` — then pick from the rows above |
| You need a reviewer with no stake in the code | A **fresh session** or a subagent — not this one |

> **Rule of thumb:** if you feel like you're fighting the context to get a good answer, clear it. The re-statement cost is lower than the compounding cost of a confused agent.

---

## Referencing Files

Claude Code can read files directly — you don't need to paste content.

```
Read main.py and tell me where the delete endpoint should go.
```

```
Before you start, read CLAUDE.md, db.py, and service.py.
```

```
Look at the failing test in tests/test_routes.py and fix what's failing.
```

> **Tip:** Tell the agent which files to read *before* it writes anything. Saves a round-trip of "I assumed the schema was X but it's actually Y."

---

## Useful One-Liners

```bash
# Ask Claude Code to explain a change before you approve it
# (just type this at the > prompt, mid-session)
What exactly will you change, and why? Show me the file paths and the lines affected.

# Planning mode — ask for a plan first
Plan the implementation of [feature] before you write any code.
List the files you'll touch and the order you'll work in.

# Asking for a review pass
Read the diff in [file] and tell me if anything looks wrong before I commit.

# Anchoring scope
Only modify db.py and tests/test_db.py. Do not touch main.py or service.py yet.

# Setting a bounded, read-only finish line instead of a next step
/goal Audit SPEC.md against stories.md without editing files. Cite every gap and stop after 6 turns.
```

---

## Things Worth Knowing

- **Claude Code inherits your shell's environment.** Variables you export in your shell (or load from `.env`) are available to the commands the agent runs.
- **`!` runs a command in YOUR shell** and shares the output back into Claude's context. The escape hatch for a quick check or an interactive login. It is **not trimmed** — pipe it (`! cmd | head`) so you don't dump a log, or a secret, into context.
- **Conversation history is saved locally and can be resumed.** Use `claude --continue` for the most recent session or `claude --resume` to choose one.
- **The agent sees your working directory.** It reads files relative to where you started `claude`. Start from the repo root.
- **Long outputs can be truncated.** Press `Ctrl+O` to inspect the transcript, narrow the command, or ask the agent to write full output to a file.
- **The status line is yours to configure.** Run `/statusline` and describe what you want on it — model, branch, context percentage — and Claude Code writes the script and the setting for you.
