# Lab Guide: Extend the Dashboard — Session 5

Autoforce AI Software-Development Training · Session 5 (hour 1; the second hour
is the separate Art of the Possible session)

Today assumes the homework did its job: your Session 4 service is validated and
your Homework 3 dashboard skeleton renders one table. **We are moving forward
together.** If either artifact is unfinished, that is useful work to continue
after class; use the committed starter for today's lab so you can still practice
the new move.

The instructor will demonstrate the final SDLC close—fresh review, merge, and
delivered tickets Closed. Your keyboard time then extends the dashboard against
the service contract: a month picker, a simple chart, and a JSON API, followed
by an end-to-end reconciliation.

---

## How the hour runs

| Elapsed | What's happening |
|---:|---|
| 0–5 | Homework receipts: what worked, what you challenged, what a gate caught |
| 5–10 | **Demo:** fresh review → merge → delivered tickets Closed |
| **10–15** | **Your keyboard:** launch the dashboard skeleton |
| **15–20** | **Your keyboard:** confirm the app/service contract |
| **20–35** | **Your keyboard:** two subagents extend independent surfaces |
| **35–45** | **Your keyboard:** integrate and inspect the rendered app |
| **45–50** | **Your keyboard:** reconcile and run the tests |
| 50–58 | The five-session loop, tied together + stretch paths |
| 58–60 | Handoff to the separate Art of the Possible session |

If the clock reaches the next checkpoint before your agent does, leave the work
in a coherent state, write the next action down, and keep going after the
session. The clock protects the lesson; it does not define when your project is
finished.

---

## Step 0 — Launch the skeleton (~5 min)

Work where Homework 3 left you:

```bash
cd autoforce-sdlc-training
git pull --ff-only origin main
cd sessions/session-5
export DB_PATH=../../data/autoforce.sqlite
```

If your Homework 3 dashboard is here, keep it. If it is not running, take the
safety net rather than spending the lab rebuilding setup:

```bash
cp -r starter/* .
python3 -m pip install -r requirements.txt
```

Start the server in one terminal:

```bash
uvicorn app:app --reload
```

Open `http://localhost:8000`. You should see the latest month's table. In a
second terminal, start Claude Code in this same folder:

```bash
claude
```

**Checkpoint 0:** page visible; no stack trace; the table has real terminals and
volumes. If not, use the starter now and diagnose your original afterward.

---

## Step 1 — Pin the contract (~5 min)

The service and app can evolve independently only if they agree on the seam.
Paste this prompt:

```text
Read service.py and app.py. Before changing code, write CONTRACT.md: the exact
row shape the service returns and the app consumes. Include the five fields and
types (terminal, month, physical_gal, taxable_gal, lift_count), the meaning of
each measure, the invariants, and the functions that produce the rows
(monthly_volumes and months). Confirm that app.py reads through the service and
never queries SQLite. Keep it readable in 30 seconds. Do not write code yet.
```

Read the result. It must pin:

- `physical_gal >= taxable_gal >= 0`;
- `lift_count >= 1`;
- one row per `(terminal, month)`;
- `terminal` resolves to a real terminal;
- the app calls `service.monthly_volumes()` and `service.months()`—no SQL in the
  app or templates.

**Checkpoint 1:** `CONTRACT.md` is specific enough that two agents can work
without inventing different field names or business rules.

---

## Step 2 — Split the build (~15 min)

Now delegate independent surfaces against that contract. Paste:

```text
Use two subagents to extend this dashboard in parallel. Both must read and honor
CONTRACT.md. Neither may query SQLite directly.

SUBAGENT A — RENDERED MAIN VIEW
- Add a month dropdown to GET / using service.months().
- Default to the latest month; changing it reloads the page with ?month=YYYY-MM.
- Keep the table and add a simple horizontal CSS bar for physical_gal relative
  to the largest terminal in the selected month. No JavaScript chart library.

SUBAGENT B — API + TESTS
- Add GET /api/volumes?month=YYYY-MM returning the same service rows as JSON.
- Add focused FastAPI TestClient tests: GET / and the API return 200; the API's
  2025-08 DAL row matches 1,517,103 physical and 1,371,642 taxable; every API
  row honors the contract invariants.

Integrate both results. Report which files each subagent changed and any
conflict you resolved. Stop before starting the server or changing the service.
```

While they work, watch for the useful failures:

- `sqlite3.connect` appears in `app.py`: reject it; the app crossed the seam.
- One side writes `physical` while the contract says `physical_gal`: point it
  back to `CONTRACT.md`.
- Empty rows cause division by zero: use `max(..., default=1)` or equivalent.
- Both agents edit `app.py`: integration is expected. The contract makes the
  disagreement small enough to resolve deliberately.

**Checkpoint 2:** the diff contains the filter, CSS bars, JSON route, and tests;
the service's business logic is unchanged.

---

## Step 3 — Integrate and inspect the rendered app (~10 min)

Review the diff before running it:

```text
Show me the integrated diff grouped by contract, main-view behavior, API, and
tests. Flag any database access outside service.py and any field name that does
not match CONTRACT.md. Do not fix anything until I approve the review.
```

Then restart or let `uvicorn --reload` refresh. Inspect it as a user:

- Select two different months. The heading, table, and bars should all change.
- Confirm bar lengths track the physical-volume values without replacing the
  exact numbers.
- Open `http://localhost:8000/api/volumes?month=2025-08` and confirm it returns
  JSON rows with all five contract fields.
- Check the terminal for template errors and the browser console for errors.

Human eyes are the required check in class. The stretch guide adds two ways to
let Claude inspect the actual rendered browser too: the Claude in Chrome
extension and a Playwright browser-testing subagent.

**Checkpoint 3:** the UI works at two months, the API returns rows, and rendered
behavior—not just source code—has been inspected.

---

## Step 4 — Reconcile and test (~5 min)

A prettier wrong number is still wrong. Run:

```bash
python3 -m pytest -q
python3 -c "import service; print(next(r for r in service.monthly_volumes('2025-08') if r['terminal'] == 'DAL'))"
curl -s "http://localhost:8000/api/volumes?month=2025-08"
```

For DAL in `2025-08`, both the service and API must show:

- `physical_gal`: **1,517,103**
- `taxable_gal`: **1,371,642**
- `lift_count`: **184**

If the UI or API disagrees with the service, fix the consumer. Do not duplicate
or "correct" the service logic from inside the web layer.

**Done gate:** month filter works; CSS bars render; JSON API works; tests pass;
DAL reconciles; no database access exists outside `service.py`.

---

## If you finish early—or continue afterward

Open `EXTRA-CREDIT.md`. The next useful moves are:

1. a terminal-detail page across all months;
2. Claude in Chrome inspecting the rendered localhost app, console, and user
   flow;
3. a reusable Playwright browser-testing subagent;
4. stronger accessibility, visual, route, and reconciliation tests;
5. documentation and the same clean-context review → merge → ticket-close loop
   the instructor demonstrated.

Anything the room does not finish is now a well-scoped continuation, not a
failed exercise. Keep `CONTRACT.md`, the test output, and your written next
action; resume from evidence rather than memory.
