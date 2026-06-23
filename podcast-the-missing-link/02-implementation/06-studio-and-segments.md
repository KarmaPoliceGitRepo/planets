# Implementation · 6 · The Studio app + segment editing (F4b/F4c + UI)

> Goal: do the **whole episode** — clean, choose what to keep, master, caption —
> from **one window in your browser**, with no command line. This is the friendly
> front-end over the same free scripts described in docs 3–5.

There are two new ideas here:

1. **DSP audio cleaning** (`clean_audio.sh`) — a one-click "make my voice sound
   clean" step before mastering.
2. **Segment editing** — your episode is automatically split into **topics
   (segments)** and smaller **sub-sections**, each **tagged**, so you can edit by
   *meaning* (tick what to keep) instead of scrubbing a waveform.

The **Studio** (`studio.py` + `studio/studio.html`) ties it all together.

---

## 6.1 Start the Studio

```bash
# one time: install the free software (FFmpeg + Whisper)
bash scripts/setup.sh

# every time: launch the Studio
python3 scripts/studio.py
```

It prints a link and opens your browser at **http://127.0.0.1:8765**. It runs
**only on your computer** (the address `127.0.0.1` means "this machine") — nothing
is uploaded. Press **Ctrl+C** in the terminal to stop it.

---

## 6.2 The pipeline, button by button

| Button | What runs | What it does |
|---|---|---|
| **+ New episode** | `new_episode.sh` | makes a tidy `episodes/NN-slug/` folder |
| **① Clean audio** | `clean_audio.sh` | high-pass (rumble) → FFT **denoise** → **de-click** → **de-ess** → gentle **compression**. Choose `light / medium / strong`. |
| **② Split into segments** | `segment_episode.py` | Whisper transcribes, then groups the audio into **tagged topics + sub-sections** and writes `working/segments.json` |
| *(tick boxes)* | — | keep/drop whole **segments** and individual **sub-sections** |
| **③ Rebuild (keep ticked)** | `render_selection.py` | FFmpeg trims + re-joins **only** the parts you kept (audio **and** video, in sync) → fresh `episode_premaster.wav` (+ `episode_cut.mp4`) |
| **④ Master (-16 LUFS)** | `process_episode.sh` | two-pass loudness, exports `episode.mp3` + `episode.mp4`, prints **PASS/FAIL** |
| **Subtitles** | `transcribe.py` | writes `episode.txt` + `episode.srt` |

> **Order for a new episode:** record into `raw/` → **①** → **②** → tick what to
> keep → **💾 Save choices** → **③** → **④**. Then publish (doc 4).

---

## 6.3 Cleaning the audio (the DSP step)

`clean_audio.sh` runs **one FFmpeg chain** (in this order):

1. **high-pass 80 Hz** — removes rumble, handling thumps, mains hum bottom-end.
2. **`afftdn`** (FFT denoise) — reduces steady hiss / fan / room hum.
3. **`adeclick`** — removes mouth clicks and little pops.
4. **`deesser`** — tames harsh "sss"/"shh" sibilance.
5. **`acompressor`** — evens out loud/quiet so the voice sits steady.
6. **low-pass 14 kHz** — shaves the very top hiss (voice untouched).

It writes `working/episode_clean.wav` and **does not** set final loudness — that
stays the single job of mastering (`process_episode.sh` → −16 LUFS), so loudness
is defined in exactly one place.

```bash
bash scripts/clean_audio.sh episodes/01-the-missing-link medium   # or light / strong
```

Use **strong** for noisy rooms, **light** for already-quiet recordings.

---

## 6.4 Segments & sub-sections — editing by meaning

`segment_episode.py` transcribes with Whisper, then:

- groups the fine transcript lines into **sub-sections** at natural pauses and
  sentence endings;
- groups sub-sections into **segments (topics)** using long pauses **and** a
  simple *lexical-cohesion* test (when the next sub-section stops sharing
  vocabulary with the current topic, a new segment starts);
- gives every segment and sub-section a short **tag/title** from its keywords.

The result is `working/segments.json`, e.g.:

```jsonc
{
  "segments": [
    {
      "id": "seg-2", "title": "kings · villages · roads",
      "tag": "villages", "start": 252.0, "end": 570.0, "keep": true,
      "subsections": [
        { "id": "seg-2-1", "start": 252.0, "end": 340.0,
          "text": "King Mahendra pushed a return to the villages…",
          "tag": "mahendra · movement", "keep": true },
        { "id": "seg-2-2", "start": 340.0, "end": 415.0,
          "text": "…a long tangent about lunch…",
          "tag": "lunch", "keep": false }
      ]
    }
  ]
}
```

In the Studio you flip those `keep` flags by ticking boxes. **A sub-section is
kept only if both it *and* its parent segment are kept.** The live bar shows how
long your finished episode will be.

```bash
# command-line equivalents (the Studio buttons run these):
python3 scripts/segment_episode.py episodes/01-the-missing-link        # ② split
python3 scripts/render_selection.py episodes/01-the-missing-link       # ③ rebuild
```

Re-running the split is cheap: the transcription is cached in
`working/whisper.json` (`--reuse` skips re-transcribing).

> **Nothing is ever lost.** `render_selection.py` reads the *original* cleaned
> audio and only *assembles* the kept pieces; a hand-made premaster is backed up
> to `working/episode_premaster.orig.wav` the first time. Change your mind and
> re-render any time.

---

## 6.5 Bigger/smaller chunks

Segment sizes are tuned for natural speech. To make topics longer or shorter,
edit the knobs at the top of `segment_episode.py` (`MIN_SEG`, `MAX_SEG`,
`COHESION_MIN`, `GAP_SUB`, …) and re-run **② Split** with `--reuse` (instant,
no re-transcribe).

---

## 6.6 The explainer deck

A ready-made "what this is + how to use it" presentation lives in
[`../slides/`](../slides/) as both **PowerPoint** and **PDF**. Rebuild it with:

```bash
python3 slides/make_slides.py
```

(It uses `python-pptx`; if LibreOffice is installed it also exports a matching
PDF, otherwise it falls back to a built-in PDF writer.)

---

## 6.7 Studio checklist

```
[ ] setup.sh run once (FFmpeg + Whisper OK)
[ ] recording in episodes/NN/raw/
[ ] ① Clean audio → episode_clean.wav
[ ] ② Split into segments → segments shown in Studio
[ ] ticked the segments / sub-sections to keep, then 💾 Save choices
[ ] ③ Rebuild → episode_premaster.wav (+ episode_cut.mp4 if video)
[ ] ④ Master → PASS, exports/episode.mp3 (+ .mp4)
[ ] Subtitles → captions/episode.srt
[ ] publish (see 04-publishing-distribution.md)
```

➡️ Publish what you made: [`04-publishing-distribution.md`](04-publishing-distribution.md).
