from __future__ import annotations

# BEGIN: ensure project root is importable
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
# END: ensure project root is importable

# app/pages/02_Bulk.py
import io, csv
import pandas as pd
import streamlit as st

from app.utils.ui import setup_page, apply_theme
from app.utils.paths import ensure_dirs
from app.utils.engines import aggregate_scan, detect_ioc_type
from app.utils.secrets import get_vt_api_key

setup_page("VirusLens — Cyber Threat Analyzer")
apply_theme()
ensure_dirs()

# Hero Section - Responsive
st.markdown("""
<div style="text-align: center; padding: clamp(1.5rem, 4vw, 2rem) 0;">
    <h1 style="font-size: clamp(2rem, 6vw, 3rem); margin-bottom: 0.5rem;">📦 Bulk Scan</h1>
    <p style="font-size: clamp(1rem, 3vw, 1.1rem); color: #94a3b8;">Scan multiple URLs or files at once</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Responsive columns - stack on mobile
lcol, rcol = st.columns([1, 1], gap="medium")
with lcol:
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
                padding: clamp(1.5rem, 4vw, 2rem); margin-bottom: 1rem;">
        <h3 style="margin-top: 0; color: #f1f5f9; font-size: clamp(1.1rem, 3vw, 1.3rem);">📄 Upload CSV</h3>
        <p style="color: #94a3b8; font-size: clamp(0.9rem, 2.5vw, 1rem); margin-bottom: 1.5rem;">Upload a CSV file with URLs or hashes</p>
    </div>
    """, unsafe_allow_html=True)
    
with rcol:
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
                padding: clamp(1.5rem, 4vw, 2rem); margin-bottom: 1rem;">
        <h3 style="margin-top: 0; color: #f1f5f9; font-size: clamp(1.1rem, 3vw, 1.3rem);">📋 Paste IOCs</h3>
        <p style="color: #94a3b8; font-size: clamp(0.9rem, 2.5vw, 1rem); margin-bottom: 1.5rem;">Paste URLs or hashes (one per line)</p>
    </div>
    """, unsafe_allow_html=True)

# API key check
try:
    _ = get_vt_api_key()
except Exception as e:
    st.error(str(e))
    st.stop()

lc, rc = st.columns(2)

with lc:
    up = st.file_uploader("CSV with columns: input,type(optional)", type=["csv"])
    run_csv = st.button("Process CSV", key="run_csv")

with rc:
    txt = st.text_area("One per line (URL or hash)", height=260, placeholder="https://example.com\n44d88612fea8a8f36de82e1278abb02f")
    run_txt = st.button("Scan Pasted", key="run_txt")

def process_rows(items):
    out = []
    prog = st.progress(0)
    for i, row in enumerate(items, start=1):
        ioc = row.get("input", "").strip()
        t = row.get("type") or detect_ioc_type(ioc)
        if not ioc:
            out.append({"input": "", "type": t, "overall_risk": "N/A", "engines": []})
            continue
        try:
            res = aggregate_scan(ioc, t)
            out.append({"input": ioc, "type": res["type"], "overall_risk": res["overall_risk"], "engines": res["engines"]})
        except Exception as e:
            out.append({"input": ioc, "type": t, "overall_risk": f"error: {e}", "engines": []})
        prog.progress(min(i / len(items), 1.0))
    return out

if run_csv and up is not None:
    try:
        df = pd.read_csv(up)
        if "input" not in df.columns:
            st.error("CSV must contain a column named 'input'. Optional column: 'type'.")
        else:
            rows = [{"input": str(r["input"]), "type": (str(r["type"]) if "type" in df.columns else "").strip() or None} for _, r in df.iterrows()]
            with st.spinner("Processing CSV…"):
                results = process_rows(rows)
            # Show summary table
            show = pd.DataFrame([{"input": r["input"], "type": r["type"], "overall": r["overall_risk"]} for r in results])
            st.dataframe(show, use_container_width=True)
            # Download results
            outdf = pd.DataFrame(results)
            csv_bytes = outdf.to_csv(index=False).encode("utf-8")
            st.download_button("Download results CSV", data=csv_bytes, file_name="bulk_results.csv", mime="text/csv")
    except Exception as e:
        st.error(f"Failed to process: {e}")

if run_txt and txt.strip():
    lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
    rows = [{"input": ln, "type": detect_ioc_type(ln)} for ln in lines]
    with st.spinner("Processing list…"):
        results = process_rows(rows)
    show = pd.DataFrame([{"input": r["input"], "type": r["type"], "overall": r["overall_risk"]} for r in results])
    st.dataframe(show, use_container_width=True)
    outdf = pd.DataFrame(results)
    st.download_button("Download results CSV", data=outdf.to_csv(index=False).encode("utf-8"), file_name="bulk_results.csv", mime="text/csv")
