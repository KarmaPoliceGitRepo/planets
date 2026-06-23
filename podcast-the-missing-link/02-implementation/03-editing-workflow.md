# Implementation · 3 · Editing & Mastering (F4 + F5)

> Goal: turn raw recordings into a tight, clean, **−16 LUFS** episode. We split
> this into **creative editing** (you, in Audacity) and **technical mastering**
> (one script, automatic).

## Part A — Creative editing in Audacity (F4)

### A1. Import
1. Open **Audacity** → **File → Import → Audio** → choose your `raw/` file(s).
2. Remote guest? Import their track too; **align the claps** so both line up,
   then delete the claps.

### A2. The "topping and tailing" edit
- Cut dead air at the start/end.
- Remove big mistakes, long silences, and "ummm"s: select with the mouse →
  press **Delete**. (Use **Ctrl/Cmd+Z** freely — editing is non-destructive.)
- Keep it punchy. A good rule: *if it doesn't add information or emotion, cut it.*

### A3. Reduce noise (uses your room tone — PR-2)
1. Select ~2 seconds of the **room tone** (pure silence).
2. **Effect → Noise Reduction → Get Noise Profile**.
3. **Select All** (Ctrl/Cmd+A) → **Effect → Noise Reduction** → OK
   (start gentle: 6–12 dB).

### A4. Add music (F4 + CR-1)
1. **File → Import → Audio** your royalty-free intro/outro from `assets/`.
2. Put music on its own track; drag it to the start/end.
3. **Fade** the music under your voice: select the music under speech →
   **Effect → Fade Out / Adjust Volume** so voice stays on top.
4. Log the track's licence in `assets/LICENSES.md` (CR-1).

### A5. Export the rough master
- **File → Export → Export as WAV** → save as `working/episode_premaster.wav`.
- Don't worry about final volume — the script handles that next.

> 🍏 GarageBand users: same idea — arrange clips, add an Apple Loop or imported
> royalty-free track, then **Share → Export Song to Disk → WAV**.

## Part B — Technical mastering with one command (F5 + F6)

This replaces fiddly manual loudness/format work with a repeatable script that
enforces **PR-1 (−16 LUFS, ≤ −1 dBTP)**, **PR-3 (MP3 spec)**, and **PR-4 (size)**
every single time, and applies a high-pass filter to cut low-frequency rumble.
(**PR-2 — the noise floor — is handled in editing step A3 above**, using your
room tone; the script does not do broadband denoising.)

```bash
# from the podcast-the-missing-link/ folder:
bash scripts/process_episode.sh episodes/01-the-missing-link
```

What it does, in order:
1. Finds `working/episode_premaster.wav` (audio) and any `raw/*.mp4` (video).
2. Applies a gentle **high-pass filter** to cut low-frequency rumble/hum
   (hiss/broadband noise is removed earlier by the Audacity step A3).
3. Runs **two-pass loudness normalisation** to **−16 LUFS, true-peak −1 dBTP**.
4. Exports **`exports/episode.mp3`** (44.1 kHz, 128 kbps — PR-3) and, if video
   exists, muxes the mastered audio into **`exports/episode.mp4`** (H.264/AAC — IR-3).
5. **Measures the result and prints `PASS` or `FAIL`** for loudness and file size.

Example output:
```
[process] Loudness measured: -16.1 LUFS (target -16)  ✅
[process] True peak: -1.0 dBTP (limit -1)             ✅
[process] episode.mp3 = 27.4 MB (limit 40)            ✅
[process] RESULT: PASS
```

If it says **FAIL**, the message tells you what to fix (usually: recording was
too quiet/too loud, or too long for the size target → trim more or lower bitrate).

## Part C — No-terminal alternative (Auphonic)

Scared of the command line? Upload `episode_premaster.wav` to **auphonic.com**
(free 2 hours/month), turn on **Loudness Normalization (−16 LUFS)** + **Noise
Reduction**, and download the MP3. Same result, GUI-only.

## Editing checklist

```
[ ] Mistakes/ums/dead air cut
[ ] Noise reduced using room tone
[ ] Intro/outro music added + faded under voice
[ ] Licence logged in assets/LICENSES.md
[ ] premaster.wav exported
[ ] process_episode.sh prints PASS
```

➡️ Next: [`04-publishing-distribution.md`](04-publishing-distribution.md).
