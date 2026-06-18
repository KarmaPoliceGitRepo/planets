#!/usr/bin/env bash
# Drift checker for the ReelCut MBSE model.
#
# Fast, deterministic structural checks that catch the kinds of "drift" that bit
# us during modelling — unbalanced code fences (break mermaid rendering) and
# dangling traceability references (an SR deriving from a need or refined by a
# function that does not exist). Does NOT render mermaid (that is slow); the
# CLAUDE.md rule covers running the renderer before committing.
#
# Usage:
#   .claude/hooks/drift-check.sh            # human-readable report, exit 1 on drift
#   (also invoked by the Stop hook in .claude/settings.json, which turns any
#    findings into a systemMessage shown to the user)
#
# Exit 0 = no drift. Exit 1 = drift found (details on stdout).
set -uo pipefail

root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$root" || exit 0
MBSE="reelcut/mbse"

issues=()

# 1) Code-fence parity across BOTH models: every ``` must be matched
#    (odd count breaks mermaid / code blocks). Scans the reelcut MBSE model and
#    the podcast SE docs.
for dir in "$MBSE" "podcast-the-missing-link"; do
  [ -d "$dir" ] || continue
  while IFS= read -r f; do
    [ -f "$f" ] || continue
    n="$(grep -c '^```' "$f" 2>/dev/null)"; n="${n:-0}"
    if (( n % 2 != 0 )); then
      issues+=("fence-parity: odd \`\`\` count ($n) in $f")
    fi
  done < <(find "$dir" -name '*.md' 2>/dev/null)
done

[ -d "$MBSE" ] || { # reelcut model absent: report fence result only
  if (( ${#issues[@]} == 0 )); then echo "drift-check: OK (fences balanced)"; exit 0
  else echo "drift-check: ${#issues[@]} issue(s):"; printf '  - %s\n' "${issues[@]}"; exit 1; fi
}

needs="$MBSE/1-problem-domain/black-box/1-stakeholder-needs.md"
reqs="$MBSE/1-problem-domain/white-box/1-system-requirements.md"
funcs="$MBSE/1-problem-domain/white-box/2-functional-analysis.md"

# Defined need IDs (rows like "| **SN-2.1** | ...") and function IDs ("| **F-21** ...").
defined_sn=""; [ -f "$needs" ] && defined_sn="$(grep -oE '\*\*SN-[0-9.]+\*\*' "$needs" | tr -d '*' | sort -u)"
defined_f="";  [ -f "$funcs" ] && defined_f="$(grep -oE '\*\*F-[0-9]+\*\*' "$funcs" | tr -d '*' | sort -u)"

# 2) Every SN referenced in an SR row's derivedFrom must be a defined need.
if [ -f "$reqs" ] && [ -n "$defined_sn" ]; then
  while IFS= read -r line; do
    for ref in $(grep -oE 'SN-[0-9]+(\.[0-9]+)?' <<<"$line" | sort -u); do
      grep -qx "$ref" <<<"$defined_sn" || issues+=("trace: SR row references undefined need $ref")
    done
  done < <(grep -E '^\| \*\*SR-' "$reqs")
fi

# 3) Every function referenced in an SR row's refinedBy must be a defined function.
if [ -f "$reqs" ] && [ -n "$defined_f" ]; then
  while IFS= read -r line; do
    for ref in $(grep -oE 'F-[0-9]+' <<<"$line" | sort -u); do
      grep -qx "$ref" <<<"$defined_f" || issues+=("trace: SR row references undefined function $ref")
    done
  done < <(grep -E '^\| \*\*SR-' "$reqs")
fi

if (( ${#issues[@]} == 0 )); then
  echo "drift-check: OK (fences balanced, SN/F traceability resolves)"
  exit 0
fi

echo "drift-check: ${#issues[@]} issue(s) found:"
printf '  - %s\n' "${issues[@]}"
exit 1
