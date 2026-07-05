import re
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).parent
CONTRACTS_DIR = ROOT / "contracts"

COMPARISONS = {
    "Driftwood LNG — Vitol / Gunvor / Shell": "driftwood_lng_spa_economic_terms_comparison_formula_signature_updated.md",
    "Cheniere Sabine Pass — BG / GNF / GAIL / Total": "cheniere_sabine_pass_spa_standalone_economic_terms.md",
}

RAG_COLORS = {
    "RED": "#f8d7da",
    "AMBER": "#fff3cd",
    "GREEN": "#d4edda",
    "NO RAG": "#e2e3e5",
}

SLIDE_RE = re.compile(r"^## Slide (\d+): (.+)$", re.MULTILINE)
TABLE_LINE_RE = re.compile(r"^\|.*\|$")
TABLE_SEP_RE = re.compile(r"^\|?\s*:?-{2,}.*-{2,}\s*\|?$")


@st.cache_data
def load_text(filename: str) -> str:
    return (CONTRACTS_DIR / filename).read_text(encoding="utf-8")


@st.cache_data
def list_contract_files():
    return sorted(p.name for p in CONTRACTS_DIR.glob("*.md"))


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


def style_rag(df: pd.DataFrame):
    rag_cols = [c for c in df.columns if c.strip().upper() == "RAG"]
    if not rag_cols:
        return df
    def color(val):
        val = str(val).strip().upper()
        return f"background-color: {RAG_COLORS[val]}" if val in RAG_COLORS else ""
    styler = df.style
    apply_fn = styler.map if hasattr(styler, "map") else styler.applymap
    return apply_fn(color, subset=rag_cols)


def render_body(body: str):
    for is_table, block_text in split_blocks(body):
        if is_table:
            df = md_table_to_df(block_text)
            if df is not None:
                st.dataframe(style_rag(df), use_container_width=True, hide_index=True)
                continue
        if block_text.strip():
            st.markdown(block_text)


def count_rag(text: str):
    return {
        label: len(re.findall(rf"\b{re.escape(label)}\b", text))
        for label in RAG_COLORS
    }


def render_comparison_page(label: str, filename: str):
    text = load_text(filename)
    intro, slides = parse_slides(text)

    search = st.sidebar.text_input("Search this comparison", "", key=f"search_{filename}")
    slide_titles = [f"Slide {s['num']}: {s['title']}" for s in slides]
    jump = st.sidebar.selectbox("Jump to slide", ["(show all)"] + slide_titles, key=f"jump_{filename}")

    st.title(label)
    if intro:
        st.markdown(intro)

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
        st.subheader(f"Slide {s['num']}: {s['title']}")
        render_body(s["body"])
        st.divider()


def render_overview():
    st.title("LNG SPA Economic Terms Comparison")
    st.caption(
        "Economic comparison of LNG Sale and Purchase Agreements — not a legal blackline. "
        "Redacted terms (`[***]`) are never inferred."
    )

    counts = {label: count_rag(load_text(fn)) for label, fn in COMPARISONS.items()}
    chart_df = pd.DataFrame(counts).T
    st.subheader("RAG rating distribution")
    st.bar_chart(chart_df)

    st.subheader("Comparisons available")
    for label, fn in COMPARISONS.items():
        with st.expander(label):
            intro, slides = parse_slides(load_text(fn))
            st.markdown(intro)
            st.caption(f"{len(slides)} slides — select this comparison from the sidebar to explore.")

    st.subheader("Source contracts in this repo")
    st.write(", ".join(f"`{f}`" for f in list_contract_files() if f not in COMPARISONS.values()))


def render_browse_contracts():
    st.title("Browse source contracts")
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
