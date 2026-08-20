# Homework #1 — Finish Your Project + Learn a Shell Trick

**Assigned after:** Session 2
**Due before:** Session 3
**Time budget:** 30–45 minutes

---

## The assignment

We completed the log hunt together during Session 2. The 35-minute project build
became homework instead, so Homework #1 has two connected parts:

1. **Finish the small project you started.** Use the real task you brought from
   work, or one of the suggested alternatives in
   [`sessions/session-2/HANDS-ON-bootstrap.md`](../sessions/session-2/HANDS-ON-bootstrap.md).
   Direct Claude Code to build it; review and steer rather than writing the files
   yourself.
2. **Turn the agent into a command-line tutor while you work.** Inspect the shell
   commands it proposes and ask it to explain one technique you do not know.

The project does not need to be ambitious. A small working result with a README
and a passing test is better than a large unfinished idea.

## Finish line for the project

Use the checklist from the Session 2 guide. At minimum, bring:

- a small project that runs;
- at least one automated test that passes;
- a short README explaining what it does and how to run it;
- one example of something you reviewed, corrected, or asked the agent to change.

If you did not bring a work task, choose `fuel-units`, `terminal-totals`, or
`notes` from the guide. Any of them fully satisfies the assignment.

## Learn one shell technique along the way

Keep Claude Code in **Manual** mode so it pauses and shows you commands before it
runs them. Read the command; use **Ctrl+E** if the approval view is collapsed;
then ask:

> Explain this command piece by piece. What does each part do, and when would I
> use this technique again?

Look for a reusable technique rather than a single flag—for example:

- a multi-stage pipe such as `sort | uniq -c | sort -rn`;
- a regular-expression construct;
- shell expansion such as `${name%.txt}`;
- redirecting output with `>`, `2>&1`, or a pipe;
- a useful `git`, `find`, `curl`, or package-manager command.

If your project does not naturally surface an interesting command, ask the agent
to show the largest files in the project, count common words in the README, or
find every TODO—and then explain the command it uses.

## What to bring to Session 3

Be ready with two short share-backs:

1. **Your project:** what you asked the agent to build, whether you used a real
   work problem or the suggested alternative, and one thing that worked or
   required your review.
2. **Your shell technique:** what it does and when you would reuse it.

Wins, incomplete attempts, and frustrations are all useful evidence. The point
is the operating practice: you directed, the agent executed, and you owned the
result.

---

*Reference cards: **CC — Claude Code Commands** and **C5 — Approval Modes**.*
