#!/usr/bin/env bash
# render.sh — regenerate podcast model-map SVGs from the Mermaid blocks in
# ../01-systems-engineering/09-model-map.md. Needs Node (npx) + headless Chromium.
set -u
cd "$(dirname "$0")" || exit 1
SRC="../01-systems-engineering/09-model-map.md"
command -v npx >/dev/null 2>&1 || { echo "❌ need Node/npx"; exit 1; }
SHELL_BIN=$(find "${PUPPETEER_CACHE_DIR:-$HOME/.cache/puppeteer}" -name chrome-headless-shell -type f 2>/dev/null | head -1)
if [ -z "$SHELL_BIN" ]; then
  echo "… fetching chrome-headless-shell (one-time)"
  npx -y puppeteer browsers install chrome-headless-shell >/dev/null 2>&1
  SHELL_BIN=$(find "${PUPPETEER_CACHE_DIR:-$HOME/.cache/puppeteer}" -name chrome-headless-shell -type f 2>/dev/null | head -1)
fi
if [ -n "$SHELL_BIN" ]; then
  printf '{"executablePath":"%s","args":["--no-sandbox","--disable-setuid-sandbox"]}\n' "$SHELL_BIN" > .pptr.json
else
  echo '{"args":["--no-sandbox","--disable-setuid-sandbox"]}' > .pptr.json
fi

# block index -> output name
NAMES="01-lifecycle 02-traceability-spine 03-stakeholder-groups 04-trade-study 05-cross-layer-bridge"

python3 - "$SRC" "$NAMES" <<'PY'
import sys, re, pathlib
src = pathlib.Path(sys.argv[1]); names = sys.argv[2].split()
blocks = re.findall(r"```mermaid\n(.*?)```", src.read_text(encoding="utf-8"), re.S)
for i, name in enumerate(names):
    if i >= len(blocks): print(f"  ⚠️  no block #{i} for {name}"); continue
    p = pathlib.Path(name + ".mmd"); p.write_text(blocks[i].rstrip()+"\n", encoding="utf-8")
    print(f"  extracted block #{i} -> {p}")
PY

ok=0; fail=0
for name in $NAMES; do
  [ -f "$name.mmd" ] || continue
  if npx -y @mermaid-js/mermaid-cli -p .pptr.json -i "$name.mmd" -o "$name.svg" >/dev/null 2>&1; then
    echo "  ✅ $name.svg"; ok=$((ok+1))
  else echo "  ❌ $name.svg"; fail=$((fail+1)); fi
done
rm -f .pptr.json
echo "Done: $ok ok, $fail failed."
