# 🎙️ The Missing Link — End-to-End Podcast System

> *Why does no one give up on Nepal, yet everyone leaves?*
> A podcast about migration, villages, energy, and tourism — and a complete,
> free, beginner-friendly system to produce and publish it.

This folder is a **turn-key solution**. You bring a **camera and a microphone**.
Everything else — the plan, the tools, the scripts, the publishing pipeline, and
even the episode content — is set up here for you.

It is built using a real **systems engineering (SE) methodology**, so the
"why" behind every choice is documented and traceable, not just the "how".

---

## 📚 How this folder is organised

```
podcast-the-missing-link/
├── README.md                     ← you are here (start here)
├── 01-systems-engineering/       ← the "engineering brain": why we build it this way
│   ├── 01-stakeholders.md            who cares about this podcast
│   ├── 02-stakeholder-needs.md       what they need, in plain words
│   ├── 03-requirements.md            those needs turned into testable rules
│   ├── 04-concept-of-operations.md   a day-in-the-life of making an episode
│   ├── 05-functional-architecture.md what the system must DO (functions)
│   ├── 06-physical-architecture.md   the real tools that do each function
│   ├── 07-verification-validation.md how we prove it actually works
│   └── 08-traceability-matrix.md     need → requirement → function → tool → test
├── 02-implementation/            ← the "hands": do this, with free tools
│   ├── 01-tools-and-environment.md   the full free toolkit + accounts
│   ├── 02-recording-setup.md         how to record audio + video well
│   ├── 03-editing-workflow.md        clean up and assemble an episode
│   ├── 04-publishing-distribution.md get onto Spotify, Apple, YouTube
│   └── 05-kid-simple-quickstart.md   ⭐ the 12-year-old, 10-step version
├── 03-content/                   ← the "soul": what we actually say
│   ├── series-arc.md                 the whole season mapped out
│   ├── episode-01-the-missing-link.md the first full episode script
│   ├── show-notes-template.md        reusable show-notes / description
│   └── research-pack.md              facts, themes, and questions to explore
└── scripts/                      ← the "robot helpers": automation
    ├── setup.sh                      installs/checks the free software
    ├── new_episode.sh                creates a fresh episode folder
    ├── process_episode.sh            auto-cleans + loudness-normalises audio/video
    ├── transcribe.py                 makes transcripts & subtitles (accessibility)
    └── requirements.txt              the Python helpers needed
```

---

## 🚀 The 4 ways to use this

| You are… | Start with |
|---|---|
| **A 12-year-old / total beginner** | [`02-implementation/05-kid-simple-quickstart.md`](02-implementation/05-kid-simple-quickstart.md) |
| **Ready to record today** | [`02-implementation/02-recording-setup.md`](02-implementation/02-recording-setup.md) |
| **Curious about the engineering** | [`01-systems-engineering/01-stakeholders.md`](01-systems-engineering/01-stakeholders.md) |
| **Wanting to script episode 1** | [`03-content/episode-01-the-missing-link.md`](03-content/episode-01-the-missing-link.md) |

---

## 💡 The big idea (in one paragraph)

Many Nepalis love their country but leave it — not out of hatred, but out of
economic necessity. Leaders like **King Mahendra** once pushed a *"return to the
villages and build local infrastructure"* idea; figures associated with
**Gyanendra** echo versions of it today. **The Missing Link** asks: *what is
actually missing* between loving home and being able to stay? The series explores
concrete answers — **geothermal energy** (the natural hot springs / *tato pani*
and thermal vents), **high-value tourism** (trekkers paying £1,000+ for trips to
**Mustang** and **Manang**), and a **licensing + app system for local guides**
(an "Uber for trekking guides" that gives locals income security and takes only a
small platform fee). The podcast is the vehicle to investigate and popularise
these ideas.

> ⚖️ **Note on scope.** Two different "systems" live inside this idea:
> 1. **The Podcast Production System** — the thing we *engineer and build here*.
> 2. **The Tourism Guide Platform** (licensing + Uber-like app) — a future
>    real-world venture that is the *subject* of the show, not built in this folder.
>    It is captured as content and as a "context system" in the SE docs, with a
>    starter concept in [`03-content/research-pack.md`](03-content/research-pack.md).

---

## ✅ What "done" looks like

By following this folder you will be able to, **for $0**, publish a
professional-sounding, accessible (transcribed, bilingual-ready) audio **and**
video podcast to **Spotify, Apple Podcasts, and YouTube**, on a repeatable weekly
schedule, using tools simple enough for a child to operate.
