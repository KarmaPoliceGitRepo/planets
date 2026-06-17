#!/usr/bin/env bash
# clean_audio.sh — studio-grade audio "clean up" before mastering (function F4b).
#
# This is the DSP (digital signal processing) cleanup stage. It runs ONE FFmpeg
# chain that, in order:
#   1. high-pass 80 Hz       → removes rumble / handling / AC hum bottom-end
#   2. afftdn (FFT denoise)   → reduces steady hiss / fan / room hum (broadband)
#   3. adeclick               → removes mouth clicks & little pops
#   4. deesser                → tames harsh "sss"/"shh" sibilance
#   5. acompressor            → evens out loud/quiet so the voice sits steady
#   6. low-pass 14 kHz        → shaves the very top hiss (voice is untouched)
#
# It does NOT set final loudness — that stays the single job of
# process_episode.sh (-16 LUFS), so loudness is defined in exactly one place.
#
# Usage:
#   bash scripts/clean_audio.sh episodes/01-the-missing-link            # medium
#   bash scripts/clean_audio.sh episodes/01-the-missing-link strong     # noisier rooms
#   bash scripts/clean_audio.sh episodes/01-the-missing-link light
#
# Input  (first that exists):  <ep>/working/episode_premaster.wav
#                              else the newest <ep>/raw/* audio or video file
# Output:                      <ep>/working/episode_clean.wav
#
# The next steps (segment_episode.py and process_episode.sh) automatically
# prefer episode_clean.wav when it exists.

set -u

green()  { printf '\033[32m%s\033[0m\n' "$*"; }
red()    { printf '\033[31m%s\033[0m\n' "$*"; }
yellow() { printf '\033[33m%s\033[0m\n' "$*"; }
bold()   { printf '\033[1m%s\033[0m\n' "$*"; }
info()   { printf '[clean] %s\n' "$*"; }

if [ "$#" -lt 1 ]; then
  red "Usage: bash scripts/clean_audio.sh <episode-folder> [light|medium|strong]"
  red "e.g.   bash scripts/clean_audio.sh episodes/01-the-missing-link medium"
  exit 1
fi
EP="${1%/}"
STRENGTH="${2:-medium}"
if [ ! -d "$EP" ]; then red "❌ No such folder: $EP"; exit 1; fi
if ! command -v ffmpeg >/dev/null 2>&1; then
  red "❌ FFmpeg not found. Run: bash scripts/setup.sh"; exit 1
fi

# --- pick the input -----------------------------------------------------------
IN="$EP/working/episode_premaster.wav"
if [ ! -f "$IN" ]; then
  IN="$(ls -t "$EP"/raw/* 2>/dev/null | head -n1 || true)"
fi
if [ -z "${IN:-}" ] || [ ! -f "$IN" ]; then
  red "❌ No input audio found."
  yellow "   Export working/episode_premaster.wav from Audacity, or put a recording in raw/."
  exit 1
fi

# --- strength presets ---------------------------------------------------------
# nr  = noise reduction amount (dB) for afftdn; dei = de-ess intensity (0..1)
case "$STRENGTH" in
  light)  NR=8  ; DEI=0.25 ;;
  strong) NR=20 ; DEI=0.55 ;;
  medium|*) STRENGTH="medium"; NR=12 ; DEI=0.40 ;;
esac

OUT="$EP/working/episode_clean.wav"
mkdir -p "$EP/working"

bold "==============================================="
bold "  Cleaning audio ($STRENGTH): $EP"
bold "==============================================="
info "input : $IN"

CHAIN="highpass=f=80,afftdn=nr=${NR}:nf=-25,adeclick,deesser=i=${DEI},acompressor=threshold=-18dB:ratio=3:attack=20:release=250:makeup=2,lowpass=f=14000"

if ffmpeg -y -hide_banner -loglevel error -i "$IN" -af "$CHAIN" -ar 44100 "$OUT"; then
  green "✅ Cleaned audio: $OUT"
  echo  "Next: split it into segments —"
  echo  "      python3 scripts/segment_episode.py $EP"
  echo  "   or master it straight away —"
  echo  "      bash scripts/process_episode.sh $EP"
else
  red "❌ FFmpeg could not clean the audio. Is the input file OK?"
  exit 2
fi
