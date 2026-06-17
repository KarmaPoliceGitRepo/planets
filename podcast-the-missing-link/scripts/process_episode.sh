#!/usr/bin/env bash
# process_episode.sh — auto-master & export an episode (functions F5 + F6).
# Cleans audio, normalises loudness to -16 LUFS / -1 dBTP (PR-1), exports a
# spec-compliant MP3 (PR-3) and, if raw video exists, an MP4 (IR-3), then
# verifies loudness and file size and prints PASS / FAIL (V&V doc 07).
#
# Usage:  bash scripts/process_episode.sh episodes/01-the-missing-link
#
# Input it expects:  <episode>/working/episode_premaster.wav   (your edit)
# Optional video:    the newest <episode>/raw/*.mp4 or *.mov

set -u

green()  { printf '\033[32m%s\033[0m\n' "$*"; }
red()    { printf '\033[31m%s\033[0m\n' "$*"; }
yellow() { printf '\033[33m%s\033[0m\n' "$*"; }
bold()   { printf '\033[1m%s\033[0m\n' "$*"; }
info()   { printf '[process] %s\n' "$*"; }

# --- targets (from requirements) ---------------------------------------------
TARGET_I="-16"        # PR-1 integrated loudness (LUFS), stereo podcast target
TARGET_TP="-1.0"      # PR-1 max true peak (dBTP)
TARGET_LRA="11"       # loudness range
MP3_BITRATE="128k"    # PR-3
MP3_RATE="44100"      # PR-3
MAX_MB="40"           # PR-4 (per ~30 min); informational for longer shows

# --- args & checks -----------------------------------------------------------
if [ "$#" -lt 1 ]; then
  red "Usage: bash scripts/process_episode.sh <episode-folder>"
  red "e.g.   bash scripts/process_episode.sh episodes/01-the-missing-link"
  exit 1
fi
EP="${1%/}"
if [ ! -d "$EP" ]; then red "❌ No such folder: $EP"; exit 1; fi
if ! command -v ffmpeg >/dev/null 2>&1; then
  red "❌ FFmpeg not found. Run: bash scripts/setup.sh"; exit 1
fi

IN="$EP/working/episode_premaster.wav"
if [ ! -f "$IN" ]; then
  red "❌ Expected your edit at: $IN"
  yellow "   In Audacity: File → Export → WAV → save as that name."
  exit 1
fi

mkdir -p "$EP/exports"
OUT_MP3="$EP/exports/episode.mp3"
OUT_WAV="$EP/exports/episode_master.wav"

bold "==============================================="
bold "  Mastering: $EP"
bold "==============================================="

# === PASS 1: measure loudness ===============================================
info "Pass 1/2: measuring loudness..."
MEAS="$(ffmpeg -hide_banner -nostats -i "$IN" \
  -af "loudnorm=I=${TARGET_I}:TP=${TARGET_TP}:LRA=${TARGET_LRA}:print_format=json" \
  -f null - 2>&1)"

get() { printf '%s\n' "$MEAS" | grep "\"$1\"" | head -n1 | sed -E 's/.*: *"?([-0-9.]+|inf)"?.*/\1/'; }
M_I="$(get input_i)"; M_TP="$(get input_tp)"; M_LRA="$(get input_lra)"
M_THRESH="$(get input_thresh)"; M_OFFSET="$(get target_offset)"

if [ -z "${M_I:-}" ]; then
  yellow "⚠️  Could not parse measurement; falling back to single-pass loudnorm."
  AF="highpass=f=80,loudnorm=I=${TARGET_I}:TP=${TARGET_TP}:LRA=${TARGET_LRA}"
else
  info "Measured input: I=${M_I} LUFS, TP=${M_TP} dBTP, LRA=${M_LRA}"
  # highpass removes rumble; loudnorm second pass uses measured values (accurate)
  AF="highpass=f=80,loudnorm=I=${TARGET_I}:TP=${TARGET_TP}:LRA=${TARGET_LRA}:measured_I=${M_I}:measured_TP=${M_TP}:measured_LRA=${M_LRA}:measured_thresh=${M_THRESH}:offset=${M_OFFSET}:linear=true"
fi

# === PASS 2: apply & export master WAV + MP3 =================================
info "Pass 2/2: normalising and exporting audio..."
ffmpeg -y -hide_banner -loglevel error -i "$IN" -af "$AF" -ar "$MP3_RATE" "$OUT_WAV"
ffmpeg -y -hide_banner -loglevel error -i "$OUT_WAV" -codec:a libmp3lame -b:a "$MP3_BITRATE" -ar "$MP3_RATE" "$OUT_MP3"
green "✅ Audio exported: $OUT_MP3"

# === optional VIDEO: mux mastered audio into newest raw video ================
VID="$(ls -t "$EP"/raw/*.mp4 "$EP"/raw/*.mov "$EP"/raw/*.mkv 2>/dev/null | head -n1 || true)"
if [ -n "${VID:-}" ]; then
  OUT_MP4="$EP/exports/episode.mp4"
  info "Found video: $(basename "$VID") → building episode.mp4 (H.264/AAC)"
  # Re-encode video to H.264 (IR-3), replace its audio with our mastered track.
  ffmpeg -y -hide_banner -loglevel error -i "$VID" -i "$OUT_WAV" \
    -map 0:v:0 -map 1:a:0 -c:v libx264 -preset veryfast -crf 22 \
    -c:a aac -b:a 160k -shortest "$OUT_MP4"
  green "✅ Video exported: $OUT_MP4"
else
  yellow "ℹ️  No raw video found (raw/*.mp4|mov|mkv) — skipping MP4. Audio-only is fine."
fi

# === VERIFY (PR-1, PR-4) ====================================================
bold "-----------------------------------------------"
info "Verifying the master..."
VER="$(ffmpeg -hide_banner -nostats -i "$OUT_MP3" \
  -af "loudnorm=I=${TARGET_I}:TP=${TARGET_TP}:LRA=${TARGET_LRA}:print_format=json" \
  -f null - 2>&1)"
getv() { printf '%s\n' "$VER" | grep "\"$1\"" | head -n1 | sed -E 's/.*: *"?([-0-9.]+|inf)"?.*/\1/'; }
F_I="$(getv input_i)"; F_TP="$(getv input_tp)"

# file size in MB (portable-ish)
BYTES="$(wc -c < "$OUT_MP3" | tr -d ' ')"
MB="$(awk "BEGIN{printf \"%.1f\", ${BYTES}/1048576}")"

pass=1
chk_band() { # chk_band "label" value lo hi   (value must be within lo..hi)
  awk -v v="$2" -v lo="$3" -v hi="$4" 'BEGIN{exit !(v>=lo && v<=hi)}' \
    && green "✅ $1: $2 (ok: $3..$4)" || { red "❌ $1: $2 (want $3..$4)"; pass=0; }
}
chk_max() { # chk_max "label" value max   (value must be <= max; lower is fine)
  awk -v v="$2" -v hi="$3" 'BEGIN{exit !(v<=hi)}' \
    && green "✅ $1: $2 (limit <= $3)" || { red "❌ $1: $2 (must be <= $3)"; pass=0; }
}
# PR-1: integrated loudness within +/-1 LUFS of target; true peak must not EXCEED -1 dBTP.
[ -n "${F_I:-}" ]  && chk_band "Loudness LUFS" "$F_I"  "-17" "-15" || yellow "⚠️ loudness unverified"
[ -n "${F_TP:-}" ] && chk_max  "True peak dBTP" "$F_TP" "$TARGET_TP" || yellow "⚠️ true-peak unverified"
awk -v v="$MB" -v hi="$MAX_MB" 'BEGIN{exit !(v<=hi)}' \
  && green "✅ Size: ${MB} MB (limit ${MAX_MB})" \
  || { yellow "⚠️ Size: ${MB} MB > ${MAX_MB} MB (fine for long episodes; trim or lower bitrate for data-light listeners)"; }

bold "-----------------------------------------------"
if [ "$pass" -eq 1 ]; then
  green "RESULT: PASS ✅  — exports/ is ready to publish."
  echo  "Next: python3 scripts/transcribe.py $EP"
else
  red   "RESULT: FAIL ❌  — see ❌ lines above."
  yellow "Common fixes: re-record closer to the mic (too quiet) or back off (too hot),"
  yellow "then re-export working/episode_premaster.wav and run this again."
  exit 2
fi
