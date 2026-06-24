#!/usr/bin/env bash
# render.sh — regenerate podcast model SVGs from the Mermaid blocks in the
# 01-systems-engineering/*.md model files. Needs Node (npx) + headless Chromium.
set -u
cd "$(dirname "$0")" || exit 1
SE="../01-systems-engineering"
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

ok=0; fail=0
# render_src <source.md> <name0> <name1> …  — extract the i-th mermaid block to <namei>.svg
render_src() {
  local src="$1"; shift
  local names="$*"
  python3 - "$src" "$names" <<'PY'
import sys, re, pathlib
src = pathlib.Path(sys.argv[1]); names = sys.argv[2].split()
blocks = re.findall(r"```mermaid\n(.*?)```", src.read_text(encoding="utf-8"), re.S)
for i, name in enumerate(names):
    if i >= len(blocks): print(f"  ⚠️  no block #{i} for {name}"); continue
    p = pathlib.Path(name + ".mmd"); p.write_text(blocks[i].rstrip()+"\n", encoding="utf-8")
PY
  for name in $names; do
    [ -f "$name.mmd" ] || continue
    if npx -y @mermaid-js/mermaid-cli -p .pptr.json -i "$name.mmd" -o "$name.svg" >/dev/null 2>&1; then
      echo "  ✅ $name.svg"; ok=$((ok+1))
    else echo "  ❌ $name.svg"; fail=$((fail+1)); fi
  done
}

render_src "$SE/09-model-map.md"                01-lifecycle 02-traceability-spine 03-stakeholder-groups 04-trade-study 05-cross-layer-bridge
render_src "$SE/10-cross-layer-traceability.md" 10-xlayer-requirements 10-xlayer-structure 10-xlayer-behaviour 10-xlayer-parametric 10-xlayer-configuration
render_src "$SE/11-formal-structure.md"         11-component-bdd 11-context-ibd
render_src "$SE/12-formal-behaviour.md"         12-use-cases 12-activity 12-state-machine 12-sequence-remote
render_src "$SE/13-parametrics-and-requirements.md" 13-parametric 13-parametric-full 13-requirements-diagram

rm -f .pptr.json
echo "Done: $ok ok, $fail failed."
