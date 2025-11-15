# app/pages/03_History.py
"""
History page - lists recent scans recorded in the local DB.

This file expects the following functions to be available from app/scan.py:
  - get_db_path()
  - init_db(db_path=None)
  - list_scans(limit=200, db_path=None)

If your scan module is in a different place adjust the import accordingly.
"""
from pathlib import Path
import streamlit as st
from typing import List, Dict, Any

# Import DB helpers from scan.py
# ensure scan.py is in the python path or same package (app/scan.py recommended)
try:
    from scan import get_db_path, init_db, list_scans
except Exception as e:
    # Provide a helpful message if import fails
    st.error(f"Failed to import DB helpers from scan.py: {e}")
    raise

# Import UI utilities
from app.utils.ui import setup_page, apply_theme

setup_page("History")
apply_theme()

# Hero Section - Responsive
st.markdown("""
<div style="text-align: center; padding: clamp(1.5rem, 4vw, 2rem) 0;">
    <h1 style="font-size: clamp(2rem, 6vw, 3rem); margin-bottom: 0.5rem;">📊 Scan History</h1>
    <p style="font-size: clamp(1rem, 3vw, 1.1rem); color: #94a3b8;">All your scans in one place</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Controls in a card - Responsive
st.markdown("""
<div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
            border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
            padding: clamp(1rem, 3vw, 1.5rem); margin-bottom: clamp(1rem, 3vw, 2rem);">
    <h3 style="margin-top: 0; color: #f1f5f9; font-size: clamp(1.1rem, 3vw, 1.3rem);">⚙️ Controls</h3>
</div>
""", unsafe_allow_html=True)

# Responsive columns: stack on mobile
col1, col2 = st.columns([2, 1])
with col1:
    limit = st.number_input("Show last N scans", min_value=1, max_value=10000, value=200, step=10, 
                           help="Number of recent scans to display")

if "history_refresh" not in st.session_state:
    st.session_state.history_refresh = 0

with col2:
    if st.button("🔄 Refresh", use_container_width=True, type="secondary"):
        st.session_state.history_refresh += 1
        st.rerun()

# Initialize DB (safe, idempotent)
try:
    db_path = get_db_path()
    # init_db will create file/tables if missing; pass the path so it's deterministic
    init_db(db_path)
except Exception as e:
    st.error(f"Failed to initialize DB at expected path: {e}")
    st.stop()

# Read recent scans
scans: List[Dict[str, Any]] = []
try:
    scans = list_scans(limit=int(limit), db_path=db_path)
except Exception as e:
    st.error(f"Failed to read scans from DB ({db_path}): {e}")
    st.stop()

# Optional: Clear history (dangerous, show confirm)
def _clear_history():
    import sqlite3
    try:
        conn = sqlite3.connect(str(db_path))
        cur = conn.cursor()
        # Truncate both common tables if they exist
        try:
            cur.execute("DELETE FROM scans;")
        except Exception:
            pass
        try:
            cur.execute("DELETE FROM history;")
        except Exception:
            pass
        conn.commit()
        conn.close()
        st.success("History cleared.")
    except Exception as ex:
        st.error(f"Failed to clear history: {ex}")

with st.expander("History controls"):
    st.write("Adjust limit and refresh/clear history.")
    if st.button("Clear history"):
        if st.confirm("Are you sure you want to permanently clear the stored history?"):
            _clear_history()
            st.session_state.history_refresh += 1

# If no scans found, show info
if not scans:
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
                padding: 3rem; text-align: center; margin: 2rem 0;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">📭</div>
        <h3 style="color: #f1f5f9; margin-bottom: 0.5rem;">No Scans Yet</h3>
        <p style="color: #94a3b8;">Start scanning URLs or files to see your history here!</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# Display the count - Responsive
st.markdown(f"""
<div style="background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.2); 
            border-radius: 12px; padding: clamp(0.75rem, 2vw, 1rem); margin-bottom: 1.5rem;
            display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem;">
    <span style="color: #8b5cf6; font-weight: 600; font-size: clamp(0.95rem, 2.5vw, 1rem);">📈 Found {len(scans)} scans</span>
    <span style="color: #94a3b8; font-size: clamp(0.85rem, 2vw, 0.9rem);">(showing up to {limit})</span>
</div>
""", unsafe_allow_html=True)

# Render a simple table: id | input | type | risk | summary | timestamp
table_rows = []
for s in scans:
    # ensure keys exist regardless of source table
    sid = s.get("id", "")
    inp = s.get("input", s.get("input_value", "")) or ""
    typ = s.get("type", s.get("scan_type", "")) or ""
    risk = s.get("risk", "")
    summary = s.get("summary", "")
    ts = s.get("timestamp", "") or s.get("created_at", "")
    table_rows.append({
        "Scan ID": sid,
        "Input": inp,
        "Type": typ,
        "Risk": risk,
        "Summary": summary,
        "Timestamp (UTC)": ts
    })

# Streamlit can display a list-of-dicts as a dataframe-like table
import pandas as pd
df = pd.DataFrame(table_rows)
st.dataframe(df, use_container_width=True)

# Optionally, allow the user to expand a single record for details
st.markdown("---")
st.subheader("Details")
sel = st.selectbox("Select scan (by id) to view full details", options=[r["Scan ID"] for r in table_rows], format_func=lambda v: f"Scan {v}" if v is not None else "(none)")

if sel is not None:
    # find object
    found = next((x for x in scans if x.get("id") == sel or str(x.get("id")) == str(sel)), None)
    if found:
        st.json(found)
    else:
        st.warning("Selected scan not found in the recent fetch — try Refresh.")
