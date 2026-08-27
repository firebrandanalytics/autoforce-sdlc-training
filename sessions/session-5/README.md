# Session 5 — Extend the Dashboard, Close the Loop

Autoforce AI Software-Development Training · Session 5 of 5 · hour 1 of the
2-hour slot (hour 2 is the separate Art of the Possible session)

Homework established the starting line: a validated service and a one-table
dashboard skeleton. Today the room grows that skeleton into a small but real web
surface—a month filter, a CSS chart, a JSON API, and tests—then proves the
rendered result still reconciles to the service. The instructor also demonstrates
the final SDLC move: fresh review, merge, and close only what shipped.

If your homework is incomplete, use `starter/` immediately. Continue the
unfinished work afterward; do not give up today's dashboard practice to rebuild
yesterday's setup.

## In this folder

- `LAB-GUIDE.md` — the one-hour lab: launch → contract → parallel build →
  rendered inspection → reconciliation.
- `starter/` — a working one-table FastAPI dashboard and service, so everyone
  shares the same starting line.
- `EXTRA-CREDIT.md` — terminal detail, Claude in Chrome, a Playwright testing
  subagent, deeper tests, documentation, and shipment.

## The hour

1. **Homework receipts + loop-close demo (10 min).** See review, merge, and
   delivered tickets Closed.
2. **Dashboard lab (40 min).** Start the page, pin the contract, split work
   across two subagents, integrate, inspect the browser, reconcile, and test.
3. **Course close + AOP handoff (10 min).** Tie the five sessions together and
   carry unfinished material forward with a precise next action.

## What you leave with

- A rendered dashboard with a month filter and simple volume chart.
- A JSON endpoint over the same service contract.
- Tests and reconciliation evidence that the web layer did not change the
  trusted numbers.
- A clear path to let Claude inspect the rendered browser through Chrome or
  Playwright after class.

## Before the session

- Bring the validated Session 4 core service and completed Homework 3 one-table
  dashboard skeleton—the assumed starting line.
- Pull current course materials with `git pull --ff-only origin main` only from
  a clean course checkout.
- If the dashboard is not running, plan to copy `starter/*` during Step 0.

The governing rule survives the UI: **the app reads through the service, never
the database; a number is right when it reconciles, not when it looks plausible.**
