# 1 · Stakeholder Identification & Analysis

> **SE step:** *Stakeholder identification* — the very first activity. Before we
> decide what to build, we list **everyone affected by or interested in** the
> podcast, and understand what each one wants. Miss a stakeholder here and you
> get a nasty surprise later (e.g. forgetting "platform rules" → your show gets
> removed for using copyrighted music).

## 1.1 What is the "system"?

- **System of Interest (SoI):** *The Missing Link Podcast Production & Distribution System* — everything needed to plan, record, edit, publish and grow the show.
- **Enabling systems:** free software, internet, hosting platforms, the laptop.
- **Context / future system:** the **Tourism Guide Platform** (licensing + Uber-like app). It is the *subject* of the show and a future venture; it is **out of scope to build here** but kept in view because the podcast must explain and promote it.

## 1.2 Stakeholder register

Each stakeholder has an **interest** (what they get) and an **influence** (how
much they can shape the system). We use a simple **Power/Interest** rating
(High/Med/Low) to decide who we *manage closely* vs. *keep informed*.

| # | Stakeholder | Type | Interest in the podcast | Power | Interest | Strategy |
|---|---|---|---|---|---|---|
| S1 | **Host / Creator** (you) | Primary | Tell the story, build an audience, drive the village/tourism agenda | High | High | **Manage closely** (this is the owner) |
| S2 | **Listeners — Nepali diaspora** | Primary | Stay connected to home; ideas to invest/return | Low | High | **Keep satisfied & informed** |
| S3 | **Listeners — Nepalis at home** (esp. youth weighing migration) | Primary | Hope, practical paths to stay & earn | Low | High | **Keep satisfied & informed** |
| S4 | **Listeners — international (trekkers, Nepal-curious)** | Secondary | Travel inspiration, ethical tourism | Low | Med | Keep informed |
| S5 | **Guests / interviewees** (returnees, villagers, guides, economists, geothermal/energy experts, movement figures) | Primary | Be heard; promote their cause/business | Med | High | **Manage closely** (content depends on them) |
| S6 | **Local guides & tourism operators** (Mustang/Manang) | Subject + beneficiary | Visibility, income, future app/licensing | Med | High | **Manage closely** |
| S7 | **Villagers / migrants / their families** | Subjects of the story | Be represented fairly and with dignity | Low | Med | Keep informed; ethical duty |
| S8 | **Distribution platforms** (Spotify for Creators, Apple Podcasts, YouTube) | Enabling | You follow their rules; they host & expose your show | High | Low | **Keep satisfied** (obey ToS) |
| S9 | **Free-tool providers** (Audacity, OBS, Auphonic, Canva, Whisper) | Enabling | Adoption; you rely on their continued free tiers | Med | Low | Keep informed; avoid lock-in |
| S10 | **Rights holders** (music/image copyright owners) | Constraint | Their work isn't used without a licence | Med | Low | **Keep satisfied** (use only free-to-use assets) |
| S11 | **Translators / accessibility users** (deaf/hard-of-hearing, non-Nepali/non-English speakers) | Secondary | Captions & bilingual content | Low | Med | Keep informed; design for them |
| S12 | **Future sponsors / funders** (tourism board, NGOs, diaspora orgs) | Future | Reach, impact, brand alignment | Med | Low | Watch; design to be sponsor-ready |
| S13 | **Helpers** (a friend/sibling who edits, a parent who approves accounts for a minor) | Enabling | Easy, low-effort tools | Low | Med | Keep informed; usability matters |
| S14 | **Regulators / cultural norms** (Nepali content sensitivities, platform age rules, data laws) | Constraint | Lawful, respectful content | High | Low | **Keep satisfied** |

## 1.3 Power/Interest map (text form)

```
              INTEREST →
              Low                         High
  P    High   S8 Platforms               S1 Host
  O           S14 Regulators             S5 Guests · S6 Guides
  W    ───────────────────────────────────────────────
  E    Low    S9 Tools · S10 Rights      S2/S3 Listeners
  R           S12 Sponsors               S4 Intl · S7 Subjects
                                         S11 Accessibility · S13 Helpers
```

- **Manage closely (High/High):** Host, Guests, Local guides.
- **Keep satisfied (High power):** Platforms, Regulators, Rights holders.
- **Keep informed (High interest):** all listener groups, subjects, accessibility users, helpers.

## 1.4 Key insights that will drive requirements

1. **The owner is likely a beginner / possibly young** ("a 12-year-old can use it") → *usability and zero-cost are first-class requirements, not nice-to-haves.*
2. **Listeners are bilingual (Nepali + English) and global** → *language and accessibility (captions, transcripts) matter.*
3. **Platforms and rights holders have real power to remove the show** → *legal/ToS compliance and royalty-free assets are hard constraints.*
4. **Content depends on guests in remote places** → *the system must support remote and in-field (low-connectivity) recording.*
5. **The show promotes a real venture** (guides app) → *the podcast must be able to host a call-to-action / community channel.*

➡️ Next: turn these stakeholders into **needs** in
[`02-stakeholder-needs.md`](02-stakeholder-needs.md).
