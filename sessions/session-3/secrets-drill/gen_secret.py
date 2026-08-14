#!/usr/bin/env python3
"""
gen_secret.py — write a strong random secret into a file the agent's LLM never reads.

The agent RUNS this command; it prints only a confirmation, never the secret value.
The value exists only in the output file (which you gitignore). Cross-platform:
pure Python standard library — no shell tools (openssl/uuidgen), no network — so it
behaves identically on Windows, macOS, and Linux.

    python gen_secret.py                 # -> writes .app_secret, prints a confirmation
    python gen_secret.py --out .db_pw    # custom file
"""
import argparse
import pathlib
import secrets

ap = argparse.ArgumentParser(description="Write a random secret to a file (value never printed).")
ap.add_argument("--out", default=".app_secret", help="file to write the secret into")
ap.add_argument("--bytes", type=int, default=32, help="entropy in bytes (default 32)")
args = ap.parse_args()

path = pathlib.Path(args.out)
path.write_text(secrets.token_urlsafe(args.bytes))
try:
    path.chmod(0o600)  # owner-only; harmless/no-op on Windows
except Exception:
    pass

# Note what we did, NOT what we wrote. The secret never reaches stdout.
print(f"wrote {path} ({path.stat().st_size} chars). The value was never printed.")
