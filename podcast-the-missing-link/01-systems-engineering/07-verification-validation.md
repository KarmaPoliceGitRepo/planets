# 7 · Verification & Validation (V&V)

> **SE step:** *Verification & Validation* — the right-hand side of the classic
> **"V" model**.
> - **Verification** = *"Did we build the system right?"* (does it meet each
>   requirement?). Methods: **T**est, **D**emonstration, **I**nspection,
>   **A**nalysis.
> - **Validation** = *"Did we build the right system?"* (does it satisfy the
>   stakeholders' real needs?).

## 7.1 The V-model at a glance

```
 Needs ───────────────────────────────────▶ Validation (Did we meet the NEEDS?)
   │                                              ▲
   ▼                                              │
 Requirements ───────────────────────────▶ Verification (Did we meet the REQS?)
   │                                              ▲
   ▼                                              │
 Functional arch ─────────────────▶ Integration test (functions work together)
   │                                              ▲
   ▼                                              │
 Physical arch ────────────────────────▶ Component test (each tool works)
   │                                              ▲
   └──────────────▶ Implement (install tools, run scripts) ──┘
```

## 7.2 Verification matrix (requirement → method → how)

Methods: **T**est / **D**emonstration / **I**nspection / **A**nalysis.

| Req | Method | How we check it | Pass criterion |
|---|---|---|---|
| FR-1 Capture audio | D | Record 10 s, play back | Speech audible in file |
| FR-2 Capture video | D | Record 10 s in OBS | MP4 has synced video+audio |
| FR-3 Edit | D | Cut a word, add music | Edit persists on export |
| FR-4 Music bed | I | Inspect master | Intro/outro present, levels under voice |
| FR-5 Export | D | Run export | `episode.mp3` + `episode.mp4` exist |
| FR-6 Transcribe | T | Run `transcribe.py` | `.txt` + `.srt` produced |
| FR-7 Publish RSS | D | Upload to host | Episode live; RSS validates |
| FR-8 YouTube | D | Upload MP4 + srt | Video live with captions |
| FR-9 Show notes | I | Inspect episode page | Notes + chapters + CTA + links present |
| FR-10 Remote guest | D | Test call + double-ender | Two usable tracks captured |
| FR-11 Backup | I | Check cloud | Raw + master copies exist off-device |
| PR-1 Loudness −16 LUFS | T/A | `ffmpeg ... loudnorm` print + `process_episode.sh` check | Integrated −16 ±1 LUFS, TP ≤ −1 dBTP → **PASS** |
| PR-2 Noise floor | A | Measure silence after clean | ≤ −50 dBFS |
| PR-3 MP3 spec | I | `ffprobe episode.mp3` | ≥128 kbps, 44.1 kHz |
| PR-4 File size | T | Check 30-min export | ≤ 40 MB |
| PR-5 Transcript acc. | A | Spot-check 100 words | ≥ 90% correct |
| PR-6 ≤3 h production | T | Time a dry-run episode | ≤ 3 h by a beginner |
| UR-1..UR-4 Usability | D | Hand quickstart to a novice | Completes unaided |
| IR-2 RSS valid | T | Run feed through a validator | No errors |
| IR-3 MP4 codec | I | `ffprobe` | H.264 + AAC |
| CR-1 Rights | I | Review asset licence log | Every asset free-to-use/attributed |
| CR-2 ToS | I | Review against platform policy | No violations |
| CR-3 Respectful/sourced | I | Editorial review of script | Claims attributed |
| CR-4 Consent | I | Check release per guest | Signed/recorded consent on file |
| CR-6 Portability | D | Export RSS / move files | Feed + files portable |

> The **`process_episode.sh`** script automates the PR-1..PR-4 checks and prints
> **PASS/FAIL**, so verification of the trickiest requirements is one command.

## 7.3 Integration test (do the functions work *together*?)

**"Golden-path" end-to-end test** — record → publish a 5-minute test episode
(this is also the §3.6 acceptance test):

1. Capture A+V (F2) → 2. Ingest+backup (F3) → 3. Edit+music (F4) → 4. Master
(F5) → 5. Export MP3+MP4 (F6) → 6. Transcribe (F7) → 7. Package (F8) →
8. Publish to host + YouTube (F9) → 9. Confirm live + analytics visible (F10).

✅ **Integration passes** when the test episode is publicly playable on Spotify
**and** YouTube with captions and show notes, produced in one sitting at $0.

## 7.4 Validation (did we meet the *needs*?)

| Need | Validation question | Evidence |
|---|---|---|
| N-04/N-05 free & simple | Could a beginner do it alone, free? | Quickstart dry-run succeeds, no spend |
| N-01 clear audio | Does it *sound* clean to a listener? | Listener feedback + PR-1/PR-2 pass |
| N-06/N-10 right places | Can fans find it where they listen? | Live on Spotify, Apple, YouTube |
| N-08 safe work | Is nothing ever lost? | Backups verified after each episode |
| N-12/N-21 access/lang | Can bilingual & deaf listeners follow? | Transcript/captions present, key parts translated |
| N-09/N-24 grow | Is there a CTA + numbers for sponsors? | CTA in notes, analytics dashboard exists |

## 7.5 Test log template

Copy this per episode into the episode folder:

```
Episode: NN — <title>
Date tested: YYYY-MM-DD   Tester: <name>
[ ] FR-1 audio   [ ] FR-2 video   [ ] FR-5 export
[ ] PR-1 loudness PASS (value: ____ LUFS, TP: ____ dBTP)
[ ] PR-4 size ____ MB (<=40)   [ ] FR-6 transcript
[ ] FR-11 backup done   [ ] FR-7 published   [ ] FR-8 YouTube
[ ] CR-1 assets licensed   [ ] CR-4 consent on file
Notes / issues:
```

➡️ Full forward/backward chain:
[`08-traceability-matrix.md`](08-traceability-matrix.md).
