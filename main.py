# Main entry point for VirusLens Streamlit app
import streamlit as st
from app.utils.ui import setup_page, apply_theme

setup_page("VirusLens")
apply_theme()

# Hero Section - Responsive
st.markdown("""
<div style="text-align: center; padding: clamp(2rem, 6vw, 4rem) clamp(1rem, 4vw, 2rem);">
    <h1 style="font-size: clamp(2.5rem, 8vw, 4rem); margin-bottom: 1rem; background: linear-gradient(135deg, #8b5cf6 0%, #06b6d4 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1.2;">
        🛡️ VirusLens
    </h1>
    <p style="font-size: clamp(1.1rem, 3vw, 1.5rem); color: #94a3b8; margin-bottom: clamp(2rem, 5vw, 3rem); font-weight: 300;">
        Cyber Threat Analyzer
    </p>
</div>
""", unsafe_allow_html=True)

# Feature Cards - Responsive: 1 column on mobile, 3 on desktop
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 20px; 
                padding: clamp(1.5rem, 4vw, 2rem); text-align: center; transition: all 0.3s ease;
                min-height: 180px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: clamp(2.5rem, 6vw, 3rem); margin-bottom: 1rem;">🔍</div>
        <h3 style="color: #f1f5f9; margin-bottom: 0.5rem; font-size: clamp(1.1rem, 3vw, 1.3rem);">Scan</h3>
        <p style="color: #94a3b8; font-size: clamp(0.85rem, 2vw, 0.9rem); margin: 0;">Analyze URLs and files for threats</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 20px; 
                padding: clamp(1.5rem, 4vw, 2rem); text-align: center;
                min-height: 180px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: clamp(2.5rem, 6vw, 3rem); margin-bottom: 1rem;">📊</div>
        <h3 style="color: #f1f5f9; margin-bottom: 0.5rem; font-size: clamp(1.1rem, 3vw, 1.3rem);">History</h3>
        <p style="color: #94a3b8; font-size: clamp(0.85rem, 2vw, 0.9rem); margin: 0;">View all your past scans</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
                border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 20px; 
                padding: clamp(1.5rem, 4vw, 2rem); text-align: center;
                min-height: 180px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: clamp(2.5rem, 6vw, 3rem); margin-bottom: 1rem;">📄</div>
        <h3 style="color: #f1f5f9; margin-bottom: 0.5rem; font-size: clamp(1.1rem, 3vw, 1.3rem);">Reports</h3>
        <p style="color: #94a3b8; font-size: clamp(0.85rem, 2vw, 0.9rem); margin: 0;">Generate detailed PDF reports</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Quick Start Section - Responsive
st.markdown("""
<div style="background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); 
            border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 20px; 
            padding: clamp(1.5rem, 4vw, 2.5rem); margin-top: clamp(1rem, 3vw, 2rem);">
    <h2 style="color: #f1f5f9; margin-top: 0; font-size: clamp(1.5rem, 4vw, 1.75rem);">🚀 Quick Start</h2>
    <p style="color: #94a3b8; line-height: 1.8; font-size: clamp(0.95rem, 2.5vw, 1rem);">
        Use the <strong style="color: #8b5cf6;">navigation sidebar</strong> to access different sections:
    </p>
    <ul style="color: #cbd5e1; line-height: clamp(2, 4vw, 2.5); font-size: clamp(0.9rem, 2.5vw, 1rem); padding-left: 1.5rem;">
        <li style="margin-bottom: 0.75rem;"><strong style="color: #8b5cf6;">Scan</strong> - Analyze URLs or files for security threats</li>
        <li style="margin-bottom: 0.75rem;"><strong style="color: #8b5cf6;">Bulk</strong> - Perform multiple scans at once</li>
        <li style="margin-bottom: 0.75rem;"><strong style="color: #8b5cf6;">History</strong> - Review all your past scan results</li>
        <li style="margin-bottom: 0.75rem;"><strong style="color: #8b5cf6;">Reports</strong> - Generate professional PDF reports</li>
        <li><strong style="color: #8b5cf6;">About</strong> - Learn more about VirusLens</li>
    </ul>
</div>
""", unsafe_allow_html=True)

