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

One row per stakeholder (listed **once**). Group membership is **many-to-many** and
is captured separately in the matrix (§1.3) — a single stakeholder often sits in
several groups (e.g. a distribution platform is at once a technical host, a
rules-setter, and a revenue channel). `Power`/`Interest` keep the High/Med/Low
rating used for engagement strategy.

| # | Stakeholder | Interest | Power | Interest | Strategy |
|---|---|---|---|---|---|
| S1 | Host / Creator (you) | Tell the story, build audience, drive the agenda | High | High | **Manage closely** (owner) |
| S2 | Listeners — Nepali diaspora | Stay connected to home; ideas to invest/return | Low | High | Keep satisfied & informed |
| S3 | Listeners — Nepalis at home (youth weighing migration) | Hope; practical paths to stay & earn | Low | High | Keep satisfied & informed |
| S4 | Listeners — international (trekkers, Nepal-curious) | Travel inspiration, ethical tourism | Low | Med | Keep informed |
| S5 | Guests / interviewees / SMEs | Be heard; promote their cause/business | Med | High | **Manage closely** |
| S6 | Local guides & tourism operators (Mustang/Manang) | Visibility, income, future app/licensing | Med | High | **Manage closely** |
| S7 | Villagers / migrants / their families | Be represented fairly and with dignity | Low | Med | Ethical duty |
| S8 | Distribution platforms (Spotify for Creators, Apple Podcasts, YouTube) | Host & expose the show; you obey their rules; they share ad revenue | High | Low | **Keep satisfied** (ToS) |
| S9 | Free-tool providers (Audacity, OBS, Auphonic, Canva, Whisper) | Adoption; you rely on their free tiers | Med | Low | Avoid lock-in |
| S10 | Rights holders / licensing bodies (music/image copyright; PRS/PPL/labels) | Their work isn't used without a licence | Med | Low | **Keep satisfied** (free-to-use only) |
| S11 | Accessibility users (deaf/HoH, non-Nepali/English speakers) | Captions, transcripts, bilingual content | Low | Med | Design for them |
| S12 | Future sponsors / funders (tourism board, NGOs, diaspora orgs) | Reach, impact, brand alignment | Med | Low | Be sponsor-ready |
| S12b | Tourism Guide Platform (future venture, promoted by the show) | Awareness, community, call-to-action reach | Med | Med | Design to promote |
| S13 | Helpers (editor friend/sibling; parent approving a minor's accounts) | Easy, low-effort tools | Low | Med | Usability matters |
| S14 | Regulators / cultural norms / data laws (Nepali sensitivities, GDPR-type, age rules) | Lawful, respectful content | High | Low | **Keep satisfied** |
| S15 | Passive / discovery listeners | Be reached by recommendation & autoplay, not active search | Low | Med | Keep informed |
| S16 | Premium / offline listeners | Ad-free, offline, background playback | Low | Low | Keep informed |
| S17 | Advertisers / media agencies | Verifiable reach, targeting, brand safety | Med | Low | Keep satisfied |
| S18 | Direct-to-creator sponsors (host-read ads) | Verified impressions to validate reach | Med | Low | Keep satisfied |
| S19 | Hardware / devices (recording mic & camera; listener phones/speakers) | Format & codec compatibility | Med | Low | Keep compatible |
| S20 | Connectivity / ISP (in-field & at-home) | Bandwidth for upload and low-connectivity recording | Low | Low | Design around it |
| S21 | Platform Trust & Safety / ToS / age-rating | Content meets community guidelines | High | Low | **Keep satisfied** |
| S22 | Interfacing social platforms (TikTok, Instagram, X) | Clean embeddable previews + native vertical formatting | Low | Low | Design clips to fit |

## 1.3 Group membership matrix (a stakeholder may sit in several groups)

Groups classify by **relationship to the system**; a stakeholder is assigned to
**every** group whose relationship it holds. The collective need of *each* group it
joins applies to it.

- **G1 Audience** · **G2 Content originators** · **G3 Subjects & beneficiaries** ·
  **G4 Financial & sponsoring** · **G5 Technical enablers** · **G6 Regulatory & interfacing**

| # | Stakeholder | G1 | G2 | G3 | G4 | G5 | G6 |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|
| S1 | Host / Creator | | ✓ | | | | |
| S2 | Diaspora listeners | ✓ | | | | | |
| S3 | At-home listeners | ✓ | | | | | |
| S4 | International listeners | ✓ | | | | | |
| S5 | Guests / SMEs | | ✓ | ✓ | | | |
| S6 | Local guides / operators | | ✓ | ✓ | | | |
| S7 | Villagers / families | | | ✓ | | | |
| S8 | Distribution platforms | | | | ✓ | ✓ | ✓ |
| S9 | Free-tool providers | | | | | ✓ | |
| S10 | Rights holders / licensing | | | | | | ✓ |
| S11 | Accessibility users | ✓ | | | | | |
| S12 | Sponsors / funders | | | | ✓ | | |
| S12b | Promoted venture | | | ✓ | ✓ | | |
| S13 | Helpers | | ✓ | | | | |
| S14 | Regulators / culture / law | | | | | | ✓ |
| S15 | Discovery listeners | ✓ | | | | | |
| S16 | Offline / premium listeners | ✓ | | | | | |
| S17 | Advertisers / agencies | | | | ✓ | | ✓ |
| S18 | Direct-to-creator sponsors | | | | ✓ | | |
| S19 | Hardware / devices | | | | | ✓ | |
| S20 | Connectivity / ISP | | | | | ✓ | |
| S21 | Platform Trust & Safety | | | | | | ✓ |
| S22 | Interfacing social platforms | ✓ | | | | ✓ | ✓ |

> **Multi-group examples:** S8 platform → G4 (ad revenue) + G5 (hosting) + G6 (ToS);
> S5 guest → G2 (contributes content) + G3 (subject/beneficiary); S22 social → G1
> (discovery) + G5 (interface) + G6 (cross-post rules); S12b venture → G3 + G4.

## 1.4 Collective needs (one per group)

Each group shares a **collective need**; the specialised stakeholders inherit and
refine it. These are the parents the detailed needs in `02-stakeholder-needs.md`
trace up to.

| ID | Group | Collective need — *"The ‹group› needs …"* |
|---|---|---|
| **CN-G1** | Audience | to easily find, play, and follow relevant episodes — reliably, accessibly, on their chosen platform and device. |
| **CN-G2** | Content originators | to plan, record, edit, and publish quality episodes at zero cost and low skill, with fair attribution. |
| **CN-G3** | Subjects & beneficiaries | to be represented fairly and with dignity, and to gain visibility, income, or support from the exposure. |
| **CN-G4** | Financial & sponsoring | to receive verifiable reach/impact and brand-safe alignment for their money. |
| **CN-G5** | Technical enablers | to exchange standards-conformant, compatible inputs/outputs without lock-in and within free tiers & low connectivity. |
| **CN-G6** | Regulatory & interfacing | to ensure content is lawful, licensed, age-appropriate, culturally respectful, and cleanly shareable across platforms. |

## 1.5 Power/Interest map (text form)

```
              INTEREST →
              Low                         High
  P    High   S8 Platforms · S21 T&S      S1 Host
  O           S14 Regulators              S5 Guests · S6 Guides
  W    ───────────────────────────────────────────────
  E    Low    S9 Tools · S10 Rights       S2/S3 Listeners · S4 Intl
  R           S12 Sponsors · S17/S18 Ads  S7 Subjects · S11 Accessibility
              S19 HW · S20 ISP · S22 Soc  S13 Helpers · S12b Venture
```

- **Manage closely (High/High):** Host, Guests, Local guides.
- **Keep satisfied (High power):** Platforms, Trust & Safety, Regulators, Rights holders.
- **Keep informed (High interest):** all listener groups, subjects, accessibility users, helpers.

## 1.6 Key insights that will drive requirements

1. **The owner is likely a beginner / possibly young** ("a 12-year-old can use it") → *usability and zero-cost are first-class requirements, not nice-to-haves.*
2. **Listeners are bilingual (Nepali + English) and global** → *language and accessibility (captions, transcripts) matter.*
3. **Platforms and rights holders have real power to remove the show** → *legal/ToS compliance and royalty-free assets are hard constraints.*
4. **Content depends on guests in remote places** → *the system must support remote and in-field (low-connectivity) recording.*
5. **The show promotes a real venture** (guides app) → *the podcast must be able to host a call-to-action / community channel.*

➡️ Next: turn these stakeholders into **needs** in
[`02-stakeholder-needs.md`](02-stakeholder-needs.md).
