# app/pages/05_About.py
"""
About page for VirusLens — Cyber Threat Analyzer.
"""

from __future__ import annotations

import streamlit as st
from app.utils.ui import setup_page, apply_theme

setup_page("About")
apply_theme()

# Hero Section - Responsive
st.markdown("""
<div style="text-align: center; padding: clamp(1.5rem, 4vw, 2rem) 0;">
    <h1 style="font-size: clamp(2rem, 6vw, 3rem); margin-bottom: 0.5rem;">ℹ️ About VirusLens</h1>
    <p style="font-size: clamp(1rem, 3vw, 1.1rem); color: #94a3b8;">Cyber Threat Analyzer</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# About Card - Responsive
st.markdown("""
<div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
            border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 20px; 
            padding: clamp(1.5rem, 4vw, 2.5rem); margin: clamp(1rem, 3vw, 2rem) 0;">
    <p style="color: #cbd5e1; font-size: clamp(0.95rem, 2.5vw, 1.1rem); line-height: 1.8; margin: 0;">
        VirusLens is a modern <strong style="color: #8b5cf6;">Cyber Threat Analyzer</strong> built with Streamlit.
        It integrates local persistence, VirusTotal lookups, hash lookups, URL scanning submissions,
        and export features (CSV / PDF). This page explains what the app does and its core features.
    </p>
</div>
""", unsafe_allow_html=True)

# What this website does - Responsive
st.markdown("""
<div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
            border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 20px; 
            padding: clamp(1.5rem, 4vw, 2.5rem); margin: clamp(1rem, 3vw, 2rem) 0;">
    <h2 style="color: #f1f5f9; margin-top: 0; margin-bottom: 1.5rem; font-size: clamp(1.5rem, 4vw, 1.75rem);">✨ What this website does</h2>
    <ul style="color: #cbd5e1; line-height: clamp(2, 4vw, 2.5); font-size: clamp(0.95rem, 2.5vw, 1.05rem); padding-left: 1.5rem;">
        <li style="margin-bottom: 0.75rem;"><strong style="color: #8b5cf6;">🔍 URL scanning</strong> — Submit a URL to VirusTotal (v3) for analysis and optionally poll until results are ready.</li>
        <li style="margin-bottom: 0.75rem;"><strong style="color: #8b5cf6;">🔐 Hash lookup</strong> — Query VirusTotal for an existing file hash (MD5 / SHA1 / SHA256) to view the last analysis.</li>
        <li style="margin-bottom: 0.75rem;"><strong style="color: #8b5cf6;">📊 History / Audit</strong> — Every search/operation performed in the UI is recorded (type, query, summary, timestamp).</li>
        <li style="margin-bottom: 0.75rem;"><strong style="color: #8b5cf6;">📥 Exports</strong> — Saved scans can be exported to CSV, and individual scan details can be exported to PDF.</li>
        <li style="margin-bottom: 0.75rem;"><strong style="color: #8b5cf6;">⚡ Bulk operations</strong> — Support for doing batch or bulk scanning flows.</li>
        <li><strong style="color: #8b5cf6;">🧪 Mock mode</strong> — A local testing mode that returns deterministic mock responses so you can develop without hitting API rate limits.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Key features - Responsive
st.markdown("""
<div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
            border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 20px; 
            padding: clamp(1.5rem, 4vw, 2.5rem); margin: clamp(1rem, 3vw, 2rem) 0;">
    <h2 style="color: #f1f5f9; margin-top: 0; margin-bottom: 1.5rem; font-size: clamp(1.5rem, 4vw, 1.75rem);">🚀 Key features</h2>
</div>
""", unsafe_allow_html=True)

# Responsive columns: 1 on mobile, 3 on desktop
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.8); backdrop-filter: blur(10px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
                padding: clamp(1.5rem, 4vw, 2rem); text-align: center; 
                min-height: 180px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: clamp(2.5rem, 6vw, 3rem); margin-bottom: 1rem;">💾</div>
        <h3 style="color: #f1f5f9; margin-bottom: 0.5rem; font-size: clamp(1.1rem, 3vw, 1.3rem);">Persistence</h3>
        <p style="color: #94a3b8; font-size: clamp(0.85rem, 2vw, 0.95rem); margin: 0;">All scans and history are stored in a local SQLite database.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.8); backdrop-filter: blur(10px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
                padding: clamp(1.5rem, 4vw, 2rem); text-align: center;
                min-height: 180px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: clamp(2.5rem, 6vw, 3rem); margin-bottom: 1rem;">📤</div>
        <h3 style="color: #f1f5f9; margin-bottom: 0.5rem; font-size: clamp(1.1rem, 3vw, 1.3rem);">Exporting</h3>
        <p style="color: #94a3b8; font-size: clamp(0.85rem, 2vw, 0.95rem); margin: 0;">Quick export to CSV for all scans. Per-scan PDF export available.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.8); backdrop-filter: blur(10px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 16px; 
                padding: clamp(1.5rem, 4vw, 2rem); text-align: center;
                min-height: 180px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: clamp(2.5rem, 6vw, 3rem); margin-bottom: 1rem;">🛡️</div>
        <h3 style="color: #f1f5f9; margin-bottom: 0.5rem; font-size: clamp(1.1rem, 3vw, 1.3rem);">Safe Development</h3>
        <p style="color: #94a3b8; font-size: clamp(0.85rem, 2vw, 0.95rem); margin: 0;">Set MOCK_MODE=true in .env to avoid hitting live APIs while developing.</p>
    </div>
    """, unsafe_allow_html=True)
