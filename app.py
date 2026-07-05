import html
import re
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

ROOT = Path(__file__).parent
CONTRACTS_DIR = ROOT / "contracts"
SLIDE_IMAGES_DIR = ROOT / "slide_images"
PPTX_DIR = ROOT / "pptx"

COMPARISONS = {
    "Driftwood LNG — Vitol / Gunvor / Shell": "driftwood_lng_spa_economic_terms_comparison_formula_signature_updated.md",
    "Cheniere Sabine Pass — BG / GNF / GAIL / Total": "cheniere_sabine_pass_spa_standalone_economic_terms.md",
}

COMPARISON_IMAGE_KEYS = {
    "Driftwood LNG — Vitol / Gunvor / Shell": "driftwood",
    "Cheniere Sabine Pass — BG / GNF / GAIL / Total": "sabine_pass",
}

COMPARISON_PPTX = {
    "Driftwood LNG — Vitol / Gunvor / Shell": "driftwood_lng_spa_economic_terms_comparison_formula_signature_updated.pptx",
    "Cheniere Sabine Pass — BG / GNF / GAIL / Total": "cheniere_sabine_pass_spa_standalone_economic_terms.pptx",
}

COMPARISON_BLURBS = {
    "Driftwood LNG — Vitol / Gunvor / Shell": (
        "Vitol, Gunvor, Shell SPA1 (JKM) & SPA2 (TTF) — merged, corrected economic-terms comparison."
    ),
    "Cheniere Sabine Pass — BG / GNF / GAIL / Total": (
        "BG, Gas Natural Fenosa, GAIL, Total — standalone economic-term comparison and valuation fields."
    ),
}

# Palette lifted from the source decks (navy headers, pastel RAG pills, zebra rows).
NAVY = "#17324D"
SLATE = "#475569"
BODY = "#1E293B"
MUTED = "#8A94A3"
ACCENT_BLUE = "#2B5F8E"
ROW_ALT = "#F7F9FC"
BORDER = "#E5E9F0"

RAG_TEXT = {"RED": "#B3261E", "AMBER": "#B36B00", "GREEN": "#1A7F37", "NO RAG": "#667085"}
RAG_BG = {"RED": "#F8D8D5", "AMBER": "#FFF0D5", "GREEN": "#DDEFE2", "NO RAG": "#E2E5EA"}

SLIDE_RE = re.compile(r"^## Slide (\d+): (.+)$", re.MULTILINE)
TABLE_LINE_RE = re.compile(r"^\|.*\|$")
TABLE_SEP_RE = re.compile(r"^\|?\s*:?-{2,}.*-{2,}\s*\|?$")

CSS = f"""
<style>
h1, h2, h3 {{ color: {NAVY}; }}
.lng-hero-title {{
    color: {NAVY}; font-weight: 800; font-size: 2.6rem; line-height: 1.15; margin-bottom: 0.2rem;
}}
.lng-hero-subtitle {{ color: {SLATE}; font-size: 1.05rem; margin-bottom: 1.2rem; }}
.lng-slide-title {{
    color: {NAVY}; font-weight: 700; font-size: 1.5rem; margin-top: 1.6rem; margin-bottom: 0.4rem;
}}
.lng-footer {{ color: {MUTED}; font-size: 0.78rem; margin-top: 2.5rem; }}
.rag-pill {{
    display: inline-block; padding: 2px 12px; border-radius: 999px;
    font-weight: 700; font-size: 0.82rem; white-space: nowrap;
}}
.lng-table {{ width: 100%; border-collapse: collapse; margin: 0.6rem 0 1.1rem 0; font-size: 0.92rem; }}
.lng-table th {{
    background: {NAVY}; color: #FFFFFF; text-align: left; font-weight: 700;
    padding: 8px 12px; border: 1px solid {NAVY};
}}
.lng-table td {{ padding: 8px 12px; border-bottom: 1px solid {BORDER}; color: {BODY}; vertical-align: top; }}
.lng-table tr:nth-child(even) td {{ background: {ROW_ALT}; }}
.lng-card {{
    background: #FFFFFF; border: 1px solid {BORDER}; border-radius: 10px;
    padding: 1.1rem 1.3rem; box-shadow: 0 1px 3px rgba(23,50,77,0.08);
}}
.lng-card h4 {{ color: {NAVY}; margin-top: 0; }}
</style>
"""


def rag_key(value: str):
    v = str(value).strip().upper()
    return v if v in RAG_TEXT else None


def rag_pill_html(value: str) -> str:
    key = rag_key(value)
    if key is None:
        return html.escape(str(value))
    return (
        f'<span class="rag-pill" style="background:{RAG_BG[key]};color:{RAG_TEXT[key]};">'
        f"{html.escape(key)}</span>"
    )


@st.cache_data
def load_text(filename: str) -> str:
    return (CONTRACTS_DIR / filename).read_text(encoding="utf-8")


@st.cache_data
def list_contract_files():
    return sorted(p.name for p in CONTRACTS_DIR.glob("*.md"))


@st.cache_data
def list_slide_images(image_key: str):
    return sorted((SLIDE_IMAGES_DIR / image_key).glob("slide-*.png"))


@st.cache_data
def load_pptx_bytes(filename: str) -> bytes:
    return (PPTX_DIR / filename).read_bytes()


def parse_slides(text: str):
    matches = list(SLIDE_RE.finditer(text))
    intro = text[: matches[0].start()].strip() if matches else text.strip()
    slides = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        body = re.sub(r"\n?-{3,}\s*$", "", body).strip()
        slides.append({"num": m.group(1), "title": m.group(2).strip(), "body": body})
    return intro, slides


def split_blocks(body: str):
    blocks = []
    cur, cur_is_table = [], None
    for line in body.split("\n"):
        is_table_line = bool(TABLE_LINE_RE.match(line.strip()))
        if cur and is_table_line != cur_is_table:
            blocks.append((cur_is_table, "\n".join(cur)))
            cur = []
        cur.append(line)
        cur_is_table = is_table_line
    if cur:
        blocks.append((cur_is_table, "\n".join(cur)))
    return blocks


def md_table_to_df(block_text: str):
    rows = []
    for line in block_text.strip().split("\n"):
        line = line.strip()
        if not line or TABLE_SEP_RE.match(line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    if len(rows) < 2:
        return None
    header, *data = rows
    width = len(header)
    data = [(r + [""] * width)[:width] for r in data]
    return pd.DataFrame(data, columns=header)


def render_table_html(df: pd.DataFrame):
    rag_cols = [c for c in df.columns if c.strip().upper() == "RAG"]
    parts = ['<table class="lng-table"><thead><tr>']
    for col in df.columns:
        parts.append(f"<th>{html.escape(str(col))}</th>")
    parts.append("</tr></thead><tbody>")
    for _, row in df.iterrows():
        parts.append("<tr>")
        for col in df.columns:
            val = row[col]
            cell = rag_pill_html(val) if col in rag_cols else html.escape(str(val)).replace("\n", "<br>")
            parts.append(f"<td>{cell}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table>")
    return "".join(parts)


def render_text_block(text: str):
    for para in re.split(r"\n\s*\n", text):
        para = para.strip()
        if not para:
            continue
        if rag_key(para) is not None:
            st.markdown(rag_pill_html(para), unsafe_allow_html=True)
        else:
            st.markdown(para)


def render_body(body: str):
    for is_table, block_text in split_blocks(body):
        if is_table:
            df = md_table_to_df(block_text)
            if df is not None:
                st.markdown(render_table_html(df), unsafe_allow_html=True)
                continue
        if block_text.strip():
            render_text_block(block_text)


def count_rag(text: str):
    return {label: len(re.findall(rf"\b{re.escape(label)}\b", text)) for label in RAG_TEXT}


def render_footer(doc_name: str):
    st.markdown(
        f'<div class="lng-footer">{html.escape(doc_name)} &nbsp;·&nbsp; '
        "Economic comparison only — not a legal blackline. Redacted terms "
        "(<code>[***]</code>) are never inferred.</div>",
        unsafe_allow_html=True,
    )


def render_comparison_page(label: str, filename: str):
    text = load_text(filename)
    _, slides = parse_slides(text)
    images = list_slide_images(COMPARISON_IMAGE_KEYS[label])
    pptx_name = COMPARISON_PPTX[label]

    search = st.sidebar.text_input("Search this comparison", "", key=f"search_{filename}")
    slide_titles = [f"Slide {s['num']}: {s['title']}" for s in slides]
    jump = st.sidebar.selectbox("Jump to slide", ["(show all)"] + slide_titles, key=f"jump_{filename}")

    st.markdown(f'<div class="lng-hero-title">{html.escape(label)}</div>', unsafe_allow_html=True)
    st.download_button(
        "Download original .pptx",
        load_pptx_bytes(pptx_name),
        file_name=pptx_name,
        key=f"dl_{filename}",
    )

    filtered = slides
    if search:
        q = search.lower()
        filtered = [s for s in slides if q in s["title"].lower() or q in s["body"].lower()]
        st.caption(f"{len(filtered)} of {len(slides)} slides match “{search}”")
    if jump != "(show all)":
        num = jump.split(":")[0].replace("Slide", "").strip()
        filtered = [s for s in filtered if s["num"] == num]

    if not filtered:
        st.info("No slides match the current filter.")
        return

    for s in filtered:
        idx = int(s["num"]) - 1
        st.markdown(
            f'<div class="lng-slide-title">Slide {s["num"]} of {len(slides)}: {html.escape(s["title"])}</div>',
            unsafe_allow_html=True,
        )
        if 0 <= idx < len(images):
            st.image(str(images[idx]), use_container_width=True)
        else:
            st.warning("Slide image not found — run scripts/export_slides.py to regenerate.")
        with st.expander("View extracted text"):
            render_body(s["body"])

    render_footer(filename)


def render_overview():
    st.markdown('<div class="lng-hero-title">LNG SPA Economic Terms Comparison</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="lng-hero-subtitle">Economic comparison of LNG Sale and Purchase Agreements — '
        "not a legal blackline. Redacted terms (<code>[***]</code>) are never inferred.</div>",
        unsafe_allow_html=True,
    )

    legend = " &nbsp; ".join(rag_pill_html(k) for k in ["GREEN", "AMBER", "RED", "NO RAG"])
    st.markdown(legend, unsafe_allow_html=True)
    st.write("")

    counts = {label: count_rag(load_text(fn)) for label, fn in COMPARISONS.items()}
    chart_df = (
        pd.DataFrame(counts)
        .T.reset_index()
        .rename(columns={"index": "Comparison"})
        .melt(id_vars="Comparison", var_name="RAG", value_name="Mentions")
    )
    color_scale = alt.Scale(
        domain=["RED", "AMBER", "GREEN", "NO RAG"],
        range=[RAG_TEXT["RED"], RAG_TEXT["AMBER"], RAG_TEXT["GREEN"], RAG_TEXT["NO RAG"]],
    )
    chart = (
        alt.Chart(chart_df)
        .mark_bar()
        .encode(
            x=alt.X("Comparison:N", title=None, axis=alt.Axis(labelAngle=0)),
            y=alt.Y("Mentions:Q"),
            color=alt.Color("RAG:N", scale=color_scale, legend=alt.Legend(title=None)),
            xOffset="RAG:N",
            tooltip=["Comparison", "RAG", "Mentions"],
        )
        .properties(height=320)
    )
    st.altair_chart(chart, use_container_width=True)

    st.markdown('<div class="lng-slide-title">Comparisons available</div>', unsafe_allow_html=True)
    cols = st.columns(len(COMPARISONS))
    for col, (label, fn) in zip(cols, COMPARISONS.items()):
        _, slides = parse_slides(load_text(fn))
        images = list_slide_images(COMPARISON_IMAGE_KEYS[label])
        with col:
            if images:
                st.image(str(images[0]), use_container_width=True)
            st.markdown(
                f'<div class="lng-card"><h4>{html.escape(label)}</h4>'
                f"<p style='color:{SLATE};'>{html.escape(COMPARISON_BLURBS[label])}</p>"
                f"<p style='color:{MUTED};font-size:0.85rem;'>{len(slides)} slides</p></div>",
                unsafe_allow_html=True,
            )

    st.write("")
    st.markdown('<div class="lng-slide-title">Source contracts in this repo</div>', unsafe_allow_html=True)
    st.write(", ".join(f"`{f}`" for f in list_contract_files() if f not in COMPARISONS.values()))


def render_browse_contracts():
    st.markdown('<div class="lng-hero-title">Browse source contracts</div>', unsafe_allow_html=True)
    files = [f for f in list_contract_files() if f not in COMPARISONS.values()]
    choice = st.selectbox("Contract", files)
    text = load_text(choice)

    keyword = st.text_input("Find in this contract", "")
    if keyword:
        paragraphs = re.split(r"\n\s*\n", text)
        hits = [p for p in paragraphs if keyword.lower() in p.lower()]
        st.caption(f"{len(hits)} matching passage(s)")
        for h in hits[:50]:
            st.markdown(h)
            st.divider()
    else:
        st.download_button("Download raw Markdown", text, file_name=choice)
        with st.expander("Show full text", expanded=False):
            st.markdown(text)


def main():
    st.set_page_config(page_title="LNG SPA Contract Comparison", layout="wide")
    st.markdown(CSS, unsafe_allow_html=True)

    pages = ["Overview", *COMPARISONS.keys(), "Browse source contracts"]
    page = st.sidebar.radio("View", pages)

    if page == "Overview":
        render_overview()
    elif page == "Browse source contracts":
        render_browse_contracts()
    else:
        render_comparison_page(page, COMPARISONS[page])


if __name__ == "__main__":
    main()
