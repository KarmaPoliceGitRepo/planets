# 4 · Concept of Operations (ConOps)

> **SE step:** *Concept of Operations.* Before drawing architecture, we describe
> **how the system is actually used** in real life — the scenarios, the actors,
> and the flow of a normal day. This keeps the design grounded in reality and
> surfaces requirements we might have missed.

## 4.1 Operating modes

| Mode | Description | Main requirements exercised |
|---|---|---|
| **M1 — Solo studio** | Host records alone at home (monologue / narration). | FR-1, FR-2, FR-3, FR-5 |
| **M2 — Remote interview** | Host + a guest over the internet. | FR-10, IR-4 |
| **M3 — In-field / village** | Recording on location (a guide in Mustang, a hot spring). | FR-1, N-15, PR-2 |
| **M4 — Production & publish** | Edit, master, transcribe, upload, schedule. | FR-3..FR-9, PR-1..PR-5 |
| **M5 — Maintain & grow** | Back up, review analytics, plan next episode, engage audience. | FR-11, N-24, N-9 |

## 4.2 Primary scenario — "A week in the life of an episode"

```
 DAY 1  PLAN            Pick topic from series-arc.md → write/adapt script
        │               → book any guest → gather royalty-free music & art.
        ▼
 DAY 2  CAPTURE (M1/M2/M3)
        │               Record audio (mic) + video (camera) locally.
        │               Remote guest? each side records its own track.
        ▼
 DAY 3  INGEST + BACKUP Copy raw files into the episode folder
        │               (new_episode.sh) → immediately back up to cloud.
        ▼
 DAY 4  EDIT            Cut mistakes, balance levels, add intro/outro music.
        ▼
 DAY 5  MASTER + CHECK  Run process_episode.sh → noise removal + loudness
        │               normalise → outputs MP3 + MP4 → prints PASS/FAIL.
        ▼
 DAY 5  TRANSCRIBE      Run transcribe.py → episode.txt + episode.srt;
        │               light human cleanup; translate key parts if needed.
        ▼
 DAY 6  PACKAGE         Write show notes (template) + chapters + CTA;
        │               design 1400×1400 cover art in Canva.
        ▼
 DAY 7  PUBLISH         Upload audio to host (Spotify for Creators) → RSS
        │               syndicates to Apple etc. Upload MP4 + .srt to YouTube.
        ▼
 ONGOING GROW           Share clips, read comments, check analytics, log
                        ideas for next episode. Loop back to PLAN.
```

## 4.3 Scenario detail — M2 Remote interview (the tricky one)

1. Host emails guest a one-click join link (free call tool) **and** asks the
   guest to also hit "record" in their own phone's Voice Memos as a backup
   (this is the *"double-ender"* trick → solves weak connections, **N-15**).
2. Both talk; host records the call locally.
3. After the call, guest sends their local recording (clearer than the call).
4. Host aligns the two tracks by a **clap at the start** (visual+audio sync
   marker) and edits as usual.

## 4.4 Scenario detail — M3 In-field recording

- Mic close to the speaker (≤ 20 cm), record a **10-second "room tone"**
  (silence) for later noise removal (**PR-2**).
- Phone/camera as a backup audio source.
- Files copied and **backed up the same day** before they can be lost (**FR-11**).

## 4.5 Operational assumptions & dependencies

- A laptop/desktop (Windows, Mac, or Linux) is available — it is the hub.
- Home internet exists for upload; field recording is **offline-first**.
- Free-tool accounts (host, YouTube, cloud backup) can be created (by an adult if the creator is a minor, **CR-5**).

## 4.6 What could go wrong (and how the design answers it)

| Risk | Mitigation built into the system |
|---|---|
| Laptop dies → lost episode | **FR-11** off-device backup every day |
| Call drops mid-interview | **M2** double-ender local backup (**N-15**) |
| Episode too quiet/loud | **PR-1** automated loudness normalisation |
| Copyright strike | **CR-1** royalty-free-only assets |
| Beginner overwhelmed | **UR-1/UR-3** single quickstart, one-command scripts |
| Platform bans/locks you in | **CR-6** portable RSS, multi-platform |

➡️ Now we turn these scenarios into the system's **functions**:
[`05-functional-architecture.md`](05-functional-architecture.md).
