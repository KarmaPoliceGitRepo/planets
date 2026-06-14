# ⭐ Quickstart — Make a Podcast (the 12-year-old version)

> **Read this if you want the shortest path.** 10 steps. No big words. Free.
> If a step has a 🤖 it means "a helper script does the hard part for you".
> Ask a grown-up to help make the accounts (rule **CR-5**).

---

## 🧰 Before you start (one time only)
1. Install **3 free apps**: **OBS Studio**, **Audacity**, and **Python**.
   *(Links and a checker are in [`01-tools-and-environment.md`](01-tools-and-environment.md).)*
2. Make **3 free accounts** (with a grown-up): **Spotify for Creators**,
   **YouTube**, and **Google Drive** (for backups).

🤖 Or run this once to set things up and check everything:
```bash
bash scripts/setup.sh
```

---

## 🎬 The 10 steps to one episode

**1. Make a folder for the episode** 🤖
```bash
bash scripts/new_episode.sh 01 "The Missing Link"
```
This builds a tidy folder with spots for everything.

**2. Pick what to say.**
Open [`../03-content/episode-01-the-missing-link.md`](../03-content/episode-01-the-missing-link.md)
and read it out loud once for practice.

**3. Get ready to record.**
- Sit close to your **microphone** (one hand away).
- Quiet room, soft things around you (less echo).
- Light **in front of your face** for the **camera**.

**4. Record.**
- Open **OBS**, press **Start Recording**, **clap once**, then talk.
- Stay quiet for **10 seconds first** (this helps clean the sound later).
- Press **Stop**. Move the video file into your episode's `raw/` folder.

**5. Clean it up in Audacity.**
- Open Audacity → **File → Import → Audio** → your recording.
- Cut out the bits you don't like (select with the mouse, press **Delete**).
- Add fun **intro music** (free music from the **YouTube Audio Library**).
- **File → Export → WAV** → save it as `working/episode_premaster.wav`.

**6. Make it sound pro** 🤖
```bash
bash scripts/process_episode.sh episodes/01-the-missing-link
```
Wait for it to say **PASS** ✅. Now you have `episode.mp3` and `episode.mp4`.

**7. Make subtitles** 🤖
```bash
bash scripts/transcribe.py episodes/01-the-missing-link
```
This writes the words out so deaf listeners can read along.

**8. Make a cover picture.**
In **Canva**, pick a "Podcast Cover", type **The Missing Link**, download as
**PNG** (size **1400×1400**). Put it in the `assets/` folder.

**9. Put it online.**
- Audio: **Spotify for Creators → New episode → upload `episode.mp3`** → add a
  title + a few sentences → **Publish**. (It also sends your show to Apple!)
- Video: **YouTube → Upload → `episode.mp4`** → add the subtitles file
  (`captions/episode.srt`).

**10. Save a copy + share.**
- Drag your whole episode folder into **Google Drive** (so you never lose it).
- Post a short clip and say *"New episode out now!"*

🎉 **You did it.** Do steps 1–10 again next week for episode 2.

---

## 😟 If something goes wrong

| Problem | Fix |
|---|---|
| "command not found: ffmpeg" | Run `bash scripts/setup.sh` and follow what it prints. |
| The script says **FAIL** | It tells you why — usually your recording was too quiet/too loud, or too long. Re-record a bit closer, or trim it shorter. |
| No terminal / too scary | Use **Auphonic.com** (free) to clean the audio instead — drag your WAV in, turn on "Loudness −16 LUFS", download the MP3. |
| Echoey sound | Record in a smaller room with soft things (clothes, bed, sofa). |
| Buzzing/hiss | Turn off fans/AC; record 10 s of silence and use Audacity's **Noise Reduction**. |

> 🌟 **Golden rule:** done is better than perfect. Episode 1 will not be your
> best — episode 10 will be way better because you *kept going.*
