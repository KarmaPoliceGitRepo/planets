#!/usr/bin/env bash
# T-7 — full server end-to-end: upload → segment → reorder → transition → export.
# Generates its own throwaway sample (no media committed to git).
set -u
cd "$(dirname "$0")/.." || exit 1

green(){ printf '\033[32m%s\033[0m\n' "$*"; }
red(){ printf '\033[31m%s\033[0m\n' "$*"; }

command -v ffmpeg >/dev/null 2>&1 || { red "ffmpeg required"; exit 1; }
TMP="$(mktemp -d)"; SRC="$TMP/src.mp4"
# 4 tone bursts (3s) + 1s silences, 4 colour blocks → silence engine finds chunks
ffmpeg -y -hide_banner -loglevel error -filter_complex "
 sine=f=200:d=3,apad=pad_dur=1[a1];sine=f=300:d=3,apad=pad_dur=1[a2];
 sine=f=400:d=3,apad=pad_dur=1[a3];sine=f=500:d=3,apad=pad_dur=1[a4];
 [a1][a2][a3][a4]concat=n=4:v=0:a=1[aout];
 color=c=red:s=320x240:r=30:d=4[v1];color=c=green:s=320x240:r=30:d=4[v2];
 color=c=blue:s=320x240:r=30:d=4[v3];color=c=orange:s=320x240:r=30:d=4[v4];
 [v1][v2][v3][v4]concat=n=4:v=1:a=0[vout]" \
 -map "[vout]" -map "[aout]" -c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac "$SRC" || { red "sample build failed"; exit 1; }

python3 app/server.py >"$TMP/server.log" 2>&1 &
SPID=$!; sleep 2
J(){ curl -s "$@"; }
BASE="http://127.0.0.1:8770"
fail(){ red "❌ $1"; kill $SPID 2>/dev/null; rm -rf "$TMP"; exit 1; }

PID=$(J -X POST --data-binary @"$SRC" -H "X-Filename: src.mp4" "$BASE/api/upload" | python3 -c "import sys,json;print(json.load(sys.stdin).get('id',''))")
[ -n "$PID" ] || fail "upload"
green "✓ uploaded ($PID)"

J -X POST "$BASE/api/segment" -H 'Content-Type: application/json' -d "{\"id\":\"$PID\"}" >/dev/null
for i in $(seq 1 25); do J "$BASE/api/job" | grep -q '"done": true' && break; sleep 1; done
NSUB=$(J "$BASE/api/project?id=$PID" | python3 -c "import sys,json;p=json.load(sys.stdin);print(sum(len(s['subsections']) for s in p['segments']))")
[ "$NSUB" -ge 2 ] || fail "segment produced <2 sub-sections"
green "✓ segmented ($NSUB sub-sections)"

J -X POST "$BASE/api/reorder" -H 'Content-Type: application/json' -d "{\"id\":\"$PID\",\"method\":\"permutation\",\"order\":[2,1]}" >/dev/null
TO=$(J "$BASE/api/sequence?id=$PID" | python3 -c "import sys,json;print(json.load(sys.stdin)['boundaries'][0]['to'])")
J -X POST "$BASE/api/transition" -H 'Content-Type: application/json' -d "{\"id\":\"$PID\",\"to\":\"$TO\",\"type\":\"crossfade\",\"duration\":0.8}" >/dev/null
green "✓ reordered + transition set"

J -X POST "$BASE/api/render" -H 'Content-Type: application/json' -d "{\"id\":\"$PID\"}" >/dev/null
for i in $(seq 1 60); do J "$BASE/api/job" | grep -q '"done": true' && break; sleep 1; done
RES=$(J "$BASE/api/job" | python3 -c "import sys,json;j=json.load(sys.stdin);r=j.get('result') or {};print(int(bool(r.get('pass'))),r.get('loudness'))")
PASS=$(echo "$RES" | cut -d' ' -f1)
for f in episode.mp4 episode.mp3 episode.srt; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "$BASE/api/file?id=$PID&name=$f")
  [ "$code" = "200" ] || fail "export $f missing ($code)"
done
green "✓ exported mp4 + mp3 + srt"
[ "$PASS" = "1" ] && green "✓ master PASS (-16 LUFS)" || red "⚠ master not PASS ($RES)"

kill $SPID 2>/dev/null; rm -rf "$TMP"
green "🎉 T-7 end-to-end PASSED"
