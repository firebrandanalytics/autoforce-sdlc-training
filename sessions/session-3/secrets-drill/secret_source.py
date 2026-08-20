#!/usr/bin/env python3
"""Emit a secret for shell capture, simulating a vault CLI's text output.

Do not run this command by itself in an agent session: its stdout is the secret.
Use it only inside command substitution so the shell captures the value and
passes it directly to the consumer command.
"""

import argparse
from pathlib import Path
import sys


parser = argparse.ArgumentParser(description="Emit a stored secret to stdout")
parser.add_argument("--secret-file", default=".app_secret")
args = parser.parse_args()

path = Path(args.secret_file)
if not path.exists():
    sys.exit(f"no secret at {path} — run gen_secret.py first")

sys.stdout.write(path.read_text().strip())
