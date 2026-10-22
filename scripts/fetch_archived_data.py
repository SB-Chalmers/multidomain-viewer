#!/usr/bin/env python3
"""Restore migration inputs from the original immutable source commit."""
import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true', help='Only verify that downloadable files are present and correct.')
args = parser.parse_args()
manifest = json.loads((root / 'migration.json').read_text())
missing = []
for entry in manifest['files']:
    if entry['status'] != 'download':
        continue
    target = root / entry['path']
    if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() == entry['sha256']:
        print('Verified', entry['path'])
        continue
    if args.check:
        missing.append(entry['path'])
        continue
    if target.exists():
        raise SystemExit('Refusing to replace modified file: ' + entry['path'])
    print('Downloading', entry['path'], flush=True)
    target.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(entry['download_url'], timeout=120) as response:
        payload = response.read()
    if hashlib.sha256(payload).hexdigest() != entry['sha256']:
        raise SystemExit('Checksum mismatch: ' + entry['path'])
    temporary = target.with_name(target.name + '.download')
    temporary.write_bytes(payload)
    temporary.replace(target)
if missing:
    raise SystemExit('Missing or modified downloadable files: ' + ', '.join(missing))
