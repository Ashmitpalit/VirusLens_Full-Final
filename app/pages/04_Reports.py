# app/pages/04_Reports.py
"""
Reports page for VirusLens.
- Shows recent scans from the local DB
- Lets the user select a scan and generate a PDF report matching the layout/format of report_14.pdf
- All content placed inside tables (no raw JSON section)
Notes:
- st.set_page_config MUST be the first Streamlit command in this file.
- The file locates a viruslens.db via st.secrets["VL_DB_FILE"], ENV VL_DB_FILE, or common paths.
"""

from pathlib import Path
import os
import io
import sqlite3
import datetime
import json

import streamlit as st

# -------------- PDF libraries --------------
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from scan import init_db
from app.utils.ui import setup_page, apply_theme

# -------------- Streamlit page config (must be the first Streamlit command) --------------
setup_page("Reports")
apply_theme()
# ---------------------------
# Utilities
# ---------------------------
# Robust rerun helper (works across Streamlit versions)
def safe_rerun():
    """
    Attempt to cause the Streamlit script to rerun. Tries multiple strategies
    to be compatible with different Streamlit releases:
      1) st.experimental_rerun() if present
      2) raise runtime.scriptrunner.RerunException
      3) raise streamlit.report_thread.RerunException (old)
      4) fallback: show an info asking user to refresh
    """
    # 1) public API if present
    try:
        if hasattr(st, "experimental_rerun"):
            st.experimental_rerun()
            return
    except Exception:
        # ignore and continue to other strategies
        pass

    # 2) runtime.scriptrunner.RerunException (newer versions)
    try:
        from streamlit.runtime.scriptrunner import RerunException
        raise RerunException()
    except Exception:
        pass

    # 3) older API location
    try:
        from streamlit.report_thread import RerunException
        raise RerunException()
    except Exception:
        pass

    # 4) last resort: instruct the user to refresh
    try:
        st.info("Please refresh the page to see the latest data.")
    except Exception:
        # nothing more to do
        pass

def get_db_path() -> Path:
    """
    Locate the viruslens sqlite DB file robustly.
    Search order:
      1. st.secrets["VL_DB_FILE"] (if available)
      2. ENV VL_DB_FILE
      3. current working dir ./viruslens.db
      4. project root (parent of app/) ../viruslens.db
      5. app subfolder ./app/viruslens.db
    Returns a Path (may not exist).
    """
    # 1) st.secrets if available (guarded)
    secret_path = None
    try:
        if hasattr(st, "secrets") and st.secrets:
            # st.secrets may be a SecretsSingleton or dict-like
            try:
                secret_path = st.secrets.get("VL_DB_FILE")
            except Exception:
                # fallback - try attribute-like access
                secret_path = None
    except Exception:
        secret_path = None

    # 2) environment variable
    env_path = os.environ.get("VL_DB_FILE")

    candidates = []
    if secret_path:
        candidates.append(Path(secret_path))
    if env_path:
        candidates.append(Path(env_path))

    # cwd
    candidates.append(Path.cwd() / "viruslens.db")

    # project root (assume this file is app/pages/04_Reports.py)
    this_file = Path(__file__).resolve()
    maybe_project_root = this_file.parents[2] if len(this_file.parents) >= 3 else this_file.parent
    candidates.append(maybe_project_root / "viruslens.db")
    # app/ subfolder
    candidates.append(maybe_project_root / "app" / "viruslens.db")
    # local folder (rare)
    candidates.append(this_file.parent / "viruslens.db")

    # Return first existing file; if none exist return the canonical project root candidate
    for p in candidates:
        try:
            if p.exists() and p.is_file():
                return p
        except Exception:
            continue
    return maybe_project_root / "viruslens.db"


def fetch_rows_from_db(db_path: Path, limit: int = 200):
    """
    Fetch recent scans from the DB using several fallback queries.
    Returns list[dict] sorted newest-first. If DB missing or unreadable -> [].
    Each dict keys: id, input, type, risk, summary, timestamp, vt_details (optional dict)
    """
    out = []
    if not db_path:
        return out
    if not db_path.exists():
        return out

    try:
        conn = sqlite3.connect(str(db_path))
        cur = conn.cursor()

        # 1) Try 'history' table
        try:
            cur.execute("""
                SELECT id,
                       COALESCE(input_value, input, target, '') AS input_val,
                       COALESCE(scan_type, type, '') AS scan_type,
                       COALESCE(risk_score, status, '') AS risk,
                       COALESCE(summary, result_json, '') AS summary,
                       COALESCE(timestamp, created_at, updated_at, '') AS ts
                FROM history
                ORDER BY id DESC
                LIMIT ?
            """, (limit,))
            rows = cur.fetchall()
            if rows:
                for r in rows:
                    out.append({
                        "id": r[0],
                        "input": r[1],
                        "type": r[2],
                        "risk": r[3],
                        "summary": r[4],
                        "timestamp": r[5],
                        "vt_details": {}  # placeholder
                    })
                conn.close()
                return out
        except Exception:
            pass

        # 2) Try 'scans' table
        try:
            # Check if vt_details column exists
            cur.execute("PRAGMA table_info(scans)")
            columns = [row[1] for row in cur.fetchall()]
            has_vt_details = 'vt_details' in columns
            has_summary = 'summary' in columns
            has_risk_score = 'risk_score' in columns
            
            # Build query based on available columns
            if has_vt_details and has_summary and has_risk_score:
                cur.execute("""
                    SELECT id,
                           COALESCE(input, target, '') as input_val,
                           COALESCE(scan_type, type, '') as scan_type,
                           COALESCE(risk_score, status, '') as risk,
                           COALESCE(summary, result_json, '') as summary_field,
                           COALESCE(vt_details, '{}') as vt_details_json,
                           COALESCE(created_at, updated_at, '') as ts
                    FROM scans
                    ORDER BY id DESC
                    LIMIT ?
                """, (limit,))
            else:
                cur.execute("""
                    SELECT id,
                           COALESCE(target, input, '') as input_val,
                           COALESCE(scan_type, type, '') as scan_type,
                           COALESCE(status, '') as status,
                           COALESCE(result_json, '') as result_json,
                           COALESCE(created_at, updated_at, '') as ts
                    FROM scans
                    ORDER BY id DESC
                    LIMIT ?
                """, (limit,))
            
            rows = cur.fetchall()
            if rows:
                for r in rows:
                    if has_vt_details and has_summary and has_risk_score:
                        # New schema with vt_details column
                        vt_details = {}
                        vt_details_json = r[5] or "{}"
                        try:
                            if vt_details_json and isinstance(vt_details_json, str):
                                vt_details = json.loads(vt_details_json)
                            elif isinstance(vt_details_json, dict):
                                vt_details = vt_details_json
                        except Exception:
                            vt_details = {}
                        
                        out.append({
                            "id": r[0],
                            "input": r[1] or "",
                            "type": r[2] or "",
                            "risk": r[3] or "",
                            "summary": r[4] or "",
                            "timestamp": r[6] or "",
                            "vt_details": vt_details
                        })
                    else:
                        # Old schema - try to parse from result_json
                        vt_details = {}
                        summary_field = r[4] or ""
                        try:
                            parsed = json.loads(summary_field) if isinstance(summary_field, str) and summary_field.strip().startswith("{") else None
                            if isinstance(parsed, dict):
                                vt_details = parsed
                                parsed_summary = parsed.get("summary") or parsed.get("result") or ""
                            else:
                                parsed_summary = summary_field
                        except Exception:
                            parsed_summary = summary_field
                        out.append({
                            "id": r[0],
                            "input": r[1] or "",
                            "type": r[2] or "",
                            "risk": r[3] or "",
                            "summary": parsed_summary or "",
                            "timestamp": r[5] or "",
                            "vt_details": vt_details
                        })
                conn.close()
                return out
        except Exception:
            pass

        # 3) Generic fallback: inspect tables and pick the first with rows
        try:
            cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [t[0] for t in cur.fetchall()]
            candidates = ["history", "scans", "scan", "records", "results"]
            for tbl in candidates:
                if tbl in tables:
                    try:
                        cur.execute(f"SELECT * FROM {tbl} ORDER BY rowid DESC LIMIT ?", (limit,))
                        rows = cur.fetchall()
                        colnames = [d[0] for d in cur.description] if cur.description else []
                        if rows:
                            for r in rows:
                                rowd = {colnames[i]: r[i] for i in range(len(colnames))}
                                out.append({
                                    "id": rowd.get("id") or rowd.get("rowid") or "",
                                    "input": rowd.get("target") or rowd.get("input") or rowd.get("input_value") or "",
                                    "type": rowd.get("scan_type") or rowd.get("type") or "",
                                    "risk": rowd.get("status") or rowd.get("risk") or "",
                                    "summary": rowd.get("result_json") or rowd.get("summary") or "",
                                    "timestamp": rowd.get("created_at") or rowd.get("timestamp") or "",
                                    "vt_details": {}
                                })
                            conn.close()
                            return out
                    except Exception:
                        continue
        except Exception:
            pass

        conn.close()
        return out
    except Exception:
        try:
            conn.close()
        except Exception:
            pass
        return []


# ---------------------------
# PDF Builder
# ---------------------------

def _wrap_text(text: str, max_length: int = 100, style=None) -> Paragraph:
    """
    Wrap long text into a Paragraph that will fit within table cells.
    Handles JSON strings and long text by formatting them appropriately.
    """
    if style is None:
        styles = getSampleStyleSheet()
        style = ParagraphStyle(
            "CellText",
            parent=styles["Normal"],
            fontSize=10,
            leading=12,
            wordWrap='CJK'  # Enables word wrapping
        )
    
    # Escape XML special characters for Paragraph
    text = str(text) if text else ""
    
    # Try to format JSON strings more readably
    if text.strip().startswith("{") or text.strip().startswith("["):
        try:
            import json
            parsed = json.loads(text)
            # Format JSON with line breaks for better readability
            text = json.dumps(parsed, indent=2, ensure_ascii=False)
        except (json.JSONDecodeError, ValueError):
            pass  # Not valid JSON, use as-is
    
    # Replace special characters that might break XML parsing
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    # For very long text, truncate but keep it reasonable
    # max_length * 3 allows for multi-line content but prevents excessive height
    if len(text) > max_length * 4:
        # Try to truncate at a word boundary if possible
        truncated = text[:max_length * 4]
        last_space = truncated.rfind(' ')
        if last_space > max_length * 3:
            text = truncated[:last_space] + "..."
        else:
            text = truncated + "..."
    
    return Paragraph(text, style)

def _make_metadata_table(scan_obj: dict):
    """
    Return a ReportLab Table for Metadata exactly in tabular format.
    Uses Paragraph objects to enable text wrapping within cells.
    """
    styles = getSampleStyleSheet()
    cell_style = ParagraphStyle(
        "CellText",
        parent=styles["Normal"],
        fontSize=10,
        leading=12,
        wordWrap='CJK',
        spaceAfter=2
    )
    label_style = ParagraphStyle(
        "LabelText",
        parent=styles["Normal"],
        fontSize=10,
        leading=12,
        wordWrap='CJK'
    )
    
    scan_id = scan_obj.get("id", "")
    input_val = scan_obj.get("input", "") or scan_obj.get("target", "")
    scan_type = scan_obj.get("type", "")
    risk = scan_obj.get("risk", "")
    summary = scan_obj.get("summary", "") or ""
    timestamp = scan_obj.get("timestamp", "") or ""

    rows = [
        [_wrap_text("Scan ID", style=label_style), _wrap_text(str(scan_id), style=cell_style)],
        [_wrap_text("Input", style=label_style), _wrap_text(input_val, max_length=80, style=cell_style)],
        [_wrap_text("Type", style=label_style), _wrap_text(scan_type, style=cell_style)],
        [_wrap_text("Risk Score", style=label_style), _wrap_text(risk, style=cell_style)],
        [_wrap_text("Summary", style=label_style), _wrap_text(summary if summary else "No summary available", max_length=120, style=cell_style)],
        [_wrap_text("Timestamp (UTC)", style=label_style), _wrap_text(str(timestamp), style=cell_style)]
    ]

    tbl = Table(rows, colWidths=[180, 330])
    tbl.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.6, colors.black),
        ("BACKGROUND", (0,0), (0,-1), colors.whitesmoke),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    return tbl


def _make_section_table(title: str, rows: list):
    """
    Create a two-column table for a section (title handled outside).
    rows: list of [label, value] - values will be wrapped in Paragraphs
    """
    styles = getSampleStyleSheet()
    cell_style = ParagraphStyle(
        "SectionCellText",
        parent=styles["Normal"],
        fontSize=9,
        leading=11,
        wordWrap='CJK',
        spaceAfter=2
    )
    label_style = ParagraphStyle(
        "SectionLabelText",
        parent=styles["Normal"],
        fontSize=9,
        leading=11,
        wordWrap='CJK'
    )
    
    # Convert all row values to Paragraphs for proper wrapping
    wrapped_rows = []
    for label, value in rows:
        wrapped_label = _wrap_text(str(label), max_length=50, style=label_style)
        wrapped_value = _wrap_text(str(value) if value else "Not available", max_length=100, style=cell_style)
        wrapped_rows.append([wrapped_label, wrapped_value])
    
    tbl = Table(wrapped_rows, colWidths=[180, 330])
    tbl.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.4, colors.grey),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BACKGROUND", (0,0), (0,-1), colors.whitesmoke)
    ]))
    return tbl


def build_report_pdf_bytes(scan_obj: dict) -> bytes:
    """
    Build and return PDF bytes for the given scan object.
    The structure matches the report_14 style: metadata table + 10 sections, all tables.
    """
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter, topMargin=36, bottomMargin=36, leftMargin=36, rightMargin=36)
    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    heading_style = ParagraphStyle("Heading", parent=styles["Heading2"], fontSize=12, spaceAfter=6)

    story = []

    # Title
    title_style = ParagraphStyle("Title", parent=styles["Title"], fontSize=20, spaceAfter=12)
    story.append(Paragraph("Metadata", title_style))
    story.append(Spacer(1, 6))

    # Metadata table
    story.append(_make_metadata_table(scan_obj))
    story.append(Spacer(1, 12))

    # Sections: use vt_details dict when available
    vt_details = {}
    if isinstance(scan_obj.get("vt_details"), dict):
        vt_details = scan_obj.get("vt_details")
    
    # Debug: Log what we're working with
    import os
    if os.getenv("DEBUG_REPORTS"):
        print(f"DEBUG: scan_obj keys: {list(scan_obj.keys())}")
        print(f"DEBUG: vt_details type: {type(scan_obj.get('vt_details'))}")
        print(f"DEBUG: vt_details keys: {list(vt_details.keys()) if isinstance(vt_details, dict) else 'Not a dict'}")
        print(f"DEBUG: Sample vt_details values: {dict(list(vt_details.items())[:5]) if isinstance(vt_details, dict) else 'N/A'}")

    # Helper function to get value or default (handles empty strings)
    def get_value(key: str, default: str) -> str:
        val = vt_details.get(key, "")
        return val if val and str(val).strip() else default
    
    # Sections list - 10 sections, each has label/value rows
    sections = [
        ("1. URL Reputation & Categorization", [
            ["Reputation", get_value("reputation", "No reputation / categorization details available.")],
            ["Category", get_value("category", "No category information available.")],
            ["Harmless/Malicious Counts", get_value("counts", "Not available.")]
        ]),
        ("2. Domain & Hosting Information", [
            ["Domain", get_value("domain", "No domain/hosting metadata available.")],
            ["Registrar / WHOIS", get_value("whois", "No public ownership (WHOIS) details were found.")],
            ["Hosting Country", get_value("country", "Hosting country not specified.")],
            ["ASN / Network", get_value("asn", "Network/ASN not reported.")]
        ]),
        ("3. DNS Records & Network Artifacts", [
            ["DNS Records", get_value("dns", "No DNS records were reported for this link.")],
            ["IP Address candidates", get_value("ips", "No IP candidates available.")]
        ]),
        ("4. Static Content Inspection", [
            ["HTML Title", get_value("html_title", "No static content inspection details available.")],
            ["Detected Scripts / Links", get_value("scripts", "No scripts/resources reported.")],
            ["Embedded Resources / Tags", get_value("resources", "No notable embedded resources.")]
        ]),
        ("5. Dynamic Behavioral Analysis", [
            ["Redirect Chain", get_value("redirects", "Not reported.")],
            ["Downloads Attempted", get_value("downloads", "None.")],
            ["Execution Behavior", get_value("execution", "No suspicious behavior detected.")]
        ]),
        ("6. Connections & Relationships", [
            ["Linked URLs / Files", get_value("linked", "None found.")],
            ["Communicating Files", get_value("files", "None found.")],
            ["Contacted Domains", get_value("domains", "None found.")]
        ]),
        ("7. SSL/TLS Certificate Information", [
            ["Issuer", get_value("cert_issuer", "Not available.")],
            ["Subject", get_value("cert_subject", "Not available.")],
            ["Validity", get_value("cert_validity", "Not available.")]
        ]),
        ("8. Antivirus / Engine Detections", [
            ["Last Analysis Stats", get_value("av_stats", "No engine detection stats available.")],
            ["Malicious Engines", get_value("av_malicious", "None reported.")]
        ]),
        ("9. Heuristic & Machine Learning Scoring", [
            ["ML/Heuristic Verdict", get_value("ml_verdict", "No ML verdict provided.")],
            ["Heuristic Tags", get_value("ml_tags", "None")]
        ]),
        ("10. Historical & Community Data", [
            ["Community Votes", get_value("community", "No community votes.")],
            ["First Submission Date", get_value("first_seen", "Unknown")],
            ["Last Analysis Date", get_value("last_seen", "Unknown")]
        ])
    ]

    # Render sections as title + table
    for title, rows in sections:
        story.append(Paragraph(f"<b>{title}</b>", heading_style))
        story.append(_make_section_table(title, rows))
        story.append(Spacer(1, 12))

    # Footer note
    story.append(Spacer(1, 12))
    story.append(Paragraph("Generated by VirusLens — Cyber Threat Analyzer", normal_style))

    doc.build(story)
    pdf_bytes = buf.getvalue()
    buf.close()
    return pdf_bytes


# ---------------------------
# Streamlit UI
# ---------------------------

# Hero Section - Responsive
st.markdown("""
<div style="text-align: center; padding: clamp(1.5rem, 4vw, 2rem) 0;">
    <h1 style="font-size: clamp(2rem, 6vw, 3rem); margin-bottom: 0.5rem;">📄 Reports</h1>
    <p style="font-size: clamp(1rem, 3vw, 1.1rem); color: #94a3b8;">Generate professional PDF reports</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

db_path = get_db_path()

# Controls Card - Responsive
st.markdown("""
<div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
            border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
            padding: clamp(1rem, 3vw, 1.5rem); margin-bottom: clamp(1rem, 3vw, 2rem);">
    <h3 style="margin-top: 0; color: #f1f5f9; font-size: clamp(1.1rem, 3vw, 1.3rem);">⚙️ Settings</h3>
</div>
""", unsafe_allow_html=True)

limit = st.number_input("Show last N scans", min_value=1, max_value=1000, value=200, step=1,
                       help="Number of recent scans to display")

# Initialize database
init_db(get_db_path())

col1, col2 = st.columns([1, 4])
with col1:
    if st.button("🔄 Refresh", use_container_width=True):
        safe_rerun()

# Fetch scans from database
scans = fetch_rows_from_db(db_path, limit=limit)

if not scans:
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
                padding: 3rem; text-align: center; margin: 2rem 0;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">📭</div>
        <h3 style="color: #f1f5f9; margin-bottom: 0.5rem;">No Scans Available</h3>
        <p style="color: #94a3b8;">Perform some scans first to generate reports!</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# Scan Selection Card - Responsive
st.markdown("""
<div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
            border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
            padding: clamp(1rem, 3vw, 1.5rem); margin: clamp(1rem, 3vw, 2rem) 0;">
    <h3 style="margin-top: 0; color: #f1f5f9; margin-bottom: 1rem; font-size: clamp(1.1rem, 3vw, 1.3rem);">📋 Select Scan</h3>
</div>
""", unsafe_allow_html=True)

# present scans in selectbox
selected_scan = st.selectbox(
    "Choose a scan to generate report",
    options=scans,
    format_func=lambda s: f"Scan {s.get('id','?')} — {s.get('input','(no input)')}",
    label_visibility="collapsed"
)

scan_obj = selected_scan
scan_id = scan_obj.get("id", "")

st.markdown(f"""
<div style="background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.2); 
            border-radius: 12px; padding: clamp(0.75rem, 2vw, 1rem); margin: 1rem 0;
            word-wrap: break-word;">
    <span style="color: #8b5cf6; font-weight: 600; font-size: clamp(0.95rem, 2.5vw, 1rem);">Selected:</span>
    <span style="color: #cbd5e1; margin-left: 0.5rem; font-size: clamp(0.85rem, 2vw, 0.9rem);">Scan {scan_id} — {scan_obj.get('input','')[:50]}</span>
</div>
""", unsafe_allow_html=True)

# Debug: Show scan data before generating report
with st.expander("🔍 Debug: Scan Data (Click to view)", expanded=False):
    st.write("**Scan object keys:**", list(scan_obj.keys()))
    st.write("**vt_details type:**", type(scan_obj.get("vt_details")))
    if isinstance(scan_obj.get("vt_details"), dict):
        st.write("**vt_details keys:**", list(scan_obj.get("vt_details", {}).keys()))
        st.write("**Sample vt_details values:**")
        for k, v in list(scan_obj.get("vt_details", {}).items())[:10]:
            val_str = str(v)[:100] if v else "None"
            st.write(f"- {k}: `{val_str}`")
    else:
        st.write("**vt_details value:**", scan_obj.get("vt_details"))
    st.json(scan_obj)

# Generate PDF button
if st.button("📥 Generate Report PDF", use_container_width=True, type="primary"):
    try:
        pdf_bytes = build_report_pdf_bytes(scan_obj)
        filename = f"report_{scan_id}.pdf"
        st.success(f"PDF generated: {filename}")

        st.download_button(
            label="Download Report PDF",
            data=pdf_bytes,
            file_name=filename,
            mime="application/pdf"
        )
    except Exception as e:
        st.error(f"Failed to generate PDF: {e}")
        raise
