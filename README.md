# FURIA GT-88 — Apple-Style Scroll Experience

[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)
[![Architecture: Vanilla Scroll-Film](https://img.shields.io/badge/Architecture-Vanilla%20Canvas%20Scrubber-black.svg)](#architecture)
[![Tech: HTML5 / CSS3 / ES6](https://img.shields.io/badge/Tech-HTML5%20%7C%20CSS3%20%7C%20ES6-e85c52.svg)](#technology-stack)

> **"Pure wedge. Zero electronic interference. Just Modena steel."**

An Apple-style scroll-driven brand website for **FURIA GT-88** — a fictional 1980s Italian mid-engine wedge supercar with a red aluminum body, matte-black thermal engine cover louvers, motorized pop-up headlights, and an aggressive rear aerodynamic spoiler.

---

## 🌟 Overview

Inspired by Apple’s iconic product reveals (AirPods, Mac Pro), this project utilizes a **vanilla scroll-film canvas sequence architecture** scrubbed frame-by-frame as the user scrolls, seamlessly flowing into a complete editorial brand homepage below the film.

### Key Highlights
- **Frame-by-Frame Film Scrubbing**: 405 high-resolution WebP frames (1400px width) scrubbed dynamically via an HTML5 `<canvas>`.
- **Zero Framework Overhead**: Pure HTML5, CSS3, and modern vanilla JavaScript. No React, no Next.js, no heavyweight bundles.
- **Memory-Safe Architecture**: Uses blob prefetching and a sliding window cache of decoded `ImageBitmap` objects (keeps mobile and desktop RAM low).
- **Time-Based Lerp Velocity**: Custom exponential lerp smoothing (`1 - Math.exp(-dt * 11)`) ensures fluid gliding across mouse wheels, trackpads, and touch devices.
- **Full Brand Story Below Film**: The scroll film acts as the opening act, transitioning into an editorial brand page complete with sticky navigation, manifesto, craft deep-dives, specs, press quotes, and a photo gallery.

---

## 🎬 Cinematic Chapters

The opening scroll film is sliced into 5 distinct cinematic beats:

| Chapter | Scene / Focus | Visual Description | Caption |
| :--- | :--- | :--- | :--- |
| **0. Title** | Opening Stance | Hero stance anchored at top of page | **FURIA GT-88**<br>*Pure wedge. Zero electronic interference.* |
| **1. Detail** | Engine Louvers | Macro track over the black slatted rear engine deck | **Ten Slatted Louvers.**<br>*Direct thermal venting for the mid-mounted 5.2-litre V12.* |
| **2. Assembly** | Monocoque | Exploded components reverse-assemble in mid-air | **Hand-Built Monocoque.**<br>*Tubular spaceframe meets hand-formed aluminum panels.* |
| **3. Wing** | Aerodynamics | Profile glide across the high-downforce rear wing | **Uncompromising Downforce.**<br>*The iconic rear spoiler stabilizes 195 mph runs.* |
| **4. Lights** | Pop-Up Optics | Motorized pods raise to reveal quad beam projectors | **Concealed Optics.**<br>*Twin pop-up pods reveal quad halogen beam projectors.* |
| **5. Stance** | Wedge Beauty | Three-quarters low-angle stance of the finished car | **The Definitive Silhouette.**<br>*Wedge architecture perfected in 1988.* |
| **6. CTA** | Reservation Card | Analog fury call-to-action before the brand page | **FURIA GT-88**<br>*Analog fury. Strictly limited production. [Reserve Chassis]* |

---

## 🏎️ Brand Page Sections (Below the Film)

Past the 520vh film track, the page seamlessly transitions into the brand homepage:
1. **Sticky Nav**: Fades in with backdrop blur once the film finishes (`scrollY > filmEnd`). Includes anchor links to Story, Craft, Specs, Gallery, and an allocation CTA.
2. **Manifesto**: Huge typography declaring the mechanical, unassisted ethos of 1988.
3. **Origin Story**: Background on the 1988 Modena homologation run with split text/crop layout.
4. **Craft 01 & 02**: Deep dives into thermal venting architecture and retractable optics.
5. **Stats Strip**: Key performance figures (`455 HP`, `3.8s 0-60`, `1,380 kg`, `195 MPH`).
6. **Specifications Table**: Two-column breakdown of engine, valvetrain, carburetors, gearbox, chassis, and homologation details.
7. **Press Quotes**: Retrospective praise celebrating the purity of Modena's wedge era.
8. **Visual Archive Gallery**: Asymmetric 4-card masonry grid with hover micro-animations.
9. **Closing CTA Band & Footer**: Private chassis commission inquiry with legal fine print.

---

## 🛠️ Technology Stack

- **Markup & Layout**: Semantic HTML5, CSS Grid, Flexbox, CSS Variables.
- **Canvas Engine**: HTML5 2D Canvas context, `createImageBitmap`, `requestAnimationFrame`.
- **Image Pipeline**: FFmpeg (video scaling, crossfading, frame extraction) + Python Pillow (WebP compression & cropping).
- **Design System**:
  - Near-black background: `#0a0908`
  - Accent colors: Deep Modena Red (`#c9302c`) & Bright Red (`#e85c52`)
  - Typography: System Pro Display stack (`-apple-system`, `SF Pro Display`, `Segoe UI`, `Roboto`)

---

## 📂 Project Structure

```
FURIA_GT-88/
├── index.html            # Main site markup, styles, captions, and brand sections
├── main.js               # Canvas sequence scrubber and sliding bitmap cache
├── frames/               # 405 sliced WebP frames (~13.6 MB total)
│   ├── frames.json       # Manifest manifest (frame count and URL pattern)
│   └── frame_0001.webp … frame_0405.webp
├── assets/
│   ├── hero.jpeg         # Anchor hero still image
│   └── crops/            # Zoomed crops for craft and gallery sections
│       ├── crop-origin.webp
│       ├── crop-louvers.webp
│       ├── crop-lights.webp
│       └── gallery-1.webp … gallery-4.webp
├── scripts/
│   ├── build_master.py   # Crossfade video chapters and slice WebP frames
│   └── make_crops.py     # Generate image crops for below-film sections
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/asmaraf/FURIA_GT-88.git
cd FURIA_GT-88
```

### 2. Run Locally
No build step or node installation is required. Serve with Python or any static HTTP server:

```bash
# Using Python 3
python -m http.server 4185

# Or using Node.js / npx
npx serve .
```

Open **[[http://localhost:4185](https://furia-gt-88.vercel.app/)]** in your browser.

---

## 🌐 Deploying to GitHub Pages

Because this is a zero-build static site, it can be deployed directly via GitHub Pages:
1. Go to your repository settings on GitHub: **Settings > Pages**.
2. Under **Build and deployment > Source**, select **Deploy from a branch**.
3. Under **Branch**, select `main` and `/ (root)`.
4. Click **Save**. Your site will be live within seconds!

---

## 📜 License & Disclaimers

- Fictional concept design and copy. All imagery generated using AI workflows.
- Not affiliated with any real automobile manufacturer.
- Open-source under the [MIT License](LICENSE).
