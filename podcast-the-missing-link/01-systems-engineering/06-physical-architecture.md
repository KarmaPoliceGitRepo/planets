# 6 · Physical Architecture

> **SE step:** *Physical architecture & allocation.* Now we name the **real
> components** (hardware + software + services) and **allocate every function**
> (F1–F10 from [`05`](05-functional-architecture.md)) to one. Selection rule from
> our constraints: **free, beginner-usable, no lock-in** (CR-1, CR-6, UR-2).

## 6.0 Solution selection (trade study)

Before naming components we choose the **architecture**. The SoI is first stated as
a **solution class**, then specialised into candidate **variants**, then scored
against **requirement-derived criteria** to pick one. §6.1 onward details the
**selected** variant.

### 6.0.1 SoI as a solution class

**Local-first Podcast Production & Distribution Toolchain** — a $0, beginner-operable
set of components running on the creator's **own laptop** that takes raw
microphone/camera input to edited, mastered, captioned audio + video, publishes via
RSS + YouTube, backs up off-device, and avoids lock-in.

### 6.0.2 Candidate variants (specialisations of the class)

| Variant | Architecture | Essence |
|---|---|---|
| **V1** | GUI tool-chain | OBS + Audacity + Auphonic (GUI master) + Canva + Spotify for Creators + YouTube — manual, many apps |
| **V2** | Script / CLI chain | OBS + FFmpeg scripts (`process_episode.sh`) + Whisper CLI + host/YouTube — repeatable, terminal-driven |
| **V3** | **Integrated local Studio** | OBS + a one-window local web app (`studio.py`, 127.0.0.1) wrapping DSP-clean + segment-edit + master/export + transcribe, then host/YouTube |
| **V4** | Commercial all-in-one | Descript / Riverside Pro — single paid app |

### 6.0.3 Criteria (each traced to a requirement)

| Crit | Meaning | Source |
|---|---|---|
| **K1 Cost = $0** (gate) | no paid software, no card | UR-2, CR-1 |
| **K2 No lock-in** (gate) | episodes + RSS portable | CR-6 |
| **K3 Beginner-usable** | "12-year-old", one quickstart, no jargon | UR-1, UR-3 |
| **K4 Low effort** | single-action tasks, ≤ 3 h/episode | UR-4, PR-6 |
| **K5 Offline / field** | creation works with no internet | N-15, §6.5 |
| **K6 Quality** | hits −16 LUFS + valid MP4 | PR-1, IR-3 |

### 6.0.4 Trade-study matrix (H = 2, M = 1, L = 0)

| | K1 cost | K2 lock-in | K3 beginner | K4 effort | K5 offline | K6 quality | Score |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **V1 GUI** | M (Auphonic free cap) | H | M (many apps) | M | M (Auphonic cloud) | H | **8** |
| **V2 CLI** | H | H | L (terminal) | H | H | H | **9** |
| **V3 Studio** | H | H | H (one window) | H | H | H | **12** |
| **V4 Paid** | **L → eliminated** | M | H | H | M | H | — |

**V4 is eliminated before scoring** — it fails the hard cost gate **K1** (UR-2/CR-1).

### 6.0.5 Selection

**Selected: V3 — Integrated local Studio.** It is the only variant scoring full marks
on the gates *and* on beginner-usability (K3) and effort (K4): one browser window, no
terminal, single-action tasks, fully offline, $0, portable. **V2 (CLI scripts) is
retained underneath V3** (the Studio drives the same FFmpeg/Whisper scripts) and
**V1 (Auphonic GUI)** is documented as a fallback for anyone who prefers it.

➡️ **The selected solution V3 is realised in detail by the `reelcut/` model** (its
local Studio editor subsystem); see §6.6 and
[`../../reelcut/mbse/00-model-overview.md`](../../reelcut/mbse/00-model-overview.md).
The components below (§6.2) are V3's allocation.

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

## 6.6 Added automation: Studio UI, DSP clean, and segment editing

Three components were added to make the system usable end-to-end with **no
command line** (strengthens UR-1 ease-of-use) and to support **edit-by-meaning**:

| Cmp | Component | Function | Allocated script |
|---|---|---|---|
| **C4b** | **DSP cleaner** (FFmpeg chain) | **F4b** clean audio: high-pass → FFT denoise → de-click → de-ess → compress (handles PR-2 noise more thoroughly than editing alone) | `scripts/clean_audio.sh` |
| **C5b** | **Segmenter** (Whisper + grouping) | **F4c** split into tagged **segments** + **sub-sections**; user selects what to keep | `scripts/segment_episode.py`, `scripts/render_selection.py` |
| **C10** | **Studio UI** (local web app, Python stdlib only) | integration/HMI: drives F4b/F4c/F5/F6/F7 from one browser window, binds to `127.0.0.1` (local-only, offline-friendly) | `scripts/studio.py` + `studio/studio.html` |

> **Relationship to `reelcut/`:** components **C4b + C5b + C10** together are the
> local **Studio editor** subsystem. `reelcut/` (and its `reelcut/mbse` model) is the
> **detailed implementation / sub-model of this subsystem only** — it is *not* a
> separate system. The System of Interest is **this podcast production & distribution
> system**; reelcut is one allocated component under it.

These are **additive and backward-compatible**: the original Audacity →
`process_episode.sh` path still works unchanged. `process_episode.sh` now also
prefers `working/episode_clean.wav` (if no hand-made premaster exists) and
`working/episode_cut.mp4` (a selection render) when present. Loudness remains
defined in **exactly one place** (F5 / `process_episode.sh`, −16 LUFS) so PR-1 has
a single source of truth. A how-to deck (pptx + pdf) is generated by
`slides/make_slides.py`.

➡️ Prove it works: [`07-verification-validation.md`](07-verification-validation.md).
