#!/usr/bin/env bash
# setup.sh — one-time environment check & setup for The Missing Link podcast.
# Implements the "install once" part of Implementation doc 01.
# Safe to run multiple times. Never deletes anything.

set -u  # treat unset vars as errors (but DON'T use -e: we want friendly messages)

# --- pretty printing ---------------------------------------------------------
green() { printf '\033[32m%s\033[0m\n' "$*"; }
yellow() { printf '\033[33m%s\033[0m\n' "$*"; }
red()    { printf '\033[31m%s\033[0m\n' "$*"; }
bold()   { printf '\033[1m%s\033[0m\n' "$*"; }

bold "==============================================="
bold "  The Missing Link — environment setup & check "
bold "==============================================="
echo

# --- detect OS so we can print the right install command ---------------------
OS="unknown"
case "$(uname -s 2>/dev/null)" in
  Darwin) OS="mac" ;;
  Linux)  OS="linux" ;;
  MINGW*|MSYS*|CYGWIN*) OS="windows" ;;
esac
echo "Detected OS: $OS"
echo

missing=0

# --- check FFmpeg ------------------------------------------------------------
if command -v ffmpeg >/dev/null 2>&1; then
  green "✅ FFmpeg found: $(ffmpeg -version | head -n1)"
else
  red "❌ FFmpeg is NOT installed (needed to master & export episodes)."
  case "$OS" in
    mac)     yellow "   Install it:  brew install ffmpeg"
             yellow "   (No brew? Get it at https://brew.sh first.)" ;;
    linux)   yellow "   Install it:  sudo apt-get update && sudo apt-get install -y ffmpeg"
             yellow "   (Fedora: sudo dnf install ffmpeg | Arch: sudo pacman -S ffmpeg)" ;;
    windows) yellow "   Install it:  winget install Gyan.FFmpeg"
             yellow "   (or download from https://ffmpeg.org/download.html and add to PATH)" ;;
    *)       yellow "   Download from https://ffmpeg.org/download.html" ;;
  esac
  missing=1
fi
echo

# --- check Python 3 ----------------------------------------------------------
PY=""
if command -v python3 >/dev/null 2>&1; then PY="python3";
elif command -v python >/dev/null 2>&1; then PY="python"; fi

if [ -n "$PY" ]; then
  green "✅ Python found: $($PY --version 2>&1)"
else
  red "❌ Python 3 is NOT installed (needed for transcripts)."
  case "$OS" in
    mac)     yellow "   Install it:  brew install python" ;;
    linux)   yellow "   Install it:  sudo apt-get install -y python3 python3-venv python3-pip" ;;
    windows) yellow "   Install it:  winget install Python.Python.3" ;;
    *)       yellow "   Download from https://www.python.org/downloads/" ;;
  esac
  missing=1
fi
echo

# --- create the working folder for episodes ----------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
mkdir -p "$ROOT/episodes"
green "✅ Episodes folder ready: $ROOT/episodes"
echo

# --- offer to set up the Python transcription helper (Whisper) ---------------
if [ -n "$PY" ]; then
  bold "Optional: set up the transcript helper (Whisper)?"
  echo "This creates a local virtual environment and installs openai-whisper."
  echo "It can be ~1 GB and take a few minutes. You can skip and do it later."
  printf "Set it up now? [y/N] "
  read -r ans
  if [ "${ans:-N}" = "y" ] || [ "${ans:-N}" = "Y" ]; then
    "$PY" -m venv "$ROOT/.venv" && \
    # shellcheck disable=SC1091
    . "$ROOT/.venv/bin/activate" 2>/dev/null || . "$ROOT/.venv/Scripts/activate"
    python -m pip install --upgrade pip
    python -m pip install -r "$SCRIPT_DIR/requirements.txt"
    green "✅ Whisper installed into .venv"
    yellow "   (transcribe.py will auto-use this .venv.)"
  else
    yellow "Skipped. Run transcribe.py later and it'll guide you."
  fi
  echo
fi

# --- summary -----------------------------------------------------------------
bold "-----------------------------------------------"
if [ "$missing" -eq 0 ]; then
  green "🎉 All core tools are ready. Next:"
  echo "   bash scripts/new_episode.sh 01 \"The Missing Link\""
else
  yellow "⚠️  Install the missing tool(s) above, then run this again."
fi
bold "-----------------------------------------------"
