#!/usr/bin/env bash
# Launch ReelCut. Needs Python 3 and FFmpeg on PATH.
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
command -v ffmpeg >/dev/null 2>&1 || { echo "❌ FFmpeg not found — install it first (see README)."; exit 1; }
PY="$(command -v python3 || command -v python)"
[ -n "$PY" ] || { echo "❌ Python 3 not found."; exit 1; }
exec "$PY" "$DIR/app/server.py"
