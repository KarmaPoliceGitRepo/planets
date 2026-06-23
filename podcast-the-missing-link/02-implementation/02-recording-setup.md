# Implementation · 2 · Recording Setup (Capture — F2)

> Goal: capture **clear audio** and **good video** so editing is easy. "Fix it
> in the mic, not in the mix" — 10 minutes of setup saves an hour of editing.

## 2.1 Room & mic (the 5 golden rules)

1. **Get close.** Mouth ~15–20 cm from the mic. Closer = more voice, less room.
2. **Kill echo.** Record in a small, soft room (curtains, bed, clothes, sofa).
   A closet full of clothes is a famous free "vocal booth".
3. **Kill noise.** Turn off fans/AC, fridge, notifications. Close the window.
4. **Pop filter on the cheap.** Speak slightly *across* the mic, not straight
   into it, to avoid "p"/"b" pops. A sock over the mic works in a pinch.
5. **Record 10 seconds of silence** ("room tone") at the start of every session
   — our noise-removal step uses it.

## 2.2 Levels (don't clip!)

- Watch the level meter while you talk normally and at your loudest laugh.
- Aim for peaks around **−12 to −6 dB**. If it hits **0 dB it "clips"** (nasty
  crackle that can't be fixed). Turn the gain down until your loudest moment
  stays below 0.

## 2.3 Recording **video + audio** together in OBS (C1)

1. Open **OBS Studio** → bottom-right **Settings → Output → Recording**:
   set **Format = mp4** (or `mkv` then remux), **Encoder = x264** (H.264, our
   IR-3 target).
2. **Settings → Audio**: pick your **microphone** as the input device.
3. In **Sources** (bottom) click **+** → **Video Capture Device** → your camera.
4. Click **+** again → **Audio Input Capture** → your mic (if not already in
   the mixer).
5. Frame yourself: eyes in the upper third, good light **in front** of you (face
   a window; never sit with the window behind you).
6. Hit **Start Recording**, clap once (sync marker), then talk.
7. **Stop Recording** → file lands in your OBS videos folder. Move it into your
   episode's `raw/` folder.

> 🎧 **Audio-only?** You can record straight into **Audacity**: press the red
> **Record** button. Even simpler. Still do the clap + room tone.

## 2.4 Recording a **remote guest** (M2 / FR-10)

**Best free option — Riverside.fm (C3):**
- Create a studio, send the guest the link. It records **each person's audio
  locally in high quality**, then uploads — so a glitchy call still sounds great.

**Zero-friction option — "the double-ender":**
1. Call on **Zoom / Google Meet** (free) and record the call as a backup.
2. Ask the guest to **also press record on their phone** (Voice Memos / Recorder)
   — this is *their* clean local track.
3. Everyone **claps once** at the start to create a sync point.
4. After, the guest sends you their phone recording. You line up the claps in
   Audacity. Result: studio-quality remote audio for free, even on weak signal
   (solves **N-15**).

## 2.5 Recording **in the field / village** (M3)

- Phone or camera mic close to the speaker; record **room tone** there too.
- Keep a **backup recorder** running (a second phone) — you rarely get a retake
  in the field.
- **Copy files to your laptop and back them up the same day** (FR-11). Field
  footage is irreplaceable.

## 2.6 Capture checklist (tick before you stop)

```
[ ] Room quiet, echo controlled
[ ] Mic ~15–20 cm, levels peak −12..−6 dB (no clipping)
[ ] 10 s room tone recorded
[ ] Clap for sync (if video or remote)
[ ] Good front lighting (if video)
[ ] Guest's local backup running (if remote)
[ ] Files moved to episodes/NN-.../raw/ and backed up
```

➡️ Next: [`03-editing-workflow.md`](03-editing-workflow.md).
