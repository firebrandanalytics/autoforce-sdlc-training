# Drill — the shell handles the secret; the model does not (8 min)

Autoforce AI Training · Session 3 · run this when your instructor calls it

You've heard the principle: **keep credentials out of the conversation.** Now
prove three common ways to use a secret without pasting or printing its value:

1. a helper reads a secret file directly;
2. the shell stores the value in an environment variable and expands it into an
   argument;
3. command substitution sends a secret-producing command's output straight into
   an argument.

The scripts use only the Python standard library. On Windows, substitute
`python` or `py` for `python3` if needed.

---

## Before you start

Work in this directory with Claude Code in **Manual** mode so you see every
command before it runs. Reject any command that reads `.app_secret`, runs
`secret_source.py` by itself, prints `DEMO_SECRET`, or enables shell tracing.

> **The boundary:** these patterns keep the value out of the prompt and normal
> command output. They do not stop an agent with approved shell access from
> deliberately running `cat`, `printenv`, or the secret-producing command. Your
> approval boundary still matters.

## 1 — A helper reads the file (about 2 min)

Ask the agent:

> Run `gen_secret.py` in this directory, then run
> `use_secret.py --sign 2025-08`. Tell me what each command returned without
> reading or printing `.app_secret`.

You should see a confirmation, signature, and fingerprint—but no secret:

```text
wrote .app_secret (43 chars). The value was never printed.
signed '2025-08' -> 4f2a...
secret loaded ok (fingerprint 9c1d...). The value was never printed.
```

The helper opened the file. The model received only safe output.

## 2 — Environment variable expanded into an argument (about 2 min)

Some commands insist on `--token VALUE`. Ask the agent to run this as **one shell
command** so the temporary variable is created, consumed, and unset together:

```bash
set +x; export DEMO_SECRET="$(python3 secret_source.py)"; python3 arg_consumer.py --secret "$DEMO_SECRET" --sign 2025-08; unset DEMO_SECRET
```

The assignment prints nothing. The shell expands `$DEMO_SECRET` only when it
launches `arg_consumer.py`, which prints a signature and fingerprint—not the
value. `set +x` makes sure shell tracing cannot echo expanded arguments.

## 3 — Command output substituted directly (about 2 min)

Now skip the named variable and capture the producer's stdout directly:

```bash
set +x; python3 arg_consumer.py --secret "$(python3 secret_source.py)" --sign 2025-08
```

This is the shape of a real vault command whose output is fed directly to a
consumer. **Never run `secret_source.py` by itself in the agent session**: its
stdout is intentionally the secret, so a direct run would put the value in the
transcript.

## Compare the three (about 2 min)

Ask the agent, without approving any new command:

> Based only on the output already returned, what was the secret value? Compare
> how the file helper, environment variable, and command substitution kept it
> out of the conversation.

The answer should be that it cannot recover the value from the signatures or
fingerprints. The teaching line is:

> **The shell may handle the value; the model does not need to.**

---

## Where `jq` fits in real work

Vault and cloud CLIs often return JSON. If `jq` is available, the producer inside
command substitution commonly looks like:

```bash
some-vault-command --output json | jq -r '.value'
```

You would place that pipeline inside `$(...)` rather than run it by itself. This
drill uses `secret_source.py` so nobody needs `jq`; think of it as the already-
extracted text output of the vault command.

## Important limitation of argument-based secrets

Even when the model never sees the value, a secret passed as `--secret VALUE`
can be visible to other local processes through the operating system's process
list or diagnostic logging. Prefer, in order:

1. a helper or client that reads a protected file, stdin, or file descriptor;
2. a tool-supported environment variable;
3. argument expansion only when the command offers no safer interface.

This exercise demonstrates how to avoid **conversation leakage** when an
argument is unavoidable; it does not make command-line arguments private.

## Done when

- All three patterns produced the same fingerprint.
- The secret itself never appeared in the transcript.
- You can explain why directly running the producer, `cat`, `printenv`, or shell
  tracing would break the boundary.

**Clean up:** delete `.app_secret` or leave it for the instructor's reset script;
it is a throwaway file and is gitignored.
