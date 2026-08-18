# Hands-On: Three Warm-Up Drills

Autoforce Developer AI Training · Session 2

**Time:** three drills, 5–7 minutes each, spread through the first hour ·
**Goal:** put your hands on the control surface *while* we're describing it,
instead of waiting until the build.

These are short and deliberately low-stakes. Each one is a single control you'll
use for the rest of the course — and each has a binary "did it work" check so you
know you got it. Your instructor will call each drill when we reach it; don't run
ahead.

> **Card:** everything here is on **CC — Claude Code Commands**. The commands
> marked ▶ on that card are the ones you practise today.

---

## Drill 1 — The orientation lap (5 min)

**When:** at the top of the session, right after the setup check.
**The idea:** you should never have to guess which model you're on, how full the
context is, what mode you're in, or which repository state you're looking at.
The built-in commands give you a snapshot; the status line turns the useful parts
into a persistent dashboard.

### Do this

1. In a terminal, `cd` into the training repository (or another Git repository)
   and run `claude`.
2. At the `>` prompt, run each of these and *read the output*:

   ```
   /status
   ```
   ```
   /context
   ```

3. Now ask Claude Code to set up your persistent status line:

   ```
   /statusline show the active model, context used as a percentage (not remaining), current working directory, and active git branch
   ```

   Approve the file-edit prompts if Claude Code asks for permission. Claude Code
   generates the status-line script and updates your settings automatically. If
   it does not appear immediately, send one harmless next message; settings take
   effect on the next interaction.

4. Read the new status line at the bottom of the interface. It should show:
   - the **active model**
   - **context used** as a percentage (we prefer used over remaining for this course)
   - the current working directory (**CWD**)
   - the active **Git branch**

5. Answer these three questions out loud (or in the chat):
   - **Which model** are you on right now?
   - **Which approval mode** are you in?
   - Roughly **how full** is your context — a sliver, or half the grid?

### Done when

You can state your model, your mode, and your context usage without guessing, and
you can point to the repository and branch you are working in. Your status line
should keep updating as the session changes.

> **Claude Code reference.** See [Customize your status line](https://code.claude.com/docs/en/statusline)
> for the `/statusline` command, the available `model.display_name`,
> `context_window.used_percentage`, `workspace.current_dir`, and Git data, plus
> examples of what Claude Code generates for you.

> **Why it matters.** Every lever we cover in the next hour — mode, model,
> context — is one you can only pull deliberately if you can *see* where it's
> set. This is the dashboard. Glance at it before any big ask.

---

## Drill 2 — `/rewind`: approve, regret, undo (7 min)

**When:** during the approval-modes beat.
**The idea:** the reason you can afford to let the agent run is that you can take
it back. `/rewind` lets you choose whether to roll back the **conversation**, the
**code**, or both.

> **Mode check first.** Claude Code now starts in **Auto mode** by default in the
> current setup. For this exercise, press **`Shift+Tab`** until the mode indicator
> says **Manual** (the underlying mode is called `default`). We want you to see
> and approve each action while you practise the safety net.

### Do this

1. Make a scratch directory and start Claude Code in it:

   ```
   mkdir /tmp/rewind-drill && cd /tmp/rewind-drill
   claude
   ```

2. Ask for something small and concrete:

   > *"Create a file `notes.md` with three bullet points about fuel terminals."*

   Approve it. Confirm the file exists — ask the agent to show it to you, or
   run `! cat notes.md`.

3. Now ask for something you'll want to undo:

   > *"Rewrite `notes.md` completely — replace it with a ten-item checklist about
   > something unrelated, and add two more files while you're at it."*

   Approve that too. Look at the mess.

4. Roll it back:

   ```
   /rewind
   ```

   Pick the checkpoint from before step 3. The menu gives you separate choices:

   - **Restore conversation** — rewind the transcript, but keep the current files.
   - **Restore code** — restore the files, but keep the rewritten conversation.
   - **Restore code and conversation** — restore both.

   For the main exercise, choose **Restore code and conversation**. Then check
   what happened with `! ls` and `! cat notes.md`. The extra files disappear only
   when you choose an option that restores the code. If you choose conversation
   only, the conversation goes back but `notes.md` stays rewritten and the extra
   files remain.

### Done when

`notes.md` is back to your three bullets, the extra files are gone, **and** the
agent doesn't reference the rewritten version when you ask it what's in the file.
That second part is the one people miss: the conversation rolled back too. If you
chose conversation-only instead, the files should still be present; that's the
point of noticing what each rewind choice actually restores.

> **Why it matters.** Every approval you give is a bet on how hard the mistake
> would be to undo. `/rewind` makes a whole class of mistakes cheap, which is
> what lets you work in a faster mode than you otherwise would.
>
> **And know its edges.** It does not reach anything already pushed, deployed, or
> run against a real system. Those still get Manual mode and `Ctrl+E`.

---

## Drill 3 — Watch your context move, then compact it (6 min)

**When:** during the context and model-selection beat.
**The idea:** context is measurable, not vibes. You're about to create a small
piece of code, write tests that expose its bugs, fix it, and watch the context
window grow after each step before compacting it back down.

### Do this

1. Stay in the same empty scratch directory from Drill 2, but start a fresh
   conversation:

   ```
   /clear
   ```

   `/clear` removes the conversation from the active context but leaves the
   directory and its files in place. Take a baseline:

   ```
   /context
   ```

   Note roughly how much of the grid is filled.

2. **Create a deliberately imperfect script.** Paste this prompt into Claude Code:

   ```
   Create a Python file called buggy_report.py, about 100 lines long, for a small monthly sales report. Use only the Python standard library. Include a summarize(rows) function that accepts rows like {"month": "2026-01", "product": "coffee", "units": 3, "price": 2.50} and returns a list of dictionaries. The contract is: group by month and product; sum units; calculate total_sales as units * price rounded to two decimals; sort the output by month ascending and then product ascending; and reject negative units with ValueError. Include docstrings, comments, a small main() with sample data, and enough readable structure to make this a roughly 100-line script. Deliberately include exactly two small, plausible bugs in summarize() or its helpers that violate the contract and will be exposed by these tests; do not put the bugs only in main(). Do not reveal which lines are buggy, and do not write tests yet. Make sure the script is syntactically valid and runs.
   ```

   When it finishes, run:

   ```
   /context
   ```

   The grid should be visibly fuller.

3. **Write tests that should fail.** Paste this prompt:

   ```
   Write standard-library unittest tests in test_buggy_report.py for the documented contract of summarize() in buggy_report.py. Cover combining rows for the same month and product, total_sales rounding, month/product sorting, and rejection of negative units. Do not change buggy_report.py and do not weaken the tests. Run python -m unittest -v and show me the failures; the tests should fail against the intentionally buggy implementation.
   ```

   Then run:

   ```
   /context
   ```

   Notice that the context has moved again. The failing tests are expected.

4. **Fix the bugs and make the tests pass.** Paste this prompt:

   ```
   Now fix only the implementation in buggy_report.py so it satisfies its documented contract. Do not change test_buggy_report.py. Run python -m unittest -v, iterate if needed, and stop only when all tests pass. Summarize the two bugs you found and fixed.
   ```

   Check the context one more time:

   ```
   /context
   ```

5. **Compact it, then measure again:**

   ```
   /compact
   ```
   ```
   /context
   ```

   The context should be visibly smaller. If the first reading after `/compact`
   has not refreshed yet, send a harmless message and run `/context` again.

### Done when

You've seen the grid grow after the script, the failing tests, and the fix; then
you've seen it shrink after `/compact`. The tests failed before the fix and passed
after it.

> **Why it matters.** This is the whole cost conversation in one drill. Nobody
> tunes context with a dial — it falls out of habits like this one: noticing a
> bloated session and compacting it, instead of fighting a confused agent for
> twenty minutes and paying for every round-trip.
>
> Note what `/compact` did to the *conversation*, not just the number: it kept
> the gist and dropped the verbatim. That's why it's the mid-task move and
> `/clear` is the between-tasks move.

> **Claude Code reference.** `/clear` starts a new conversation with empty
> context, `/context` visualizes current context usage, and `/compact` summarizes
> the conversation to free space. See the [commands reference](https://code.claude.com/docs/en/commands).

---

## After the drills

Keep the scratch directory or bin it — it's served its purpose. The three
controls carry forward:

- **`/status` + `/context`** — the glance you take before a big ask. You'll use
  it at the top of every session from here.
- **`/rewind`** — the safety net that lets you step up to Auto Mode in the
  bootstrap exercise later today.
- **`/compact` + `/usage`** — the habit that keeps long sessions sharp. Sessions
  3, 4 and 5 all run long enough to need it.
