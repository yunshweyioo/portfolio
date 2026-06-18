# Portfolio Redesign — "Dreamy Editorial" Design Spec

**Date:** 2026-06-17
**File:** `yun_oo_portfolio.html` (single self-contained HTML file, no build step)
**Goal:** Re-imagine the visual design of Yun Oo's portfolio in a soft, painterly-editorial style — keeping all existing content and the single-file architecture, restyling every section.

---

## 1. Design language

Soft, warm, painterly-editorial. Calm and elegant with small organic touches. Inspired by a dreamy creative-portfolio reference (cream + sky, serif display, watercolor artwork). Adapted to a production-coordinator voice — refined, not influencer-casual.

**Hard constraints**
- Stays one self-contained `yun_oo_portfolio.html` file.
- All current content/sections preserved (hero, stats, timeline, case studies, about, skills, education, contact).
- All artwork is **inline SVG** (no external image assets beyond the existing embedded photo) so the file stays portable. A real painted image may be swapped in later if desired.

---

## 2. Palette

| Token | Light | Notes |
|---|---|---|
| `--bg` cream | `#f4eee2` | page background |
| hero gradient | `#cdddea → #dfe6e0 → #f1ead8 → #f4eee2` (170deg) | dreamy sky→cream |
| `--ink` (main text) | `#2b2018` | **dark brown — primary text color** |
| `--ink-soft` | `#5a4636` / `#4a3a2c` | body copy |
| `--accent` terracotta | `#c2552f` | wordmark, links, ✦, italic emphasis, timeline dots, "Winnie" |
| accent-deep | `#b06a3f` / `#a05a34` | secondary terracotta (kicker labels, emphasis words) |
| `--muted` | `#8a7558` | small caps labels, captions |
| hairline | `#d8ccb6` | rules, dividers |
| sage | `#aeb289` | subtle organic outlines |
| watercolor | periwinkle `#aab2dd`, blush `#f6dccd`/`#f0cbb8`, core red-orange `#e0492a`/`#e85a2a`, amber `#ecab4f` | logo bloom + photo wash |

**Dark mode ("warm dusk"):** deep brown canvas `#241a14` / surface `#3a2a20`; text blush `#e9cdbb`; accents lighter terracotta `#d98a5c` + periwinkle `#9aa6d8`. Toggle stays in nav (◐).

---

## 3. Typography

- **Display serif:** keep **DM Serif Display** for big headings ("Hello! I'm Yun.", section statements). High-contrast, italic for emphasis words.
- **Wordmark / logo:** **Pinyon Script** (Google Font), terracotta, "Yun Oo" with caps **Y** and **O**. Formal pointed-pen calligraphy.
- **Body / labels:** **DM Sans** (keep). Uppercase letter-spaced kickers and captions.
- New Google Fonts to add to `<head>`: `Pinyon+Script`.

---

## 4. Logo lockup

- **Wordmark:** "Yun Oo" in Pinyon Script, terracotta, ~ display size in hero / smaller in sticky nav.
- **Watercolor bloom:** inline SVG (periwinkle wash + blush petals + red-orange/amber center) with watery feathered edges via an SVG `feTurbulence` + `feDisplacementMap` + `feGaussianBlur` filter. The bloom **hangs to the left** of the text, offset on its own.
- **Role line:** `PRODUCTION COORDINATOR ✦ SAN FRANCISCO` (DM Sans, uppercase, letter-spaced, muted) sits **directly under the wordmark, sharing the same left edge** as "Yun Oo" (flower offset further left).
- Implementation: relative container with left padding; flower absolutely positioned hanging left; wordmark + role left-aligned in the text column.

---

## 5. Section-by-section

### Nav (sticky)
`Work ✦ Case Studies ✦ About ✦ Contact` with terracotta ✦ separators, plus a `◐ Dark` mode toggle pill. Logo lockup (wordmark + role) on the left.

### Hero
- Background: dreamy sky→cream gradient in a large rounded panel.
- **Headline:** "Hello! 👋 / I'm Yun." (DM Serif Display, large, dark brown).
- **Warm subline:** *"— though most people call me Winnie."* ("Winnie" in terracotta). Italic.
- **Name approach:** **Yun professionally, Winnie warmly** — logo + all credits stay "Yun Oo" (matches IMDb/résumé); hero greeting surfaces "Winnie" as the personal touch.
- **Intro:** one tight sentence — "I turn the chaos of previs & postvis into something calm, clear, and on schedule."
- **Actions:** `GET IN TOUCH` (dark-brown pill) + `Résumé ↓` (text link, terracotta underline).
- **Portrait:** existing photo masked into a **watercolor-feathered organic blob** (turbulence filter), with a soft periwinkle/blush wash bleeding behind it. Replaces the old hard cloud shape.
- Removed: the "So glad you stopped by" kicker.

### Stats bar (replaces the curved running-text band)
Horizontal row, hairline top/bottom rules, four stats with serif numbers + DM Sans caption:
`20 Productions` · *`Zero`* `Missed Deadlines` (Zero in italic terracotta) · `3.5 yrs @ The Third Floor` · `50+ Artists Coordinated`.

### Work (Case Studies feature row)
Heading: "A few of the *shows* I've helped bring to life" (italic "shows"). Three soft rounded image cards — **The Fantastic Four** (Marvel Studios), **Monarch: Legacy of Monsters** (Apple TV+), **Venom: The Last Dance** (Sony Pictures). Caption = show title + studio only (no "Visualization Coordinator").

### Career Timeline (full + show-all)
Vertical timeline, hairline rail, terracotta dots, serif year markers. **All credits**, grouped by year, with a `Show all credits ↓` / `Show less ↑` toggle (later years collapsed by default). Full list:

- **2026:** For All Mankind (Apple TV+) · Send Help (20th Century Studios)
- **2025:** The Fantastic Four: First Steps (Marvel) · Superman (Warner Bros.) · Thunderbolts* (Marvel) · Predator: Badlands (20th Century) · The SpongeBob Movie (Paramount) · The Gorge (Apple TV+) · Toyota USA: Grip (Intertrend) · Sphere Project: Illenium — Odyssey (Woodblock/Sphere)
- **2024:** Venom: The Last Dance (Sony) · Godzilla X Kong: The New Empire (Warner Bros.) · Kraven the Hunter (Sony) · Carnival Tropicale (Carnival Cruise)
- **2023:** Monarch: Legacy of Monsters (Apple TV+) · Echo (Marvel/Disney+) · Loki (Marvel/Disney+) · Murder Mystery 2 (Netflix)
- **2022:** Whitney Houston: I Wanna Dance (Sony) · White Noise (Netflix)

Each row keeps its tag (Series / Feature / Live Event / Commercial) and role where relevant.

### Experience
Keep existing roles/bullets (The Third Floor, Turncoat Pictures, Marina Studios), restyled: serif role titles, hairline meta column, DM Sans bullets.

### About + Skills
- **About:** short warm paragraph, serif, dark brown.
- **Skills — categorized exactly like the résumé**, as clean italic-headed columns (NOT pill buttons):
  - *Production:* Workflow Coordination, Scheduling, Resource Allocation, Budget Tracking, Quality Control, Vendor Management, Stakeholder Communication, Cross-functional Collaboration
  - *Tools:* Asana, Trello, Notion, Confluence, ShotGrid / Flow, FileMaker Pro, ZoeLog
  - *Software:* Google Workspace, Microsoft Office, Adobe Creative Cloud
  - Category headers in italic terracotta with a hairline underline; items in DM Sans.

### Education
Keep: Syracuse University — S.I. Newhouse School of Public Communications, B.S. Visual Communications, Graduated May 2021 · GPA 3.72. Restyled to match.

### Studios row
"Trusted by" — `MARVEL ✦ APPLE TV+ ✦ WARNER BROS ✦ SONY ✦ PARAMOUNT` with terracotta ✦ separators, hairline rules.

### Contact / Footer
Watercolor bloom motif, closing line "Let's make something *clear*." (italic "clear"), short availability line, `GET IN TOUCH` dark-brown pill.

---

## 6. Motion

Gentle only: soft fade/rise on scroll reveal, subtle hover lifts on cards/buttons. **No bouncing letters** (the old kinetic hover was already removed). Respect `prefers-reduced-motion`.

---

## 7. Dark mode

Keep the existing toggle + `localStorage` persistence. Re-theme to the "warm dusk" palette (section 2). Verify the watercolor SVGs and hero gradient read well on the dark canvas; lighten accents as specified.

---

## 8. Out of scope

- No content rewriting beyond the small hero/section microcopy specified here.
- No framework migration — stays vanilla HTML/CSS/JS in one file.
- Real painted artwork swap-in: optional future enhancement, not this pass.
