#!/usr/bin/env python3
"""
use_secret.py — USE the secret without ever exposing it.

This is the seam: the agent calls this helper; the helper reads the secret file;
the value never enters the conversation. The only thing printed is non-reversible
proof that it worked (a fingerprint, or an HMAC signature) — never the secret.

    python use_secret.py                       # prove the secret loads
    python use_secret.py --sign "2025-08"      # real use: HMAC-sign a value with it
"""
import argparse
import hashlib
import hmac
import pathlib
import sys

ap = argparse.ArgumentParser(description="Use the app secret without revealing it.")
ap.add_argument("--secret-file", default=".app_secret")
ap.add_argument("--sign", help="a value to HMAC-sign with the secret (a real use)")
args = ap.parse_args()

p = pathlib.Path(args.secret_file)
if not p.exists():
    sys.exit(f"no secret at {p} — run gen_secret.py first")

secret = p.read_text().strip()            # read by THIS process — not by the LLM

fingerprint = hashlib.sha256(secret.encode()).hexdigest()[:12]
if args.sign:
    sig = hmac.new(secret.encode(), args.sign.encode(), hashlib.sha256).hexdigest()
    print(f"signed {args.sign!r} -> {sig}")   # reveals nothing about the secret itself
print(f"secret loaded ok (fingerprint {fingerprint}). The value was never printed.")
