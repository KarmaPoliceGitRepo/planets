# 🎬 ReelCut — edit your talk by topic

Turn a single raw video into a finished, captioned, loudness-mastered video by
**picking**, **re-ordering**, and **adding transitions** between auto-detected
topic segments — all in your browser, **on your own machine**. Your video never
leaves your computer.

> Upload → auto-split into segments → keep what you want → drag/swap/renumber the
> order → choose transitions (gaps auto-flagged) → export MP4 + MP3 + SRT.

Built with a **Model-Based Systems Engineering** approach: see [`mbse/`](mbse/)
for the requirements, use-case, structure, and behaviour models, all traced to
the code and tests.

---

## Quick start

**You need:** Python 3.9+ and **FFmpeg** on your PATH. (Whisper is *optional* —
with it you get real transcript-based topic tags; without it ReelCut falls back
to a silence-based split so it still works.)

```bash
# 1. install FFmpeg (one time)
#    macOS:  brew install ffmpeg
#    Ubuntu: sudo apt-get install ffmpeg
#    Windows: https://www.gyan.dev/ffmpeg/builds/  (add bin/ to PATH)

# 2. (optional) better topic tags via Whisper
python3 -m pip install -r requirements.txt

# 3. run it
./run.sh           # macOS/Linux        (run.bat on Windows)
```

Your browser opens at **http://127.0.0.1:8770**. Follow the 5-step wizard.

---

## The 5 steps

| Step | You do | ReelCut does |
|---|---|---|
| **0 · Upload** | drop a video/audio file | copies it locally, reads size/length |
| **1 · Segments** | tick the topics to keep | transcribes (or silence-splits) → tagged **segments** + **sub-sections** |
| **2 · Order & keep** | drag, **swap** two positions, or type a **new order** | re-sequences your clips; validates the order |
| **3 · Transitions** | pick an effect per join | auto-flags **gaps** (cut-out chunks / reorder jumps) and suggests crossfades |
| **4 · Export** | click **Build my video** | renders order+transitions, **re-times captions**, masters to −16 LUFS, gives you `episode.mp4 / .mp3 / .srt` |

### Re-ordering — three ways
- **Drag & drop** the cards into the order you want.
- **Swap** — type two positions to exchange (e.g. `3` ↔ `7`).
- **Renumber** — type the current positions in the new sequence, e.g. `1, 4, 2, 3`.

### Transitions
Every join between two clips is a *boundary*. Boundaries where a chunk was cut
out, or where you re-ordered across the timeline, are **gaps** — highlighted and
best smoothed with a transition. Choose from crossfade, dissolve, fade to
black/white, wipes, slides, circle, radial, … and set each one's duration. One
click applies a crossfade to **all** gaps.

---

## How it works (architecture)

```
Browser UI ──HTTP/JSON──▶ Local Server ──▶ Probe ─┐
(app/static)             (app/server.py)          ├─▶ Segmenter (Whisper|silence)
                                                   ├─▶ Edit Model (project.json)
                                                   ├─▶ Render Engine (two-stage xfade)
                                                   ├─▶ Caption Re-timer
                                                   └─▶ Master (-16 LUFS) ──▶ exports/
```

- **Two-stage render**: each kept clip is cut & normalised to its own file, then
  the files are joined with `xfade`/`acrossfade`/`concat`. (Joining many trims of
  *one* input starves the audio crossfade — separate files avoid that.)
- **Overlap-aware timing**: transitions overlap clips, so each offset is computed
  from a running, overlap-adjusted duration → audio & video stay in sync.
- **Caption re-timing**: because you re-ordered, captions are remapped onto the
  new output timeline.

Full models: [`mbse/00-model-overview.md`](mbse/00-model-overview.md).

---

## Project layout

```
reelcut/
├── run.sh / run.bat          launchers
├── requirements.txt          optional: openai-whisper
├── app/
│   ├── server.py             local web server + REST API + job runner
│   ├── model.py              edit project + the 3 reorder methods
│   ├── static/               the wizard UI (index.html, app.js, styles.css)
│   └── pipeline/
│       ├── probe.py          ffprobe wrapper
│       ├── segment.py        Whisper | silence segmentation + tagging
│       ├── render.py         reorder-aware two-stage transition renderer
│       ├── captions.py       re-time captions for the new order
│       └── master.py         two-pass loudnorm to -16 LUFS, export mp4/mp3
├── mbse/                     the MBSE model (requirements → behaviour → traceability)
├── tests/                    test_reelcut.py (T-1..T-6) + run_e2e.sh (T-7)
└── projects/                 your local edits (git-ignored)
```

## Tests

```bash
python3 tests/test_reelcut.py    # unit + ffmpeg render tests
bash    tests/run_e2e.sh         # full server end-to-end
```

## Privacy & license
Everything runs locally; the server binds to `127.0.0.1` and uploads nothing.
Licensed under the MIT License — see [`LICENSE`](LICENSE).
