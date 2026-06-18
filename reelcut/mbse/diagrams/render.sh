#!/usr/bin/env bash
# render.sh — regenerate MBSE diagram SVGs from the model markdown.
# Single source of truth = the Mermaid blocks in the model files (your Q5-c).
# Output folders mirror the MagicGrid layers. Needs Node (npx) + headless Chromium.
set -u
cd "$(dirname "$0")" || exit 1
MBSE=".."
command -v npx >/dev/null 2>&1 || { echo "❌ need Node/npx"; exit 1; }
# Ensure a headless Chromium is available (fresh containers have none cached).
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

MAP="
0-enterprise-sos/1-sos-context-and-bdd.md|0|enterprise/sos-context-bdd
0-enterprise-sos/2-sos-ibd-exchanges.md|0|enterprise/sos-ibd
0-enterprise-sos/4-actors-perspectives-activities.md|0|enterprise/perspective-contexts
0-enterprise-sos/4-actors-perspectives-activities.md|1|enterprise/system-activity
1-problem-domain/white-box/4-system-behavior-dynamics.md|0|logical/system-sequence
1-problem-domain/white-box/4-system-behavior-dynamics.md|1|logical/system-state-machine
1-problem-domain/black-box/2-use-cases.md|0|conceptual/use-cases
1-problem-domain/black-box/3-system-context.md|0|conceptual/system-context-ibd
1-problem-domain/white-box/2-functional-analysis.md|0|logical/functional-analysis-activity
1-problem-domain/white-box/3-logical-subsystems.md|0|logical/logical-subsystems-bdd
1-problem-domain/white-box/3-logical-subsystems.md|1|logical/logical-subsystems-ibd
2-solution-domain/2-component-behavior.md|0|physical/component-behavior-sequence
2-solution-domain/3-component-structure.md|0|physical/component-structure-bdd
5-traceability.md|0|traceability/vertical-thread
"

python3 - "$MBSE" "$MAP" <<'PY'
import sys, re, pathlib
mbse = pathlib.Path(sys.argv[1])
mapping = [l.split("|") for l in sys.argv[2].strip().splitlines()]
cache = {}
def blocks(fn):
    if fn not in cache:
        cache[fn] = re.findall(r"```mermaid\n(.*?)```", (mbse/fn).read_text(encoding="utf-8"), re.S)
    return cache[fn]
for fn, idx, out in mapping:
    b = blocks(fn); i = int(idx)
    if i >= len(b): print(f"  ⚠️  {fn} has no block #{i}"); continue
    p = pathlib.Path(out + ".mmd"); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(b[i].rstrip()+"\n", encoding="utf-8"); print(f"  extracted {fn}#{i} -> {p}")
PY

ok=0; fail=0
while IFS='|' read -r fn idx out; do
  [ -z "${out:-}" ] && continue
  if npx -y @mermaid-js/mermaid-cli -p .pptr.json -i "$out.mmd" -o "$out.svg" >/dev/null 2>&1; then
    echo "  ✅ $out.svg"; ok=$((ok+1))
  else echo "  ❌ $out.svg"; fail=$((fail+1)); fi
done <<EOF
$MAP
EOF
rm -f .pptr.json
echo "Done: $ok ok, $fail failed."
