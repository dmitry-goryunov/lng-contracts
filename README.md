# LNG Contracts

Economic-terms comparison of LNG Sale and Purchase Agreements (SPAs), plus a Streamlit app
for browsing the comparisons interactively.

## Contents

- `contracts/` — full-text Markdown conversions of the underlying SPAs, plus three
  economic-terms comparison decks converted to Markdown:
  - `driftwood_lng_spa_economic_terms_comparison_formula_signature_updated.md` — Driftwood LNG
    (Vitol, Gunvor, Shell SPA1/SPA2)
  - `cheniere_sabine_pass_spa_standalone_economic_terms.md` — Cheniere Sabine Pass
    (BG, Gas Natural Fenosa, GAIL, Total)
  - `cheniere_followon_gdf_spa_economic_terms.md` — Cheniere follow-on & GdF
    (BG Gulf Coast A&R, Centrica, GNF Corpus Christi, Woodside, GdF Master Ex-Ship)
- `pptx/` — the source decks. The app displays these slide-for-slide (via `slide_images/`)
  and offers them for download. Where a deck's PNGs have not been exported yet, the app
  falls back to rendering the extracted slide text directly.
- `slide_images/driftwood/`, `slide_images/sabine_pass/` — each deck's slides pre-rendered to
  PNG by PowerPoint, so the app shows the real slides pixel-for-pixel rather than a
  reconstruction.
- `app.py` — Streamlit app for browsing, filtering, and searching the comparisons.
- `scripts/` — asset pipeline (Windows + PowerPoint required to regenerate):
  - `build_sabine_deck.py` — authors the Cheniere Sabine Pass deck from scratch in the same
    visual format as the Driftwood deck (see note below), plus extra slides for Cheniere-only
    economics (price architecture, UFC/MSC, embedded Xy, cancellation/suspension mechanics).
  - `build_followon_deck.py` — authors the Cheniere follow-on & GdF deck (BG Gulf Coast A&R,
    Centrica, GNF Corpus Christi, Woodside, GdF Master Ex-Ship) in the same visual format.
    Runs anywhere python-pptx is installed; title arcs are copied from the Driftwood deck when
    present, else approximated.
  - `extract_sabine_markdown.py` — regenerates `contracts/cheniere_sabine_pass_...md` from the
    built deck, so the app's search/text view stays in sync.
  - `export_slides.py` — copies both decks into `pptx/` and exports every slide to
    `slide_images/` via PowerPoint COM automation.

  Run in order after editing `build_sabine_deck.py`:
  ```bash
  python scripts/build_sabine_deck.py
  python scripts/extract_sabine_markdown.py
  python scripts/export_slides.py
  ```

  **Why the Sabine Pass deck is built, not just converted:** the original source file's native
  PowerPoint tables are encoded in a way real PowerPoint refuses to open ("PowerPoint could not
  open the file"), even though python-pptx, LibreOffice, and Google Slides all read it fine.
  Rather than ship a deck the user's own PowerPoint can't open, `build_sabine_deck.py`
  reproduces the Driftwood deck's exact design system (colors, fonts, table/card/badge layouts,
  extracted via `python-pptx`) and re-authors the Cheniere content on top of it as plain shapes
  instead of native tables.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy

Deployable as-is on [Streamlit Community Cloud](https://streamlit.io/cloud) — point it at
`app.py` in this repository.

## Disclaimer

This is an economic comparison, not a legal blackline. Redacted contract terms (`[***]`) are
never inferred.
