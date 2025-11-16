# app/utils/secrets.py
from __future__ import annotations
import os

# Load .env once (quietly)
_ENV_LOADED = False
def _ensure_dotenv_loaded() -> None:
    global _ENV_LOADED
    if _ENV_LOADED:
        return
    try:
        from dotenv import load_dotenv  # type: ignore
        from pathlib import Path
        # Try multiple locations for .env file
        # 1. Project root (go up from app/utils/secrets.py)
        project_root = Path(__file__).resolve().parents[2]
        env_file = project_root / ".env"
        
        # 2. Current working directory
        cwd_env = Path.cwd() / ".env"
        
        # Load from project root first, then current directory
        if env_file.exists():
            load_dotenv(env_file, override=False)
        elif cwd_env.exists():
            load_dotenv(cwd_env, override=False)
        else:
            # Try default location
            load_dotenv(override=False)
    except Exception as e:
        # Silently fail - will fall back to Streamlit secrets or mock mode
        pass
    _ENV_LOADED = True


def get_vt_api_key() -> str:
    """
    Resolve VirusTotal API key without surfacing Streamlit 'No secrets found' errors.

    Priority:
      1) Environment / .env: VIRUSTOTAL_API_KEY
      2) streamlit secrets: st.secrets["VIRUSTOTAL_API_KEY"]
      3) Mock mode: returns dummy key if MOCK_MODE is enabled
    """
    _ensure_dotenv_loaded()

    # Check for mock mode first
    mock_mode = os.getenv("MOCK_MODE", "false").lower() in ("1", "true", "yes")
    
    # 1) ENV / .env
    key = os.getenv("VIRUSTOTAL_API_KEY")
    if key and key != "your_api_key_here":
        return key

    # 2) streamlit secrets (swallow any error if secrets.toml is missing)
    try:
        import streamlit as st  # type: ignore
        try:
            k = st.secrets["VIRUSTOTAL_API_KEY"]  # may raise if not present
            if k and k != "your_api_key_here":
                return str(k)
        except Exception:
            pass
    except Exception:
        pass

    # 3) If mock mode is enabled, return a dummy key
    if mock_mode:
        return "mock-api-key-for-development"

    # Nothing found and not in mock mode
    raise ValueError(
        "VirusTotal API key not found. Set VIRUSTOTAL_API_KEY in your environment or .env "
        "file, or add VIRUSTOTAL_API_KEY to Streamlit secrets. "
        "Alternatively, set MOCK_MODE=true to run without an API key (for development/testing)."
    )
