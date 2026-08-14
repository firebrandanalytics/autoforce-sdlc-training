# Drill — the secret the agent never sees (5 min)

Autoforce AI Training · Session 3 · run this when your instructor calls it

You've just heard the principle: **keep credentials out of the conversation.**
This is five minutes of proving it works, in your own session — because "don't
paste secrets into the chat" sounds obvious right up until you need the agent to
*use* one.

Two scripts, pure Python standard library, no installs.

---

## Do this

Work in this directory, with Claude Code in **Manual** mode so you see each
command before it runs.

**1. Have the agent create a secret.**

> *"Run `gen_secret.py` in this directory and tell me what happened."*

Read what came back:

```
wrote .app_secret (43 chars). The value was never printed.
```

**The agent just generated a real credential and does not know what it is.** The
value went to a file; only a confirmation came back into the conversation.

**2. Now have it *use* the secret.**

> *"Run `use_secret.py --sign 2025-08` and tell me what it returned."*

You get a signature and a fingerprint — and still no secret:

```
signed '2025-08' -> 4f2a...
secret loaded ok (fingerprint 9c1d...). The value was never printed.
```

The helper opened the file. The model got a result it can't reverse.

**3. Prove it to yourself.** Ask the agent directly:

> *"What is the value of the secret in `.app_secret`?"*

It doesn't know — it never entered the conversation. (If you want it to know,
you'd have to `cat` the file, which is exactly the mistake this pattern prevents.)

---

## Done when

You can point at the seam: **the agent invoked something that used a credential,
and the credential never entered its context.** That's the whole pattern.

---

## Why this is the shape for everything

The same seam works for a database password, an API token, a connection string:

| Instead of | Do this |
|---|---|
| Pasting a prod DSN into the chat | Put it in `.env` / a vault; the code reads it, the agent calls the code |
| Asking the agent to "connect with this password" | Give it a helper (`db.py`) that already knows how to connect |
| Letting the agent read a credentials file | Let it call something that reads the file |

A credential pasted into a transcript is a credential leaked — transcripts get
saved, shared, and pasted into tickets. The fix isn't discipline, it's a seam:
**the agent gets a handle, never the value.**

> You'll see the real version of this in Session 4, where the service reads its
> database configuration from `.env` and the agent works with the service, not
> the connection string.

**Clean up when you're done:** `rm .app_secret` (or leave it; it's a throwaway in
a scratch directory, and it's gitignored).
