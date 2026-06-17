# 6 · Physical Architecture

> **SE step:** *Physical architecture & allocation.* Now we name the **real
> components** (hardware + software + services) and **allocate every function**
> (F1–F10 from [`05`](05-functional-architecture.md)) to one. Selection rule from
> our constraints: **free, beginner-usable, no lock-in** (CR-1, CR-6, UR-2).

## 6.1 Physical block diagram

```
 ┌─────────────────────────── YOU PROVIDE ───────────────────────────┐
 │   🎤 Microphone (USB/3.5mm)        📷 Camera (USB / phone / DSLR)   │
 └───────────────┬───────────────────────────┬───────────────────────┘
                 │ audio                       │ video
                 ▼                             ▼
 ┌──────────────────────────── THE HUB: your laptop/PC ───────────────────────────┐
 │                                                                                 │
 │  [C1 OBS Studio] ──capture A/V──▶ [C2 Audacity] ──edit/master audio──┐          │
 │        │ (also remote screen)                                        │          │
 │  [C3 Browser call tool] ──remote guest──▶ ────────────────────────────┘         │
 │                                                                       ▼          │
 │  [C4 FFmpeg + scripts] ──normalise loudness, export MP3/MP4, checks──▶ deliver   │
 │  [C5 Whisper (script)] ──transcribe──▶ .txt + .srt                               │
 │  [C6 Canva] ──cover art 1400×1400──▶ cover.png                                   │
 │                                                                                  │
 └───────────────┬───────────────────────────────────────┬────────────────────────┘
                 │ episode.mp3 + metadata + art            │ episode.mp4 + .srt
                 ▼                                         ▼
        ┌──────────────────┐                      ┌────────────────┐
        │ C7 Spotify for   │  generates RSS  ───▶  │  Apple Podcasts │
        │ Creators (host)  │  ─────────────▶ Spotify, Amazon, etc.  │
        └──────────────────┘                      └────────────────┘
                 ▲                                         ▲
                 │                                         │
        ┌────────┴─────────┐                      ┌────────┴────────┐
        │ C8 Cloud backup  │◀── raw + masters ──  │  C9 YouTube     │
        │ (Drive/MEGA/Git) │                      │  (video + .srt) │
        └──────────────────┘                      └─────────────────┘
```

## 6.2 Component catalogue (all free)

| Cmp | Component | What it is | Cost | Platforms | Replaces / alt. |
|---|---|---|---|---|---|
| **C1** | **OBS Studio** | Records camera + mic + screen to MP4; great for video & remote captures | Free, open-source | Win/Mac/Linux | QuickTime, built-in camera app |
| **C2** | **Audacity** | Multitrack audio editor (cut, denoise, levels, music) | Free, open-source | Win/Mac/Linux | GarageBand (Mac), Ocenaudio |
| **C3** | **Browser call tool** | Free remote-guest calls; e.g. **Riverside.fm** free tier (per-speaker tracks) or **Zoom**/**Google Meet** + double-ender | Free tier | Browser | Cleanfeed, Jitsi |
| **C4** | **FFmpeg + repo scripts** | Command-line engine doing high-pass rumble filtering, **loudness normalise to −16 LUFS**, MP3/MP4 export, PASS/FAIL checks | Free, open-source | Win/Mac/Linux | Auphonic (free 2h/mo, GUI) |
| **C5** | **Whisper** (`openai-whisper`, runs locally) | Speech-to-text → transcript + `.srt` captions | Free, open-source | Win/Mac/Linux | YouTube auto-captions, Spotify auto-transcripts |
| **C6** | **Canva** | Drag-and-drop cover art (1400×1400) & social clips | Free tier | Browser | GIMP, Photopea |
| **C7** | **Spotify for Creators** (was Anchor) | Free unlimited podcast **host**; auto-creates the **RSS feed**; 1-click to Spotify; submits to Apple | Free | Browser/app | Podbean free, RSS.com |
| **C8** | **Cloud backup** | Off-device copy of raw + masters | Free tier | Browser/app | Google Drive 15 GB, MEGA 20 GB, GitHub (small files) |
| **C9** | **YouTube** | Video host + huge discovery; accepts `.srt` captions | Free | Browser | Odysee, Vimeo free |
| **C0** | **The laptop/PC** | The integration hub running C1–C6 | Owned | — | A reasonably modern phone can cover much of this |

> 🎵 **Royalty-free assets (CR-1):** intro/outro music & sounds from **YouTube
> Audio Library**, **Pixabay Music**, **Free Music Archive (CC)**, **Incompetech
> (CC-BY)**. Stock images from **Unsplash**, **Pexels**, **Pixabay**. Always keep
> the licence/attribution note in the episode folder.

## 6.3 Allocation matrix (function → component)

| Function | Allocated to | Notes |
|---|---|---|
| F1 Plan | `03-content/` docs + any notes app | scripts/series arc live in this repo |
| F2 Capture | **C1 OBS** (+ mic/cam) | one tool grabs audio **and** video |
| F3 Ingest & back up | **C0 laptop** + `new_episode.sh` → **C8 cloud** | one command makes the folder; you sync to cloud |
| F4 Edit | **C2 Audacity** | audio; video trims also doable in OBS-recorded clips |
| F5 Master | **C4 FFmpeg** (`process_episode.sh`) | automated, repeatable, PR-1/PR-2 |
| F6 Export | **C4 FFmpeg** | MP3 (PR-3) + MP4 (IR-3) |
| F7 Transcribe | **C5 Whisper** (`transcribe.py`) | `.txt` + `.srt` |
| F8 Package | **C6 Canva** + show-notes template | art + notes/chapters/CTA |
| F9 Publish | **C7 Spotify for Creators** (audio→RSS) + **C9 YouTube** (video) | RSS syndicates to Apple etc. |
| F10 Engage & measure | **C7/C9 built-in analytics** + **C6** for clips | feeds back to F1 |

## 6.4 Why these choices (trade-offs)

- **One capture tool (OBS) for A+V** → fewer apps for a beginner (UR-1), and audio+video stay in sync (FR-2).
- **Scripts wrap FFmpeg** instead of a GUI → guarantees the **exact same loudness/format every episode** (PR-1, UR-4) and is 100% free. The GUI alternative **Auphonic** is listed for anyone who fears the terminal.
- **Spotify for Creators as host** → the only free host that is *truly* unlimited and gives a portable RSS feed → satisfies FR-7 + CR-6 at $0.
- **Whisper local** → free, private, bilingual-capable (Nepali + English), no upload limits (PR-5, N-12).
- **No paid item anywhere** → meets UR-2/CR cost constraints; the only "cost" is the laptop you already own.

## 6.5 Deployment / environment view

```
 OFFLINE (works in a village)          ONLINE (needs internet)
 ───────────────────────────          ────────────────────────
  OBS capture                          Cloud backup sync
  Audacity edit                        Publish to host / YouTube
  FFmpeg master/export                 Remote-guest calls
  Whisper transcribe                   Distribution to Spotify/Apple
```

This split satisfies the **offline-first field requirement (N-15, M3)**: all
*creation* runs locally; only *backup and publishing* need the internet.

➡️ Prove it works: [`07-verification-validation.md`](07-verification-validation.md).
