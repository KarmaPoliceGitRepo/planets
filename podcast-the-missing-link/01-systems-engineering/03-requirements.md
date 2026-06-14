# 3 · Requirements

> **SE step:** *Requirements definition.* A **requirement** turns a need into a
> precise, **verifiable** statement using **"shall"**. Each one must be
> *unambiguous, testable, and traceable* back to a need (`N-xx`) and forward to a
> verification method (see [`07`](07-verification-validation.md)).
>
> **IDs:** `FR` = Functional Requirement (what it does), `PR` = Performance/
> quality, `CR` = Constraint, `IR` = Interface, `UR` = Usability.

## 3.1 Functional Requirements (what the system shall do)

| ID | Requirement | From |
|---|---|---|
| **FR-1** | The system **shall capture spoken audio** from a connected microphone to a digital file. | N-01 |
| **FR-2** | The system **shall capture synchronised video** from a connected camera. | N-02 |
| **FR-3** | The system **shall allow non-destructive editing** (cut, trim, re-order, remove noise) of recordings. | N-03 |
| **FR-4** | The system **shall mix in an intro/outro and music bed** from royalty-free assets. | N-09, N-19 |
| **FR-5** | The system **shall export a distributable audio file** (MP3) and a **video file** (MP4). | N-06, N-02 |
| **FR-6** | The system **shall generate a transcript and caption file** (`.txt` + `.srt`) for each episode. | N-21, N-13 |
| **FR-7** | The system **shall publish episodes to an RSS-based podcast host** that syndicates to Spotify & Apple Podcasts. | N-06, N-10 |
| **FR-8** | The system **shall publish the video version to YouTube**. | N-02, N-10 |
| **FR-9** | The system **shall attach show notes, chapters and links** (incl. a call-to-action) to each episode. | N-09, N-13 |
| **FR-10** | The system **shall support recording a remote guest**, capturing each side. | N-14, N-15 |
| **FR-11** | The system **shall back up every raw recording and master** to off-device storage. | N-08 |

## 3.2 Performance / Quality Requirements (how well)

| ID | Requirement | Target & rationale | From |
|---|---|---|---|
| **PR-1** | Exported audio loudness **shall be normalised to −16 LUFS (±1) integrated, true-peak ≤ −1 dBTP**. | The Apple/Spotify-friendly target for stereo podcasts; consistent volume across episodes. | N-01, N-18 |
| **PR-2** | The audible noise floor **shall be ≤ −50 dBFS** after processing. | Removes hiss/hum so speech is clear. | N-01 |
| **PR-3** | Audio **shall be exported as MP3, mono or stereo, ≥ 128 kbps, 44.1 kHz**. | Small files, universal playback, data-friendly. | N-11, N-18 |
| **PR-4** | A typical 30-minute episode audio file **shall be ≤ 40 MB**. | Downloads on weak connections. | N-11 |
| **PR-5** | Transcript word-accuracy **shall be ≥ 90%** for clear speech before human cleanup. | Usable captions with light editing. | N-21 |
| **PR-6** | End-to-end production of one episode **shall be achievable in ≤ 3 hours** by a beginner. | Sustains a weekly cadence. | N-07, N-05 |

## 3.3 Usability Requirements (the "12-year-old" test)

| ID | Requirement | From |
|---|---|---|
| **UR-1** | Every routine task **shall be documented as a numbered, copy-paste-able step list** with no jargon left unexplained. | N-05, N-22 |
| **UR-2** | The system **shall require no paid software and no credit card** to complete a full episode. | N-04 |
| **UR-3** | A first-time user **shall be able to record, edit and publish a test episode by following one quickstart document**. | N-05 |
| **UR-4** | Automation **shall be runnable with a single command** per task (e.g. `process_episode.sh`). | N-05, N-07 |

## 3.4 Interface Requirements (how it connects)

| ID | Requirement | From |
|---|---|---|
| **IR-1** | The system **shall accept** a USB or 3.5 mm **microphone** and a USB/built-in **camera** as inputs. | N-01, N-02 |
| **IR-2** | The system **shall output a valid podcast RSS feed** conforming to the host's spec (enclosure, title, description, pubDate, artwork ≥ 1400×1400 px). | N-18, FR-7 |
| **IR-3** | The system **shall produce YouTube-compatible MP4** (H.264 video, AAC audio). | N-18, FR-8 |
| **IR-4** | Remote-guest audio **shall interface via a free call/recording tool** that exports per-speaker tracks where possible. | N-14, FR-10 |

## 3.5 Constraints (hard boundaries we cannot cross)

| ID | Constraint | From |
|---|---|---|
| **CR-1** | The system **shall use only assets the creator has the right to use** (own recordings, or royalty-free / Creative Commons / public-domain music & images with attribution as required). | N-19, N-10★ |
| **CR-2** | Content **shall comply with each platform's Terms of Service and content policies**, and with applicable law. | N-18, N-20 |
| **CR-3** | Content **shall be culturally respectful and factually sourced**; claims about people/movements **shall be attributed**. | N-17, N-20 |
| **CR-4** | Personal data of guests/subjects **shall only be published with their consent** (a recorded/written release). | N-17 |
| **CR-5** | If the creator is a minor, platform accounts **shall be created/owned by a responsible adult** per platform age rules. | N-23 |
| **CR-6** | The solution **shall avoid hard lock-in**: episodes and the RSS feed **shall be exportable/portable** to another host. | N-09, N-04 |

## 3.6 Acceptance criteria (definition of "the system works")

The system is accepted when, in a single beginner sitting, the user can:
1. Record audio **and** video of a 5-minute test segment (FR-1, FR-2).
2. Edit it, add intro/outro music, and export MP3 + MP4 (FR-3, FR-4, FR-5).
3. Produce a transcript/`.srt` (FR-6).
4. Pass loudness/noise/size checks via the script (PR-1..PR-4) — the script prints **PASS**.
5. Publish to a podcast host (→ Spotify/Apple) and to YouTube with show notes (FR-7, FR-8, FR-9).
6. Confirm raw + master are backed up off-device (FR-11).
7. Spend **≤ 3 hours** and **$0** (PR-6, UR-2).

➡️ See the full chain in the
[`08-traceability-matrix.md`](08-traceability-matrix.md). Next, the operational
picture: [`04-concept-of-operations.md`](04-concept-of-operations.md).
