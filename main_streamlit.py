# Main entry point for Streamlit app
import streamlit as st

st.set_page_config(
    page_title="VirusLens",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🛡️ VirusLens — Cyber Threat Analyzer")
st.markdown("""
Welcome to VirusLens! Use the sidebar to navigate to different sections:
- **Scan**: Scan URLs or files
- **Bulk**: Perform bulk scans
- **History**: View scan history
- **Reports**: Generate PDF reports
- **About**: Learn more about VirusLens
""")

