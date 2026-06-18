#!/usr/bin/env bash
# render.sh — regenerate the MBSE diagram SVGs from the model markdown.
#
# Single source of truth = the Mermaid blocks inside ../0X-*.md (decision Q5-c).
# This script EXTRACTS those blocks and RENDERS them to SVG, organised by
# MagicGrid cell. Re-run after editing any diagram in the model.
#
# Needs: Node (npx) + a headless Chromium (mermaid-cli fetches one).
set -u
cd "$(dirname "$0")" || exit 1
MBSE=".."

command -v npx >/dev/null 2>&1 || { echo "❌ need Node/npx"; exit 1; }
echo '{"args":["--no-sandbox","--disable-setuid-sandbox"]}' > .pptr.json

# (source-file, 0-based block index) -> output path  [MagicGrid cell]
MAP="
02-use-cases.md|0|B2-use-cases/use-case-diagram
03-structure.md|0|B3-system-context/system-context
03-structure.md|1|W3-structure/block-definition
03-structure.md|2|W3-structure/internal-block
04-behavior.md|0|W2-behaviour/wizard-state-machine
04-behavior.md|1|W2-behaviour/a6-export-activity
04-behavior.md|2|W2-behaviour/a10-replace-audio-activity
"

# 1) extract the mermaid blocks into .mmd files at the mapped paths
python3 - "$MBSE" <<'PY'
import sys, re, pathlib
mbse = pathlib.Path(sys.argv[1])
mapping = [l.split("|") for l in """
02-use-cases.md|0|B2-use-cases/use-case-diagram
03-structure.md|0|B3-system-context/system-context
03-structure.md|1|W3-structure/block-definition
03-structure.md|2|W3-structure/internal-block
04-behavior.md|0|W2-behaviour/wizard-state-machine
04-behavior.md|1|W2-behaviour/a6-export-activity
04-behavior.md|2|W2-behaviour/a10-replace-audio-activity
""".strip().splitlines()]
cache = {}
def blocks(fn):
    if fn not in cache:
        text = (mbse/fn).read_text(encoding="utf-8")
        cache[fn] = re.findall(r"```mermaid\n(.*?)```", text, re.S)
    return cache[fn]
for fn, idx, out in mapping:
    b = blocks(fn)
    i = int(idx)
    if i >= len(b):
        print(f"  ⚠️  {fn} has no block #{i}"); continue
    p = pathlib.Path(out + ".mmd"); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(b[i].rstrip() + "\n", encoding="utf-8")
    print(f"  extracted {fn}#{i} -> {p}")
PY

# 2) render each .mmd -> .svg
echo "Rendering SVGs (first run downloads Chromium)…"
ok=0; fail=0
while IFS='|' read -r fn idx out; do
  [ -z "${out:-}" ] && continue
  mmd="$out.mmd"; svg="$out.svg"
  [ -f "$mmd" ] || continue
  if npx -y @mermaid-js/mermaid-cli -p .pptr.json -i "$mmd" -o "$svg" >/dev/null 2>&1; then
    echo "  ✅ $svg"; ok=$((ok+1))
  else
    echo "  ❌ $svg (mermaid render failed)"; fail=$((fail+1))
  fi
done <<EOF
$MAP
EOF
rm -f .pptr.json
echo "Done: $ok ok, $fail failed."
