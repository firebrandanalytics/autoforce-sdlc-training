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
context is, or what mode you're in. Three commands answer all of it.

### Do this

1. In a terminal, in any directory, run `claude`.
2. At the `>` prompt, run each of these and *read the output*:

   ```
   /status
   ```
   ```
   /context
   ```

3. Answer these three questions out loud (or in the chat):
   - **Which model** are you on right now?
   - **Which approval mode** are you in?
   - Roughly **how full** is your context — a sliver, or half the grid?

### Done when

You can state your model, your mode, and your context usage without guessing.

> **Why it matters.** Every lever we cover in the next hour — mode, model,
> context — is one you can only pull deliberately if you can *see* where it's
> set. This is the dashboard. Glance at it before any big ask.

---

## Drill 2 — `/rewind`: approve, regret, undo (7 min)

**When:** during the approval-modes beat.
**The idea:** the reason you can afford to let the agent run is that you can take
it back. `/rewind` rolls the **code and the conversation** back to a checkpoint.

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

   Pick the checkpoint from before step 3. Then check what happened:
   `! ls` and `! cat notes.md`.

### Done when

`notes.md` is back to your three bullets, the extra files are gone — **and** the
agent doesn't reference the rewritten version when you ask it what's in the file.
That second part is the one people miss: the conversation rolled back too.

> **Why it matters.** Every approval you give is a bet on how hard the mistake
> would be to undo. `/rewind` makes a whole class of mistakes cheap, which is
> what lets you work in a faster mode than you otherwise would.
>
> **And know its edges.** It does not reach anything already pushed, deployed, or
> run against a real system. Those still get Manual mode and `Ctrl+E`.

---

## Drill 3 — Watch your working memory and your bill move (6 min)

**When:** during the context and model-selection beat.
**The idea:** context and cost are measurable, not vibes. You're about to watch
both of them move in response to something you did.

### Do this

1. Stay in the same session as Drill 2 (you want some history in it).
2. Take a **baseline**:

   ```
   /context
   ```
   ```
   /usage
   ```

   Note roughly how much of the grid is filled, and what the session has cost so
   far.

3. **Fill it up.** Give the agent something that reads a lot:

   > *"Read every file in this directory, then summarise what this project is
   > and what you'd add next."*

4. Take the reading again — `/context`, then `/usage`. The grid should be
   visibly fuller and the number visibly bigger.

5. **Compact it, then measure again:**

   ```
   /compact
   ```
   ```
   /context
   ```

### Done when

You've seen the grid grow and then shrink, and you can say roughly what this
session has cost you.

> **Why it matters.** This is the whole cost conversation in one drill. Nobody
> tunes cost with a dial — it falls out of habits like this one: noticing a
> bloated session and compacting it, instead of fighting a confused agent for
> twenty minutes and paying for every round-trip.
>
> Note what `/compact` did to the *conversation*, not just the number: it kept
> the gist and dropped the verbatim. That's why it's the mid-task move and
> `/clear` is the between-tasks move.

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
