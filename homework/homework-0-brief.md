# Warm-Up — Before Session 2

Autoforce AI Training · do this before **Tuesday, August 18** · **20–30 minutes**

Session 2 is hands-on from the first ten minutes. This warm-up makes sure that
time goes into learning instead of into setup — and it gets the agent's hands on
*your* code before we meet, so the session lands on work you actually care about.

**Three parts. The first one is the one that matters most.**

> **New to the cohort?** You're in the right place — nothing here assumes you
> were at Session 1. Part 2 is the whole of Session 1's idea, and doing it is a
> better introduction than watching it.
>
> **Were you at Session 1 back in June?** It's been a while. Part 2 is the
> re-land, and it takes five minutes.

---

## Part 1 — Prove your setup works (10 min) · **required**

**Do this first, and do it today rather than Monday night.** If something's
broken, we need time to fix it before Tuesday — and a broken install discovered
at 1:05pm on the 18th costs you the whole session's hands-on time.

1. **Open a terminal.** On Windows, use **Git Bash** (not PowerShell or CMD) —
   everything we do assumes bash.
2. **Run `claude`.** It should launch into an interactive prompt.
3. **At the prompt, run these three:**

   ```
   /status
   ```
   ```
   /context
   ```
   ```
   /help
   ```

4. **Write down three things** from that output — you'll want them Tuesday, and
   they tell us what version you're on:
   - the **model** you're on
   - the **approval mode** you're in
   - whether `/context` and `/usage` appear in your `/help` list

### If anything fails

| What happened | Try this |
|---|---|
| `claude: command not found` | It isn't installed, or isn't on your PATH. Reply to the invitation email so it can be routed to whoever handles access at USV — don't burn an evening on it. |
| It launches but errors on auth | Run `/login` and complete the browser sign-in. |
| It launches but `/context` isn't in `/help` | You're on an older build. Run `claude update`, then check again. |
| Anything else | **Run `/doctor`** — it diagnoses install and config problems and can often fix them itself. If it can't, reply to the email with what it said. |

> **Please don't skip this or assume it'll be fine.** Of the survey responses we
> have so far, one person in four doesn't yet have Claude Code access. We would
> much rather sort that out on Friday than on Tuesday.

---

## Part 2 — Point it at something you didn't write (10–15 min) · **required**

This is the actual exercise, and it's the one that makes Tuesday click.

**Pick a repository you work in** — a real one, your own team's. Any language;
C#, SQL, Python, TypeScript, it genuinely doesn't matter. Then:

```bash
cd /path/to/your/repo
claude
```

**Ask it to explain something you didn't write and never fully understood.**
Everyone has one — the stored proc nobody touches, the config nobody can explain,
the job that runs at 3am, the class with a comment that stopped being true three
years ago. Something like:

> *"Read `<file>` and explain what it actually does — not what its name and
> comments claim. Where the behaviour and the comments disagree, tell me which
> one the code actually follows, and show me the lines."*

Or, if nothing specific comes to mind:

> *"Give me a tour of this repository: what it does, how it's laid out, and the
> three things a new engineer here would most likely get wrong."*

**Then push on one answer.** Pick the claim you're least sure about and ask:

> *"How do you know that? Show me the specific lines."*

That second question is the whole course in miniature. **Notice whether the
answer changes when you ask for evidence.**

### Bring one thing to the session

One sentence, on **something the agent told you about your own codebase that you
didn't already know** — or a place where it was confidently wrong and you caught
it. Either one is a great share; the second is arguably better.

We'll open Session 2 with a couple of these. It takes 30 seconds to share, and it
sets up everything we do afterward.

---

## Part 3 — Bring one real task (5 min) · **required**

Session 2 ends with you directing the agent on real work, and your homework after
it runs on a task from your actual backlog. **Come with one in mind.**

If you filled in the pre-training survey, you already named one — use that.
Otherwise, pick something that's:

- **real** — on your actual list, not a toy problem
- **small** — a few hours of work, not a quarter
- **safe** — nothing needing production access you can't sandbox, and nothing
  where a mistake is hard to reverse

Good shapes, drawn from what this cohort actually said in the survey:

- a script that reconciles or compares two sources of data
- reviewing or rewriting a stored procedure whose rules have drifted
- working out which parts of a legacy system are still in real use
- documentation for something that has none
- a test suite for code that's never had one

---

## Stretch — only if you want it

Several of you told us in the survey that you're already past the basics and want
**custom skills** and **agent orchestration**. Those land properly in Sessions 4
and 5, but if you'd like something to chew on before Tuesday:

1. **Ask the agent to write its own instructions.** In your repo, run `/init`. It
   reads the codebase and writes a `CLAUDE.md` — the file it will read at the
   start of every future session there. **Read what it produced and correct it.**
   The corrections are the interesting part: they're the things it couldn't infer
   from the code, which is exactly what that file is for.
2. **Undo something on purpose.** Let it make a change you don't want, then run
   `/rewind` and watch both the code *and* the conversation roll back. We drill
   this Tuesday; arriving having already seen it is a head start.

---

## The short version

- [ ] `claude` launches, and `/status`, `/context`, `/help` all work — **flag problems now, not Tuesday**
- [ ] You pointed it at a repo you work in and asked about something you didn't write
- [ ] You pushed back once with *"how do you know that?"*
- [ ] You have one sentence to share, and one real task in mind

**Total: 20–30 minutes.** If you only have ten, do Part 1.

Questions, or anything broken — reply to the invitation email so it gets to the
right people before Tuesday. The earlier it's raised, the more likely it's fixed
in time.
