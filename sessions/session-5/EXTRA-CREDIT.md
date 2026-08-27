# Stretch: Finish, Inspect, and Harden the Dashboard

Use this after the timed Session 5 lab—or immediately if you finish early. The
clock may stop; the project does not. Start from whatever is true in your folder
and complete the next coherent move.

The core target is:

- month filter;
- CSS volume bars;
- `GET /api/volumes`;
- tests and the DAL reconciliation anchor;
- no database access outside `service.py`.

Finish any missing core item first. Then choose one or more stretches below.

---

## Stretch 1 — Add a terminal-detail page (~15–25 min)

Build `GET /terminal/{terminal}`: one terminal across all months, ordered by
month, with exact physical and taxable numbers. Link terminal names in the main
table to the detail page.

```text
Read CONTRACT.md and the current dashboard. Add GET /terminal/{terminal} and a
terminal-detail template showing that terminal across all months. The route must
read through service.monthly_volumes(), never SQLite. Link terminal names in the
main table to the page. Add route and not-found tests. Review the diff before
running it.
```

Done means `/terminal/DAL` renders all 12 months and the existing dashboard/API
tests remain green.

---

## Stretch 2 — Let Claude inspect the rendered app in Chrome (~10–20 min)

Source review cannot tell you whether a dropdown is awkward, a bar is invisible,
or the browser console is red. Connect Claude Code to the visible browser and
make rendered behavior part of the evidence.

### Prerequisites

- Google Chrome or Microsoft Edge;
- the **Claude in Chrome** extension installed and enabled;
- current Claude Code and a direct Anthropic plan that supports the integration;
- your local server running at `http://localhost:8000`.

In Claude Code:

```text
/chrome
```

Connect or reconnect the extension and grant access only to the site you intend
to test. Then paste:

```text
Use Chrome to review the rendered dashboard at http://localhost:8000. Do not
change code yet.

1. Load the main page and report the selected/default month.
2. Change to two other months and verify the heading, rows, and CSS bars change
   together.
3. Check that exact numeric values remain readable and that bar lengths roughly
   track physical_gal.
4. Open /api/volumes?month=2025-08 and confirm it returns JSON with the five
   CONTRACT.md fields.
5. If the terminal-detail stretch exists, open /terminal/DAL and verify the
   month ordering and navigation back to the dashboard.
6. Inspect the browser console for errors and the page for obvious overflow,
   missing labels, poor contrast, or unusable controls.

Write BROWSER-REVIEW.md with PASS/FAIL for each check, screenshots or a short GIF
if useful, and at most three prioritized findings. Wait for my approval before
fixing anything.
```

Review the report, approve only real findings, let Claude fix them, then ask it
to repeat the same browser pass. The point is the loop: **render → observe → fix
→ re-observe**, not merely “the HTML looks plausible.”

> Chrome uses the browser's current session and visible tabs. Treat site
> permissions as real access: use localhost for this exercise and do not grant
> unrelated sites or expose credentials just to make the demo work.

---

## Stretch 3 — Create a reusable Playwright browser tester (~25–40 min)

Chrome is excellent for an immediate visible review. Playwright is the next step
when you want the same browser rubric to be reusable and automatable.

This path requires Node.js/npm because the browser agent launches the Playwright
MCP package with `npx`. Create `.claude/agents/browser-tester.md`:

```markdown
---
name: browser-tester
description: Tests the rendered dashboard in a real browser and reports evidence before suggesting fixes
mcpServers:
  - playwright:
      type: stdio
      command: npx
      args: ["-y", "@playwright/mcp@latest"]
---

You are the browser reviewer, not the feature author. Read CONTRACT.md and the
acceptance criteria, then use Playwright to exercise the visible application.
Check navigation, controls, rendered values, console errors, and obvious
accessibility problems. Capture screenshots for failures. Write a concise
BROWSER-REVIEW.md with PASS/FAIL evidence and at most three prioritized
findings. Do not edit application code unless the user explicitly approves a
finding.
```

Start a fresh Claude Code session so the new project agent is loaded, run the
server, and ask:

```text
Use the browser-tester agent to inspect http://localhost:8000. Exercise the
month filter, the 2025-08 API, and the terminal-detail page if present. Verify
the DAL values against CONTRACT.md, check the console, and save screenshots for
any failure. Return the report without changing code.
```

Then inspect `.claude/agents/browser-tester.md` like code. The reusable value is
the standard: everyone on the project gets the same browser review when the
agent file is committed.

---

## Stretch 4 — Strengthen the quality gates (~20–35 min)

Ask the agent to add only tests that can fail for a meaningful reason:

```text
Strengthen test_app.py without duplicating implementation details. Add:
- GET /, /terminal/DAL (if present), and /api/volumes?month=2025-08 return 200;
- the API's DAL row matches 1,517,103 physical, 1,371,642 taxable, and 184 lifts;
- every API row honors physical >= taxable >= 0 and lift_count >= 1;
- the selected month is preserved in the rendered page;
- every main-table terminal link resolves;
- an unknown terminal gets a deliberate 404 or an explicit empty state.
Run the tests and explain which real regression each test catches.
```

Optional accessibility pass:

- every form control has a label;
- keyboard focus is visible;
- tables have headers and meaningful captions;
- color is not the only carrier of meaning;
- the CSS bars do not hide the exact numeric values.

---

## Stretch 5 — Document and ship it (~15–25 min)

Add a short README covering:

- what the dashboard shows;
- the app/service contract and why the app never queries the database;
- setup and `DB_PATH`;
- routes and example URLs;
- tests and reconciliation anchors;
- optional Chrome and Playwright browser-review workflows.

Then close the same loop demonstrated in class:

1. fresh-context review against the contract and stories;
2. tests and browser evidence re-run by the reviewer;
3. commit and PR approved;
4. merge;
5. close only the dashboard tickets that actually shipped.

Anything left is backlog, not failure. Record the next action precisely enough
that a fresh session can resume from the artifacts rather than from memory.

---

Official references:

- [Use Claude Code with Chrome](https://code.claude.com/docs/en/chrome)
- [Create custom subagents, including a Playwright MCP agent](https://code.claude.com/docs/en/sub-agents)
