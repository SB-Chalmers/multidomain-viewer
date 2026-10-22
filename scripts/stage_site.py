#!/usr/bin/env python3
"""Stage only the viewer runtime files for static hosting."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
site = root / '_site'
if site.exists():
    shutil.rmtree(site)
site.mkdir()
for name in ('index.html', 'main.js', '.nojekyll'):
    shutil.copy2(root / name, site / name)
for name in ('src', 'libs', 'resources', 'data'):
    shutil.copytree(root / name, site / name)
print(f'Staged viewer at {site}')
