# LNG Contracts

Economic-terms comparison of LNG Sale and Purchase Agreements (SPAs), plus a Streamlit app
for browsing the comparisons interactively.

## Contents

- `contracts/` — full-text Markdown conversions of the underlying SPAs, plus two
  economic-terms comparison decks converted to Markdown:
  - `driftwood_lng_spa_economic_terms_comparison_formula_signature_updated.md` — Driftwood LNG
    (Vitol, Gunvor, Shell SPA1/SPA2)
  - `cheniere_sabine_pass_spa_standalone_economic_terms.md` — Cheniere Sabine Pass
    (BG, Gas Natural Fenosa, GAIL, Total)
- `app.py` — Streamlit app for browsing, filtering, and searching the comparisons.

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
