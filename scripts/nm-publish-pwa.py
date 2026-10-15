#!/usr/bin/env python3
"""Publish The National Measure manuscript bytes into the boundary-universe PWA worktree.

Copies chapter-01..chapter-NN from the source book into the PWA's public manuscript folder
(exact bytes), regenerates the kindling-2680-book-02 entry of src/lib/manuscript-index.ts,
updates the shelf entry in src/lib/catalog.ts, bumps app version/build, writes a new service
worker file and its no-store header. Does not commit or push.

usage: nm-publish-pwa.py --through 24 --subtitle "..." --description "..." --note "..." --slug "..."
"""
import argparse, json, re, shutil, sys
from pathlib import Path

BOOK = Path("/Users/drive/kindling-2680-book-02/books/book-2680-national-measure/manuscript")
PWA = Path("/Users/drive/boundary-universe-2680-publish")
DEST = PWA / "public/manuscripts/books/book-2680-national-measure/manuscript"
BOOK_ID = "kindling-2680-book-02"

ap = argparse.ArgumentParser()
ap.add_argument("--through", type=int, required=True)
ap.add_argument("--subtitle", required=True)
ap.add_argument("--description", required=True)
ap.add_argument("--note", required=True)
ap.add_argument("--slug", required=True, help="build slug, e.g. national-measure-chapters-01-16-r2")
ap.add_argument("--label", required=True)
ap.add_argument("--date", default="2026.10.15")
ap.add_argument("--released", default="15 October 2026")
a = ap.parse_args()

# 1. exact bytes
DEST.mkdir(parents=True, exist_ok=True)
changed = []
for n in range(1, a.through + 1):
    src = BOOK / f"chapter-{n:02d}.md"
    dst = DEST / src.name
    if not src.exists():
        sys.exit(f"missing source {src}")
    if not dst.exists() or dst.read_bytes() != src.read_bytes():
        shutil.copyfile(src, dst)
        changed.append(src.name)
print("copied/changed:", changed)

# 2. manuscript index
entries = []
for n in range(1, a.through + 1):
    head = (DEST / f"chapter-{n:02d}.md").read_text(encoding="utf-8").splitlines()[0]
    m = re.match(r"#\s*Chapter\s+\d+\s*[—-]\s*(.+)$", head)
    if not m:
        sys.exit(f"cannot parse title of chapter {n}: {head!r}")
    entries.append({"number": n, "title": m.group(1).strip(),
                    "path": f"books/book-2680-national-measure/manuscript/chapter-{n:02d}.md"})
body = json.dumps(entries, indent=2, ensure_ascii=False)
body = "\n".join(("  " + l if i else l) for i, l in enumerate(body.splitlines()))
idx_p = PWA / "src/lib/manuscript-index.ts"
idx = idx_p.read_text(encoding="utf-8")
pat = re.compile(r'  "kindling-2680-book-02": \[.*?\n  \],\n', re.S)
if not pat.search(idx):
    sys.exit("index entry not found")
idx = pat.sub(lambda m: f'  "{BOOK_ID}": {body},\n', idx, count=1)
idx_p.write_text(idx, encoding="utf-8")

# 3. catalog shelf entry
cat_p = PWA / "src/lib/catalog.ts"
cat = cat_p.read_text(encoding="utf-8")
blk = re.search(r'(id: KINDLING_2680_BOOK_TWO_ID,.*?\n  \},)', cat, re.S)
if not blk:
    sys.exit("catalog entry not found")
b = blk.group(1)
b2 = re.sub(r'subtitle: ".*?",', lambda m: f'subtitle: {json.dumps(a.subtitle, ensure_ascii=False)},', b, count=1)
b2 = re.sub(r'totalChapters: \d+,', f'totalChapters: {a.through},', b2, count=1)
b2 = re.sub(r'description:\n\s+".*?",\n', lambda m: f'description:\n      {json.dumps(a.description, ensure_ascii=False)},\n', b2, count=1, flags=re.S)
cat = cat.replace(b, b2, 1)
cat_p.write_text(cat, encoding="utf-8")

# 4. app update metadata
au_p = PWA / "src/lib/app-update.ts"
au = au_p.read_text(encoding="utf-8")
ver = re.search(r'APP_VERSION = "(\d+)\.(\d+)\.(\d+)"', au)
newver = f"{ver.group(1)}.{ver.group(2)}.{int(ver.group(3)) + 1}"
build = f"{a.date}-{a.slug}"
sw_old = int(re.search(r"/sw-v(\d+)\.js", au).group(1))
sw_new = sw_old + 1
au = re.sub(r'APP_BUILD = ".*?";', f'APP_BUILD = "{build}";', au, count=1)
au = re.sub(r'APP_VERSION = ".*?";', f'APP_VERSION = "{newver}";', au, count=1)
au = re.sub(r'APP_RELEASED = ".*?";', f'APP_RELEASED = "{a.released}";', au, count=1)
au = au.replace("export const APP_NOTES = [\n", f"export const APP_NOTES = [\n  {json.dumps(a.note, ensure_ascii=False)},\n", 1)
au = au.replace(f"/sw-v{sw_old}.js", f"/sw-v{sw_new}.js", 1)
au_p.write_text(au, encoding="utf-8")

# 5. version.json
vj = PWA / "public/version.json"
vj.write_text(json.dumps({"build": build, "version": newver, "label": a.label}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 6. service worker file + header
old_sw = PWA / f"public/sw-v{sw_old}.js"
new_sw = PWA / f"public/sw-v{sw_new}.js"
txt = old_sw.read_text(encoding="utf-8")
txt = re.sub(r'const VERSION = ".*?";', f'const VERSION = "{build}";', txt, count=1)
new_sw.write_text(txt, encoding="utf-8")
vp = PWA / "vercel.json"
v = vp.read_text(encoding="utf-8")
hdr = f'    {{\n      "source": "/sw-v{sw_new}.js",\n      "headers": [{{ "key": "Cache-Control", "value": "no-store" }}]\n    }},\n'
v = v.replace('  "headers": [\n', '  "headers": [\n' + hdr, 1)
vp.write_text(v, encoding="utf-8")
print(json.dumps({"version": newver, "build": build, "sw": f"sw-v{sw_new}.js", "changed": changed}))
