# 🌊 Hermanos Tatis — Flyer de Reseñas

A single-file, print-ready flyer that invites diners at **Restaurante Hermanos Tatis** (Manzanillo del Mar, Cartagena) to scan a QR code and leave a review on Google.

No build tools, no dependencies to install — just open the HTML file in a browser and you're done.

<p align="center">
  <img alt="HTML5" src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white">
  <img alt="CSS3" src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white">
  <img alt="No build step" src="https://img.shields.io/badge/build-none-brightgreen">
  <img alt="License" src="https://img.shields.io/badge/license-unspecified-lightgrey">
</p>

---

## ✨ Features

- **Zero setup** — one `.html` file, opens straight in any modern browser.
- **QR code generated on the fly** via [`qrcodejs`](https://github.com/davidshimjs/qrcodejs) (loaded from a CDN), wrapped in a “scan-me” corner frame.
- **One-click print** — a floating **Imprimir / PDF** button (screen only) fires the browser print dialog.
- **3-step guide** — *Escanea → Califícanos → ¡Gracias!* with icons so guests know exactly what to do.
- **Ocean-side branding** — fish emblem, layered waves, floating bubbles, custom palette, and Google Fonts.
- **Motion, done right** — subtle float/twinkle animations that respect `prefers-reduced-motion`.
- **Print & poster ready** — a `720 × 1020` canvas with A4 print styles that export cleanly to PDF or paper.
- **Fully in Spanish**, tailored to a Colombian seaside restaurant.

## 🚀 Quick start

```bash
# Clone the repo
git clone https://github.com/thany-8/mini_project.git
cd mini_project

# Open it — pick whichever works on your OS
open flyer-review.html        # macOS
xdg-open flyer-review.html    # Linux
start flyer-review.html       # Windows
```

> An internet connection is required the first time, because the fonts and the QR-code library are loaded from CDNs.

## 🛠️ Customization

Everything lives in **`flyer-review.html`**.

### 1. Point the QR code to your review link

Near the bottom of the file, update `REVIEW_URL`:

```js
var REVIEW_URL = "https://www.google.com/maps/search/?api=1&query=Restaurante+Hermanos+Tatis+Manzanillo+del+Mar+Cartagena";
```

For a **guaranteed direct review page**, replace it with the short link from your
Google Business Profile → **"Ask for reviews"** button, then reload the page to
regenerate the code.

### 2. Change the wording

Edit the text inside `<main class="flyer">`:

| Element        | Current text                                  |
| -------------- | --------------------------------------------- |
| Eyebrow        | `Manzanillo del Mar · Cartagena`              |
| Title          | `Hermanos Tatis`                              |
| Location       | `Restaurante frente al mar`                   |
| Call to action | `¡Déjanos tu reseña!`                         |
| Subtitle       | `Escanea el código con la cámara de tu celular…` |

### 3. Rebrand the colors

Tweak the CSS variables in the `:root` block:

| Variable  | Hex        | Role              |
| --------- | ---------- | ----------------- |
| `--deep`  | `#0B4A4E`  | Background base   |
| `--sand`  | `#F2E6C9`  | Text / QR card    |
| `--turq`  | `#2FA8A3`  | Accents & waves   |
| `--coral` | `#E4603F`  | Title shadow      |
| `--sun`   | `#F2C94C`  | CTA & stars       |

## 🖨️ Printing / exporting

1. Open the flyer in your browser.
2. Click the **🖨️ Imprimir / PDF** button (or press **Cmd/Ctrl + P**).
3. Choose **Save as PDF** (or send it to a printer).
4. Disable headers/footers for a clean result — the flyer already uses A4 print styling, and the toolbar button and animations are hidden automatically when printing.

## 📁 Project structure

```
mini_project/
└── flyer-review.html   # The entire flyer: markup, styles, and QR logic
```

## 📄 License

No license has been specified yet. Add one (e.g. MIT) if you plan to share or reuse this project.
