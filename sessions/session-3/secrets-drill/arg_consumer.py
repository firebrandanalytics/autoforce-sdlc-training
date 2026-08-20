#!/usr/bin/env python3
"""Consume a secret supplied as a command argument without printing it."""

import argparse
import hashlib
import hmac


parser = argparse.ArgumentParser(description="Use a secret supplied as an argument")
parser.add_argument("--secret", required=True)
parser.add_argument("--sign", required=True)
args = parser.parse_args()

fingerprint = hashlib.sha256(args.secret.encode()).hexdigest()[:12]
signature = hmac.new(
    args.secret.encode(), args.sign.encode(), hashlib.sha256
).hexdigest()

print(f"signed {args.sign!r} -> {signature}")
print(
    f"argument secret consumed ok (fingerprint {fingerprint}). "
    "The value was never printed."
)
