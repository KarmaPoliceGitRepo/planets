#!/usr/bin/env bash
# new_episode.sh — scaffold a tidy folder for one episode (function F3).
# Usage:  bash scripts/new_episode.sh <number> "<title>"
# Example: bash scripts/new_episode.sh 01 "The Missing Link"

set -u

green() { printf '\033[32m%s\033[0m\n' "$*"; }
red()   { printf '\033[31m%s\033[0m\n' "$*"; }

if [ "$#" -lt 2 ]; then
  red "Usage: bash scripts/new_episode.sh <number> \"<title>\""
  red "e.g.   bash scripts/new_episode.sh 01 \"The Missing Link\""
  exit 1
fi

NUM="$1"; shift
TITLE="$*"

# make a filesystem-friendly slug from the title
SLUG="$(printf '%s' "$TITLE" | tr '[:upper:]' '[:lower:]' \
        | sed -e 's/[^a-z0-9]\+/-/g' -e 's/^-//' -e 's/-$//')"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
EP="$ROOT/episodes/${NUM}-${SLUG}"

if [ -d "$EP" ]; then
  red "❌ That episode folder already exists: $EP"
  red "   (Refusing to overwrite. Pick a different number/title.)"
  exit 1
fi

mkdir -p "$EP/raw" "$EP/assets" "$EP/working" "$EP/exports" "$EP/captions"

# --- asset licence log (CR-1) ------------------------------------------------
cat > "$EP/assets/LICENSES.md" <<EOF
# Asset licences for Episode ${NUM} — ${TITLE}

Log EVERY piece of music, sound, and image you use, so the show stays legal.

| Asset (file) | Source link | Author | Licence | Attribution required? |
|---|---|---|---|---|
|  |  |  |  |  |
EOF

# --- show notes (copied from template idea) ----------------------------------
cat > "$EP/show-notes.md" <<EOF
# Episode ${NUM} — ${TITLE}

**<one–two sentence hook>**

In this episode: <2–3 sentences>.

### Chapters
\`\`\`
00:00 Cold open
00:30 Intro
01:00 <segment>
\`\`\`

### Guest / credits
- Guest: <name> — <who> — <link>

### Sources & links
- <claim> — <source>

### Follow & take part
- Tell us your village's "missing link": <contact>

### Accessibility
- Transcript: captions/episode.txt

### Music & image credits
- See assets/LICENSES.md
EOF

# --- V&V test log (from SE doc 07) -------------------------------------------
cat > "$EP/test-log.md" <<EOF
# Test log — Episode ${NUM}: ${TITLE}
Date tested: ____-__-__   Tester: ________
[ ] FR-1 audio   [ ] FR-2 video   [ ] FR-5 export
[ ] PR-1 loudness PASS (value: ____ LUFS, TP: ____ dBTP)
[ ] PR-4 size ____ MB (<=40)   [ ] FR-6 transcript
[ ] FR-11 backup done   [ ] FR-7 published   [ ] FR-8 YouTube
[ ] CR-1 assets licensed   [ ] CR-4 consent on file
Notes / issues:
EOF

green "✅ Created episode folder: $EP"
echo "   ├── raw/        (put recordings here — never edit these)"
echo "   ├── assets/     (music/images + LICENSES.md)"
echo "   ├── working/    (Audacity project, export premaster.wav here)"
echo "   ├── exports/    (episode.mp3 / episode.mp4 land here)"
echo "   ├── captions/   (transcript + subtitles)"
echo "   ├── show-notes.md"
echo "   └── test-log.md"
echo
echo "Next: record into raw/, edit in Audacity, export working/episode_premaster.wav,"
echo "then run:  bash scripts/process_episode.sh $EP"
