# Implementation · 4 · Publishing & Distribution (F7 + F8 + F9)

> Goal: get the finished episode **everywhere people listen and watch**, with
> transcripts, art, and show notes — for free.

## 4.1 Make the transcript & captions first (F7 — accessibility, N-21)

```bash
bash scripts/transcribe.py episodes/01-the-missing-link
# or:  python3 scripts/transcribe.py episodes/01-the-missing-link
```
This creates `captions/episode.txt` (full transcript) and
`captions/episode.srt` (subtitles for YouTube). Skim and fix any names
(e.g. *Mahendra*, *Gyanendra*, *Mustang*, *Manang*, *tato pani*) — Whisper
guesses spellings. For bilingual episodes, run it once; for a translation, paste
the `.txt` into a free translator and save `episode.ne.txt` / `episode.en.txt`.

## 4.2 Cover art (F8 — IR-2 requires ≥ 1400×1400 px)

1. In **Canva**: search the template "**Podcast Cover**" (it's already square).
2. Set size to **1400 × 1400 px** (or bigger, up to 3000×3000).
3. Put the show title **The Missing Link** large enough to read as a tiny phone
   thumbnail. Use a royalty-free image (Unsplash/Pexels) — log it in `LICENSES.md`.
4. **Download as PNG** → save to `episodes/NN-.../assets/cover_1400.png`.

## 4.3 Write the show notes (F8 — FR-9)

Copy `03-content/show-notes-template.md` into your episode folder and fill it in:
title, 2–3 sentence description, **chapters with timestamps**, **links/sources**,
**guest credits** (N-16), and a clear **call-to-action** (N-09) — e.g. *"Follow,
share, and tell us your village's missing link."*

## 4.4 Publish AUDIO → Spotify for Creators (F9 — FR-7)

1. Go to **creators.spotify.com** → log in → **New episode**.
2. **Upload** `exports/episode.mp3`.
3. Paste the **title**, **description/show notes**, and **chapters**.
4. Upload `cover_1400.png` (first episode sets the show artwork).
5. **Publish** (or schedule).
6. Spotify for Creators automatically:
   - creates your **RSS feed** (this is the master copy of your show — keep the
     URL; it's how you stay portable, **CR-6**),
   - lists you on **Spotify**,
   - lets you **submit the RSS to Apple Podcasts** (one-time, via
     podcastsconnect.apple.com) and to Amazon/iHeart etc.

> 🔗 **The RSS feed is the heart of podcasting.** Every app (Apple, Overcast,
> Pocket Casts…) just reads that feed. Host once → everywhere. If you ever
> outgrow this host, you can redirect the feed elsewhere — no audience lost.

## 4.5 Publish VIDEO → YouTube (F9 — FR-8)

1. **youtube.com → Create → Upload video** → choose `exports/episode.mp4`.
2. Title + description (reuse your show notes + chapters; YouTube turns
   `00:00 Intro` style timestamps into clickable chapters).
3. **Subtitles → Upload file → select `captions/episode.srt`** (accessibility,
   N-21; also boosts discovery).
4. Add the `cover` image as a custom thumbnail.
5. Set audience appropriately and **Publish** (or schedule).

## 4.6 Back up (F9→done, FR-11)

Copy the whole `episodes/NN-.../` folder (raw + exports + captions) to your
**cloud backup** (Drive/MEGA). You should never have only one copy of a master.

## 4.7 Grow & measure (F10)

- **Clips:** in Canva or CapCut, cut a 30–60 s highlight for TikTok/Reels/Shorts
  → link back to the full episode.
- **Analytics:** Spotify for Creators + YouTube Studio show plays, listens, and
  audience — this is your **sponsor-ready evidence** (N-24).
- **Engage:** reply to comments; ask listeners to suggest the next village story
  → feeds back into planning (F10 → F1).

## 4.8 Publish checklist

```
[ ] transcript + .srt generated & names fixed
[ ] cover_1400.png ready (>=1400px)
[ ] show notes: description + chapters + links + credits + CTA
[ ] audio published on Spotify for Creators (RSS live)
[ ] RSS submitted to Apple Podcasts (one-time)
[ ] video + .srt uploaded to YouTube
[ ] whole episode folder backed up to cloud
[ ] highlight clip posted with link back
```

➡️ Beginner version of all of this: [`05-kid-simple-quickstart.md`](05-kid-simple-quickstart.md).
