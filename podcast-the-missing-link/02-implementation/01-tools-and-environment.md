# Implementation · 1 · Tools & Environment Setup

> This is the **shopping list** (everything free) and the **install once** guide.
> You only do this section **once**. After that, jump to recording.
> Maps to physical components **C1–C9** in
> [`../01-systems-engineering/06-physical-architecture.md`](../01-systems-engineering/06-physical-architecture.md).

## 1.1 What you already have ✅
- 🎤 A **microphone** (USB mic, headset, or even phone earbuds with a mic).
- 📷 A **camera** (webcam, phone, or DSLR).
- 💻 A **laptop or desktop** (Windows, Mac, or Linux).

## 1.2 Free software to install (the "studio")

| # | Tool | Get it from | Used for |
|---|---|---|---|
| 1 | **OBS Studio** | obsproject.com | Record camera + mic + screen (video) |
| 2 | **Audacity** | audacityteam.org | Edit & clean audio |
| 3 | **FFmpeg** | ffmpeg.org (or via the setup script) | Auto-master & export (used by our scripts) |
| 4 | **Python 3** | python.org | Runs the transcript script |
| 5 | *(optional)* **Git** | git-scm.com | Already here if you cloned this repo |

> 🍎 **Mac shortcut:** instead of OBS you can use the built-in **QuickTime
> Player** and **GarageBand**. The scripts still work.

## 1.3 Free accounts to create (the "broadcast")

| # | Account | Site | Used for | Note |
|---|---|---|---|---|
| 1 | **Spotify for Creators** | creators.spotify.com | Host audio + auto RSS → Spotify/Apple | Was "Anchor" |
| 2 | **YouTube** (a Google account) | youtube.com | Video host + discovery | Use a brand channel |
| 3 | **Cloud backup** | drive.google.com / mega.nz | Off-device backup (FR-11) | 15–20 GB free |
| 4 | **Canva** | canva.com | Cover art + clips | Free tier |
| 5 | *(optional)* **Riverside.fm** | riverside.fm | Remote guest recording | Free tier |

> 🔒 **If the creator is under 18 (CR-5):** a parent/guardian creates and owns
> these accounts and supervises uploads. Check each platform's minimum age.

## 1.4 One-command environment check (recommended)

Open a **Terminal** (Mac/Linux) or **Git Bash / WSL** (Windows), `cd` into this
folder, and run:

```bash
cd podcast-the-missing-link
bash scripts/setup.sh
```

The script will:
- check whether **FFmpeg** and **Python 3** are installed,
- print the exact install command for **your** operating system if something is missing,
- install the Python transcript helper (Whisper) into a local virtual environment,
- create the `episodes/` working folder.

> If you'd rather not touch the terminal at all, you can do **everything** with
> the GUI apps (OBS, Audacity, and **Auphonic** for mastering). The scripts are a
> faster, repeatable shortcut — not a requirement.

## 1.5 Folder convention (so nothing gets lost — F3)

Each episode lives in its own folder, created by `new_episode.sh`:

```
episodes/
└── 01-the-missing-link/
    ├── raw/              ← original recordings (never edit these)
    ├── assets/           ← music, images + LICENSES.md (CR-1)
    ├── working/          ← Audacity project, rough cuts
    ├── exports/          ← episode.mp3, episode.mp4
    ├── captions/         ← episode.txt, episode.srt
    ├── show-notes.md     ← description, chapters, CTA, credits
    └── test-log.md       ← the V&V checklist (from doc 07)
```

## 1.6 Royalty-free asset sources (stay legal — CR-1)

| Need | Free source |
|---|---|
| 🎵 Music / stings | YouTube Audio Library, Pixabay Music, Free Music Archive, Incompetech (CC-BY) |
| 🔊 Sound effects | Freesound (check each licence), Pixabay |
| 🖼️ Images | Unsplash, Pexels, Pixabay |
| 🅰️ Fonts | Google Fonts |

**Always** save the source link + licence into `assets/LICENSES.md`. The
`new_episode.sh` script creates that file for you with a template.

➡️ Next: [`02-recording-setup.md`](02-recording-setup.md).
