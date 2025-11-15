from __future__ import annotations

# BEGIN: ensure project root is importable
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
# END: ensure project root is importable

# app/pages/01_Scan.py
import io
import json
import streamlit as st

from app.utils.ui import setup_page, apply_theme
from app.utils.paths import ensure_dirs
from app.utils.engines import aggregate_scan, detect_ioc_type, sha256_file
from app.utils.virustotal import file_hash_sha256  # if you prefer the older helper
from app.utils.secrets import get_vt_api_key
from scan import record_search, init_db, get_db_path

setup_page("VirusLens — Cyber Threat Analyzer")
apply_theme()
ensure_dirs()

# Initialize database
try:
    db_path = get_db_path()
    init_db(db_path)
except Exception as e:
    st.warning(f"Database initialization warning: {e}")

# Hero Section - Responsive
st.markdown("""
<div style="text-align: center; padding: 1.5rem 0;">
    <h1 style="font-size: clamp(2rem, 5vw, 3rem); margin-bottom: 0.5rem;">🛡️ VirusLens</h1>
    <p style="font-size: clamp(1rem, 3vw, 1.2rem); color: #94a3b8; margin-bottom: 1.5rem;">Cyber Threat Analyzer</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Scan Options in Cards - Responsive columns
# Streamlit automatically stacks columns on mobile (< 768px)
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
                padding: clamp(1.5rem, 4vw, 2rem); margin-bottom: 1rem;">
        <h3 style="margin-top: 0; color: #f1f5f9; font-size: clamp(1.1rem, 3vw, 1.3rem);">🌐 Scan URL</h3>
        <p style="color: #94a3b8; margin-bottom: 1.5rem; font-size: clamp(0.9rem, 2.5vw, 1rem);">Analyze any URL for threats</p>
    </div>
    """, unsafe_allow_html=True)
    url = st.text_input("Enter URL", placeholder="https://example.com", label_visibility="collapsed", key="url_input")
    btn_url = st.button("🔍 Scan URL", use_container_width=True, type="primary")

with col2:
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
                padding: clamp(1.5rem, 4vw, 2rem); margin-bottom: 1rem;">
        <h3 style="margin-top: 0; color: #f1f5f9; font-size: clamp(1.1rem, 3vw, 1.3rem);">📁 Scan File</h3>
        <p style="color: #94a3b8; margin-bottom: 1.5rem; font-size: clamp(0.9rem, 2.5vw, 1rem);">Upload and analyze files</p>
    </div>
    """, unsafe_allow_html=True)
    up = st.file_uploader("Upload a file", type=None, label_visibility="collapsed", key="file_uploader")
    btn_file = st.button("🔍 Scan File", use_container_width=True, type="primary")

# Check API key early so the UX is clear
try:
    _ = get_vt_api_key()
except Exception as e:
    st.error(str(e))
    st.stop()

def render_result(res: dict):
    # Risk badge with gradient
    risk_colors = {
        "High": "#ef4444",
        "Medium": "#f59e0b", 
        "Low": "#10b981"
    }
    risk_color = risk_colors.get(res.get('overall_risk', 'Low'), "#10b981")
    
    st.markdown(f"""
    <div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
                padding: clamp(1.5rem, 4vw, 2rem); margin: 1.5rem 0;">
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
            <div style="background: {risk_color}20; border: 1px solid {risk_color}40; 
                        border-radius: 12px; padding: clamp(0.5rem, 2vw, 0.75rem) clamp(0.75rem, 3vw, 1rem); 
                        min-height: 44px; display: flex; align-items: center;">
                <span style="color: {risk_color}; font-weight: 600; font-size: clamp(1rem, 3vw, 1.1rem);">
                    Risk: {res.get('overall_risk', 'Low')}
                </span>
            </div>
            <div style="background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.2); 
                        border-radius: 12px; padding: clamp(0.5rem, 2vw, 0.75rem) clamp(0.75rem, 3vw, 1rem);
                        min-height: 44px; display: flex; align-items: center;">
                <span style="color: #8b5cf6; font-weight: 500; font-size: clamp(0.9rem, 2.5vw, 1rem);">
                    Type: {res.get('type', 'unknown')}
                </span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    for eng in res["engines"]:
        with st.expander(f"🔍 {eng.get('engine','?')} Details", expanded=False):
            st.json(eng.get("summary", {}))

def _extract_vt_details(res: dict) -> dict:
    """Extract detailed information from engine responses for report generation."""
    vt_details = {
        "overall_risk": res.get("overall_risk", ""),
        "type": res.get("type", ""),
    }
    
    # Extract data from VirusTotal raw response
    for eng in res.get("engines", []):
        if eng.get("engine") == "VirusTotal":
            raw = eng.get("raw", {})
            if not raw:
                # Debug: log that raw is empty
                import streamlit as st
                st.warning("⚠️ VirusTotal raw data is empty!")
                continue
                
            data = raw.get("data", {})
            if not data:
                # Debug: log structure issue
                import streamlit as st
                st.warning(f"⚠️ VirusTotal data structure issue. Raw keys: {list(raw.keys())}")
                continue
                
            attrs = data.get("attributes", {})
            if not attrs:
                # Debug: log attributes issue
                import streamlit as st
                st.warning(f"⚠️ VirusTotal attributes missing. Data keys: {list(data.keys())}")
                continue
            
            # URL Reputation & Categorization
            vt_details["reputation"] = str(attrs.get("reputation", "")) if attrs.get("reputation") else ""
            categories = attrs.get("categories", {})
            if isinstance(categories, dict) and categories:
                unique_cats = sorted(set(str(v) for v in categories.values() if v))
                vt_details["category"] = ", ".join(unique_cats[:5])  # Limit to 5 categories
            else:
                vt_details["category"] = ""
            
            stats = attrs.get("last_analysis_stats", {}) or attrs.get("stats", {})
            if stats:
                harmless = stats.get("harmless", 0)
                malicious = stats.get("malicious", 0)
                suspicious = stats.get("suspicious", 0)
                undetected = stats.get("undetected", 0)
                total = harmless + malicious + suspicious + undetected
                vt_details["counts"] = f"Clean: {harmless}, Malicious: {malicious}, Suspicious: {suspicious}, Undetected: {undetected} (Total: {total})"
            else:
                vt_details["counts"] = ""
            
            # Domain & Hosting Information
            vt_details["domain"] = str(data.get("id", "")) or ""
            vt_details["whois"] = "Available" if attrs.get("whois") else ""
            vt_details["country"] = str(attrs.get("country", "")) if attrs.get("country") else ""
            asn = attrs.get("asn")
            vt_details["asn"] = f"AS{asn}" if asn else ""
            
            # DNS Records & Network Artifacts
            dns_records = attrs.get("last_dns_records") or attrs.get("dns_records")
            vt_details["dns"] = "Available" if dns_records else ""
            ip_addrs = []
            if dns_records:
                for record_type, records in (dns_records.items() if isinstance(dns_records, dict) else []):
                    if isinstance(records, list):
                        for rec in records:
                            if isinstance(rec, dict) and rec.get("value"):
                                ip_addrs.append(str(rec.get("value")))
            vt_details["ips"] = ", ".join(ip_addrs[:5]) if ip_addrs else ""
            
            # Static Content Inspection
            vt_details["html_title"] = str(attrs.get("title", "")) if attrs.get("title") else ""
            outgoing_links = attrs.get("outgoing_links", [])
            if isinstance(outgoing_links, list) and outgoing_links:
                vt_details["scripts"] = f"{len(outgoing_links)} external resources found"
            else:
                vt_details["scripts"] = ""
            tags = attrs.get("tags", [])
            if isinstance(tags, list) and tags:
                vt_details["resources"] = ", ".join([str(t) for t in tags[:8]])
            else:
                vt_details["resources"] = ""
            
            # Dynamic Behavioral Analysis
            redirect_chain = attrs.get("redirection_chain", [])
            if isinstance(redirect_chain, list) and redirect_chain:
                vt_details["redirects"] = f"{len(redirect_chain)} redirect(s)"
            else:
                vt_details["redirects"] = ""
            downloads = attrs.get("downloaded_files", [])
            vt_details["downloads"] = f"{len(downloads)} file(s)" if downloads else ""
            behavior = attrs.get("behaviour_summary")
            vt_details["execution"] = "Behavior captured" if behavior else ""
            
            # Connections & Relationships
            relationships = data.get("relationships", {})
            linked_files = relationships.get("downloaded_files", {}).get("data", [])
            vt_details["linked"] = f"{len(linked_files)} items" if linked_files else ""
            comm_files = relationships.get("communicating_files", {}).get("data", [])
            vt_details["files"] = f"{len(comm_files)} files" if comm_files else ""
            contacted_domains = relationships.get("contacted_domains", {}).get("data", [])
            vt_details["domains"] = f"{len(contacted_domains)} domains" if contacted_domains else ""
            
            # SSL/TLS Certificate Information
            cert = attrs.get("last_https_certificate", {})
            if isinstance(cert, dict):
                vt_details["cert_issuer"] = str(cert.get("issuer", "")) if cert.get("issuer") else ""
                vt_details["cert_subject"] = str(cert.get("subject", "")) if cert.get("subject") else ""
                validity = cert.get("validity")
                if validity:
                    vt_details["cert_validity"] = f"Valid from {validity.get('not_before', '')} to {validity.get('not_after', '')}"
                else:
                    vt_details["cert_validity"] = ""
            else:
                vt_details["cert_issuer"] = ""
                vt_details["cert_subject"] = ""
                vt_details["cert_validity"] = ""
            
            # Antivirus / Engine Detections
            if stats:
                vt_details["av_stats"] = vt_details.get("counts", "")
            else:
                vt_details["av_stats"] = ""
            last_results = attrs.get("last_analysis_results", {})
            malicious_engs = []
            if isinstance(last_results, dict):
                for eng_name, result in last_results.items():
                    if isinstance(result, dict) and result.get("category") == "malicious":
                        malicious_engs.append(eng_name)
            vt_details["av_malicious"] = ", ".join(malicious_engs[:10]) if malicious_engs else ""
            
            # Heuristic & Machine Learning Scoring
            verdict = attrs.get("verdict")
            vt_details["ml_verdict"] = str(verdict) if verdict else ""
            ml_tags = attrs.get("tags", [])
            if isinstance(ml_tags, list) and ml_tags:
                vt_details["ml_tags"] = ", ".join([str(t) for t in ml_tags[:12]])
            else:
                vt_details["ml_tags"] = ""
            
            # Historical & Community Data
            votes = attrs.get("total_votes", {})
            if isinstance(votes, dict):
                harmless_votes = votes.get("harmless", 0)
                malicious_votes = votes.get("malicious", 0)
                if harmless_votes or malicious_votes:
                    vt_details["community"] = f"Safe: {harmless_votes}, Unsafe: {malicious_votes}"
                else:
                    vt_details["community"] = ""
            else:
                vt_details["community"] = ""
            
            first_sub = attrs.get("first_submission_date")
            if first_sub:
                try:
                    from datetime import datetime
                    dt = datetime.fromtimestamp(first_sub)
                    vt_details["first_seen"] = dt.isoformat() + "Z"
                except:
                    vt_details["first_seen"] = str(first_sub)
            else:
                vt_details["first_seen"] = ""
            
            last_analysis = attrs.get("last_analysis_date")
            if last_analysis:
                try:
                    from datetime import datetime
                    dt = datetime.fromtimestamp(last_analysis)
                    vt_details["last_seen"] = dt.isoformat() + "Z"
                except:
                    vt_details["last_seen"] = str(last_analysis)
            else:
                vt_details["last_seen"] = ""
            
            break  # Only process first VirusTotal engine
    
    # Extract data from urlscan.io if available
    for eng in res.get("engines", []):
        if eng.get("engine") == "urlscan.io":
            raw = eng.get("raw", {})
            # urlscan provides additional context that can supplement VT data
            verdicts = raw.get("verdicts", {})
            if verdicts:
                overall = verdicts.get("overall", {})
                if overall.get("malicious"):
                    if not vt_details.get("reputation"):
                        vt_details["reputation"] = "High risk (urlscan.io flagged)"
            break
    
    # Extract data from OTX if available
    for eng in res.get("engines", []):
        if eng.get("engine") == "AlienVault OTX":
            summary = eng.get("summary", {})
            pulses = summary.get("pulses", 0)
            if pulses and pulses > 0:
                if not vt_details.get("reputation"):
                    vt_details["reputation"] = f"Risk detected ({pulses} threat intelligence pulse(s))"
            break
    
    return vt_details

def save_scan_result(res: dict, input_value: str):
    """Save scan result to database."""
    try:
        # Extract summary from engines
        summary_parts = []
        for eng in res.get("engines", []):
            engine_name = eng.get("engine", "Unknown")
            eng_summary = eng.get("summary", {})
            if eng_summary:
                summary_parts.append(f"{engine_name}: {json.dumps(eng_summary)}")
        
        summary = " | ".join(summary_parts) if summary_parts else json.dumps(res)
        
        # Extract detailed vt_details from engine responses
        vt_details = _extract_vt_details(res)
        
        # Debug: Show what we extracted
        with st.expander("🔍 Debug: Extracted Data (Click to view)", expanded=False):
            st.write("**vt_details keys:**", list(vt_details.keys()))
            st.write("**Sample values:**")
            for k, v in list(vt_details.items())[:10]:
                val_str = str(v)[:100] if v else "None"
                st.write(f"- {k}: `{val_str}`")
            st.write("**Full vt_details:**")
            st.json(vt_details)
        
        # Save to database
        scan_id = record_search(
            scan_type=res.get("type", "unknown"),
            input_value=input_value,
            summary=summary[:1000] if len(summary) > 1000 else summary,  # Limit summary length
            risk_score=res.get("overall_risk", ""),
            vt_details=vt_details,
            db_path=get_db_path()
        )
        return scan_id
    except Exception as e:
        import traceback
        st.warning(f"Failed to save scan to database: {e}")
        st.error(f"Traceback: {traceback.format_exc()}")
        return None

if btn_url and url:
    with st.spinner("Scanning URL…"):
        try:
            res = aggregate_scan(url, "url")
            render_result(res)
            # Save scan result to database
            scan_id = save_scan_result(res, url)
            if scan_id:
                st.markdown(f"""
                <div style="background: rgba(6, 182, 212, 0.1); border: 1px solid rgba(6, 182, 212, 0.3); 
                            border-radius: 12px; padding: 1rem; margin: 1rem 0;">
                    <span style="color: #06b6d4; font-weight: 500;">✅ Scan saved to history (ID: {scan_id})</span>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Scan failed: {e}")

if btn_file and up is not None:
    with st.spinner("Hashing and checking file…"):
        try:
            # Save to temp buffer and hash
            b = up.read()
            h = file_hash_sha256  # keep compatibility with your existing helper
            sha = h(io.BytesIO(b)) if callable(h) and h.__code__.co_argcount == 1 else None
            # if the older helper expects a path, compute here quickly
            if sha is None:
                import hashlib
                hh = hashlib.sha256(); hh.update(b); sha = hh.hexdigest()
            res = aggregate_scan(sha, "hash")
            render_result(res)
            # Save scan result to database (use filename or hash as input)
            input_value = f"{up.name} (SHA256: {sha})" if up.name else f"SHA256: {sha}"
            scan_id = save_scan_result(res, input_value)
            if scan_id:
                st.markdown(f"""
                <div style="background: rgba(6, 182, 212, 0.1); border: 1px solid rgba(6, 182, 212, 0.3); 
                            border-radius: 12px; padding: 1rem; margin: 1rem 0;">
                    <span style="color: #06b6d4; font-weight: 500;">✅ Scan saved to history (ID: {scan_id})</span>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Scan failed: {e}")
