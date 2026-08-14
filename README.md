# Hermanos Tatis — Flyer de Reseñas

Single-file HTML flyer with a QR code for diners to review **Restaurante Hermanos Tatis** (Manzanillo del Mar, Cartagena) on Google.

## Run

```bash
open flyer-review.html   # macOS (or xdg-open / start)
python3 file.py          # local server + opens the flyer (Ctrl+C to stop)
```

Needs internet the first time (fonts and QR library load from CDNs).

## Customize

Edit `flyer-review.html`:

- **Review link** — set `REVIEW_URL` (bottom of the file), then reload.
- **Text** — inside `<main class="flyer">`.
- **Colors** — the `:root` CSS variables.

## Print

Click **Imprimir / PDF** (or Cmd/Ctrl+P) → Save as PDF. A4 print styles are built in.

## Files

```
flyer-review.html   # the flyer (markup + styles + QR)
file.py             # local dev server
```
