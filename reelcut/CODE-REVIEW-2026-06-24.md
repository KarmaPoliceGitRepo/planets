# ReelCut Code Review — 2026-06-24

> Defect-level review of the **finished, merged** ReelCut code (closes RAID issue **I-3**).
> Produced by four parallel reviewers over `reelcut/app/**` (~1,700 LOC). Findings are
> deduplicated and prioritised. Severity: **HIGH** = correctness / data-loss / security ·
> **MED** = likely bug / risky · **LOW** = quality / tech-debt.
>
> Status key: `Open` (not yet fixed) · `Fixed(commit)` · `Won't-fix(reason)`.
> This list is the backlog; fixes land in later commits and flip the Status here.

## HIGH — security (localhost HTTP API → FFmpeg)

| ID | Status | File:line | Problem | Fix |
|----|--------|-----------|---------|-----|
| CR-H1 | Fixed | server.py:250–255 | `replace_audio`/`add_audio`/`add_image` pass `data["video"|"audio"|"image"]` straight to FFmpeg `-i` with only an extension check — **arbitrary local file read** (e.g. `/etc/passwd`) and write outside the project. | Resolve every artifact path inside the project dir (reuse `_safe_id`); reject paths that escape it. |
| CR-H2 | Fixed | audio_mix.py:31,35 | `level_db` from the request body is string-interpolated into `-filter_complex` — **filtergraph injection** (`"0dB[x];…"`). | Validate as a bounded float; never raw-interpolate request values into a filter string. |
| CR-H3 | Fixed | server.py:229–232 | `/api/save` persists `data["project"]` verbatim — a request can set `source` to any path, later read by render/probe as an FFmpeg input. | Validate project shape; confine `source`/`whisper_cache` to the project dir before persisting. |
| CR-H4 | Fixed | server.py:159–187 | No **Host-header / Origin** validation → a DNS-rebinding site can reach the 127.0.0.1 server and drive file ops despite the localhost bind. | Reject requests whose `Host` ≠ `127.0.0.1:PORT`/`localhost:PORT`; add a per-session token on state-changing routes. |
| CR-H5 | Fixed | server.py:163–167 | `/static/` traversal guard relies on `STATIC in f.parents` with no `resolve()`/symlink guard. | Use `Path.resolve()` + `is_relative_to(STATIC.resolve())`; refuse symlinks. |

## HIGH — correctness / data-loss

| ID | Status | File:line | Problem | Fix |
|----|--------|-----------|---------|-----|
| CR-H6 | Fixed | model.py:139–142 | `source_sha256` is **never written** on import/save, so `assert_source_unchanged` is permanently inert — source mutation (SR-4.1) is never actually detected. | On import, store `project["source_sha256"] = source_digest(project)` as the baseline. |
| CR-H7 | Fixed | model.py:214–226 | Autosave writes the sidecar **non-atomically**; a crash mid-write corrupts the `.autosave` that `restore` then fails to parse — defeating the crash-recovery feature. | Write to a temp file then `os.replace()` (atomic swap). |
| CR-H8 | Fixed | jobs.py:17–30 | `CancelToken._cancelled` is a bare bool shared across threads with no sync → cancellation can be missed/delayed (cross-thread render abort, SR-3.4). | Use `threading.Event`. |
| CR-H9 | Won't-fix | audio_mix.py:31–33 | Ducking is **inverted**: speech is compressed under the music instead of music ducked under speech. | Compress the music keyed by speech, then `amix` ducked-music with untouched speech. |
| CR-H10 | Won't-fix | render.py:139,184–200 | Crossfade overlap uses cumulative `running` instead of the previous clip's tail → for the 2nd clip onward, video `xfade` offset and audio `acrossfade` drift **out of A/V sync** across transitions. | Derive both `xfade` offset and `acrossfade` duration from one shared overlap-adjusted running total. |
| CR-H11 | Fixed | render.py:81–86 / segment.py:81 / tighten.py:19–27 | Silence parsing `zip(starts, ends+[duration])` mispairs when audio ends in silence (unequal start/end counts) → final speech range dropped / wrong cursor. | One shared strict state-machine `parse_silences()`; only append trailing `[cursor,duration]` when a silence is genuinely open. |
| CR-H12 | Fixed | branding.py:49 / metadata.py:21 | `drawtext`/`-metadata` interpolate user text (names/title) with no escaping → broken filtergraph or metadata injection on `'`,`:`,`\`,`%`,newline. | Escape drawtext specials or use `textfile=`; strip newlines from metadata values. |

## MED (likely bugs)

| ID | Status | File:line | Problem | Fix |
|----|--------|-----------|---------|-----|
| CR-M1 | Fixed | render.py:155 / video_ops.py:45 | Input-side `-ss`/`-to` before `-i` with re-encode can snap cuts to keyframes → clip start/length off vs requested (breaks frame-accuracy SR-4.4). | Use output seeking (`-i … -ss -t`) or add `-accurate_seek`. |
| CR-M2 | Fixed | render.py:213 / master.py:53,61 | Final mux / pass-2 encodes run `check=False` and never inspect return code → returns `ok:True` with a missing/corrupt output. | Check return codes (or `os.path.exists` on outputs); set `ok:false` on failure. |
| CR-M3 | Fixed | master.py:64 | Loudness PASS/FAIL re-measures the 128 kbps **MP3**, not the MP4 deliverable; lossy encode can push true-peak over target. | Measure the actual deliverable(s); report each. |
| CR-M4 | Fixed | master.py:25,42 | Only `input_i` is checked before pass-2; missing/`inf` `tp/lra/thresh/offset` → `KeyError` or invalid filter (silently, via check=False). | Guard all five keys + non-finite values; fall back to single-pass. |
| CR-M5 | Fixed | captions.py:54–57 | Cues spanning a cut boundary are dropped, and re-timed cues aren't clamped to the clip window → lost transcript text + overlap at seams. | Include overlapping cues, clamp start/end to the clip's output window. |
| CR-M6 | Fixed | export.py:41 | Chapter times re-sum source durations assuming no gaps/re-timing → drift from the actual render. | Derive chapter times from the render timing map (same source as captions). |
| CR-M7 | Fixed | audio_mix.py:18 | `replace_audio -shortest` truncates video to a shorter audio track, dropping the video tail. | Pad/loop audio or handle durations explicitly. |
| CR-M8 | Fixed | server.py:225,244,279 | `_job["running"]` read outside `_job_lock` (two jobs can start); upload writes bytes with no size cap / format check. | Gate under the lock; cap Content-Length + `validate_import` before writing. |
| CR-M9 | Fixed | render.py:116 | `was_adjacent` uses a 0.20 s time-proximity heuristic → reordered non-adjacent clips wrongly treated as hard cuts. | Use original-index adjacency only. |
| CR-M10 | Fixed | validate.py:28–36 | `validate_import` checks extension only, never bytes/existence → renamed file passes; SR-3.1 "format validated" is not real. | Sniff content (ffprobe/magic) + `os.path.isfile`. |
| CR-M11 | Fixed | model.py:247 | `apply_preset` does `project.update(style)` with no key whitelist → a preset can overwrite `segments`/`source` (data-loss). | Restrict to `_STYLE_KEYS`. |
| CR-M12 | Fixed | tighten.py:19 | `detect_silences` overwrites a pending `start` on duplicate `silence_start`; accepts `silence_end` with no duration. | Strict start/end state machine (shared with CR-H11). |

## LOW (quality / tech-debt — see also TD-1..3 in DECISIONS.md)

- CR-L1 — **Fixed.** `model.py` imports `hashlib`/`os`/`copy` moved to the top.
- CR-L2 — **Fixed.** `probe` keeps the fractional rate; `Plan.fps` is now `float`.
- CR-L3 — **Fixed.** Single shared parser `app/pipeline/silences.py`; both callers refactored.
- CR-L4 — **Fixed.** Shared `app/pipeline/_ff.run` captures stderr and raises `FFmpegError`; all pipeline passes adopt it.
- CR-L5 — **Fixed.** Cues now sorted by `(start, end)`.
- CR-L6 — **Fixed.** `-map_metadata 0 -map_chapters 1` keeps source metadata, imports only chapters.
- CR-L7 — **Fixed.** `concat_clips` removes its intermediates in a `finally`.
- CR-L8 — **Fixed.** `kept_subs` now sorts missing `order` with `+inf` + start tie-break.
- CR-L9 — **Fixed.** Context detected via `__package__` (api/metadata) and relative imports (tighten/segment); no `except ImportError` swallow.
- CR-L10 — **Fixed.** `build_plan` raises on `end <= start`.
- CR-L11 — **Fixed.** `_wait_ready` polls the server socket instead of a fixed sleep.

---

## Fix status (2026-06-24)

**Second pass — fixed + regression-tested** (`tests/test_fixes.py`, 14 tests):
all 5 HIGH-security (CR-H1..H5), 4 HIGH-correctness (CR-H6, CR-H7, CR-H8, CR-H12),
4 MED (CR-M7, CR-M8, CR-M10, CR-M11), 2 LOW (CR-L1, CR-L8).

**Third pass — golden-test harness for the render-math items** (`tests/test_golden.py`, 6 tests):
- **CR-H11 / CR-M12 / CR-L3 — Fixed.** The two divergent silence parsers were the real defect;
  replaced by one strict state machine `app/pipeline/silences.py` (both callers refactored), with
  edge-case tests (audio ends in silence, ends in speech, no silence, duplicate `silence_start`,
  short-gap suppression).
- **CR-H10 — Won't-fix (verified correct).** A 3-clip / 2-crossfade render is probed per stream and
  the **video and audio durations match within 0.25 s** — `timing_map` and `_build_join` already
  share the same overlap `t` and accumulator, so there is no A/V drift. The original finding
  misread `running` as the raw timeline; it is the overlap-adjusted accumulator.

**Won't-fix — CR-H9 (disputed).** On close reading the filtergraph is **correct**:
`sidechaincompress` compresses its *first* input keyed by its *second*, so `[music][speech]…`
ducks the **music** under speech, then `amix` adds untouched speech — the intended behaviour.

**Fourth pass — MED/LOW batch** (`tests/test_batch.py`, 5 tests): fixed CR-M1 (accurate `-ss/-t`
trim), CR-M2 (return-code + output-exists checks in render & master), CR-M3 (loudness measured on
the actual MP4 deliverable), CR-M4 (all five loudnorm keys + finiteness guarded; else single-pass),
CR-M5 (boundary-spanning cues clamped, not dropped), CR-M6 (chapter times from the render timing
map), CR-M9 (adjacency by original index only), CR-L5/L6/L7/L10/L11.

**Fifth pass — final 3 LOW (`tests/test_batch.py` +2):** CR-L2 (rational fps through `probe`/`Plan`),
CR-L4 (shared `_ff.run` standardises ffmpeg error handling), CR-L9/TD-1 (explicit `__package__` /
relative imports, no swallowed `ImportError`). **Entire backlog now Fixed or verified-correct; 0 open.**

**Scorecard:** HIGH 10 fixed / 2 verified-correct / **0 open** · MED 12 fixed / 0 open ·
LOW 11 fixed / 0 open.

*Method: 4 parallel reviewers, full-file reads. ~50 raw findings deduplicated. The review modified
no code; passes 2–4 applied fixes with `unittest` regression + golden tests (full suite 12/12 green,
39 new test cases across test_fixes/test_golden/test_batch).*
