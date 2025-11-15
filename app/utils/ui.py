# app/utils/ui.py
from __future__ import annotations
import streamlit as st

# Modern Gen Z Color Palette
BG_GRADIENT_START = "#0a0e27"
BG_GRADIENT_END = "#1a1f3a"
SIDEBAR_BG = "rgba(15, 23, 42, 0.8)"
CARD_BG = "rgba(30, 41, 59, 0.6)"
ACCENT_PRIMARY = "#8b5cf6"  # Vibrant purple
ACCENT_SECONDARY = "#06b6d4"  # Cyan
ACCENT_GRADIENT = "linear-gradient(135deg, #8b5cf6 0%, #06b6d4 100%)"
TEXT_PRIMARY = "#f1f5f9"
TEXT_SECONDARY = "#cbd5e1"
TEXT_MUTED = "#94a3b8"
SUCCESS = "#10b981"
WARNING = "#f59e0b"
ERROR = "#ef4444"

def setup_page(title: str = "VirusLens — Cyber Threat Analyzer") -> None:
    """Must be the first Streamlit call on every page."""
    st.set_page_config(
        page_title=title,
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items=None
    )

def apply_theme(title_note: str = "VirusLens") -> None:
    """Modern Gen Z minimalist theme with glassmorphism and smooth animations."""
    # Add viewport meta for mobile
    st.markdown("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    """, unsafe_allow_html=True)
    
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        * {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }}
        
        /* ======= Base Layout ======= */
        .stApp {{
            background: linear-gradient(135deg, {BG_GRADIENT_START} 0%, {BG_GRADIENT_END} 100%);
            background-attachment: fixed;
        }}
        
        .block-container {{
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 3rem;
            margin-left: auto !important;
            margin-right: auto !important;
        }}
        
        html, body, [data-testid="stAppViewContainer"] {{
            background: transparent;
        }}
        
        /* ======= Header ======= */
        header[data-testid="stHeader"] {{
            background: rgba(15, 23, 42, 0.5);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(139, 92, 246, 0.1);
        }}
        
        /* ======= Sidebar - Glassmorphism ======= */
        [data-testid="stSidebar"] {{
            background: {SIDEBAR_BG};
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(139, 92, 246, 0.1);
            width: 280px !important;
        }}
        
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {{
            padding: 1rem 0;
        }}
        
        [data-testid="stSidebar"] .css-1d391kg {{
            padding-top: 2rem;
        }}
        
        /* ======= Typography ======= */
        h1 {{
            font-size: 2.5rem;
            font-weight: 800;
            background: {ACCENT_GRADIENT};
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.2;
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
        }}
        
        h2 {{
            font-size: 1.75rem;
            font-weight: 700;
            color: {TEXT_PRIMARY};
            margin-top: 2rem;
            margin-bottom: 1rem;
            letter-spacing: -0.01em;
        }}
        
        h3 {{
            font-size: 1.5rem;
            font-weight: 600;
            color: {TEXT_PRIMARY};
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }}
        
        h4 {{
            font-size: 1.25rem;
            font-weight: 600;
            color: {TEXT_PRIMARY};
        }}
        
        p, .stMarkdown, .stText, label, span {{
            color: {TEXT_SECONDARY};
            line-height: 1.6;
        }}
        
        /* ======= Cards - Glassmorphism ======= */
        .stCard {{
            background: {CARD_BG};
            backdrop-filter: blur(20px);
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 16px;
            padding: 1.5rem;
            margin: 1rem 0;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        .stCard:hover {{
            border-color: rgba(139, 92, 246, 0.4);
            transform: translateY(-2px);
            box-shadow: 0 10px 40px rgba(139, 92, 246, 0.15);
        }}
        
        /* ======= Buttons - Modern Gradient ======= */
        .stButton > button {{
            background: {ACCENT_GRADIENT};
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 2rem;
            font-weight: 600;
            font-size: 0.95rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);
            width: 100%;
        }}
        
        .stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(139, 92, 246, 0.4);
            filter: brightness(1.1);
        }}
        
        .stButton > button:active {{
            transform: translateY(0);
        }}
        
        /* ======= Input Fields - Modern Style ======= */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > select,
        .stNumberInput > div > div > input {{
            background: {CARD_BG};
            backdrop-filter: blur(10px);
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 12px;
            color: {TEXT_PRIMARY};
            padding: 0.75rem 1rem;
            font-size: 0.95rem;
            transition: all 0.3s ease;
        }}
        
        .stTextInput > div > div > input:focus,
        .stSelectbox > div > div > select:focus,
        .stNumberInput > div > div > input:focus {{
            border-color: {ACCENT_PRIMARY};
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);
            outline: none;
        }}
        
        /* ======= File Uploader ======= */
        .stFileUploader {{
            background: {CARD_BG};
            backdrop-filter: blur(10px);
            border: 2px dashed rgba(139, 92, 246, 0.3);
            border-radius: 16px;
            padding: 2rem;
            transition: all 0.3s ease;
        }}
        
        .stFileUploader:hover {{
            border-color: rgba(139, 92, 246, 0.5);
            background: rgba(30, 41, 59, 0.8);
        }}
        
        /* ======= Expanders ======= */
        .streamlit-expanderHeader {{
            background: {CARD_BG};
            backdrop-filter: blur(10px);
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 12px;
            padding: 1rem;
            font-weight: 600;
            color: {TEXT_PRIMARY};
            transition: all 0.3s ease;
        }}
        
        .streamlit-expanderHeader:hover {{
            border-color: rgba(139, 92, 246, 0.4);
            background: rgba(30, 41, 59, 0.8);
        }}
        
        /* ======= Success/Error/Warning Messages ======= */
        .stSuccess {{
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: 12px;
            padding: 1rem;
        }}
        
        .stError {{
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.3);
            border-radius: 12px;
            padding: 1rem;
        }}
        
        .stWarning {{
            background: rgba(245, 158, 11, 0.1);
            border: 1px solid rgba(245, 158, 11, 0.3);
            border-radius: 12px;
            padding: 1rem;
        }}
        
        .stInfo {{
            background: rgba(6, 182, 212, 0.1);
            border: 1px solid rgba(6, 182, 212, 0.3);
            border-radius: 12px;
            padding: 1rem;
        }}
        
        /* ======= Dataframes/Tables ======= */
        .dataframe {{
            background: {CARD_BG};
            backdrop-filter: blur(10px);
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 12px;
            overflow: auto;
            width: 100%;
        }}
        
        /* Mobile table optimizations */
        @media (max-width: 768px) {{
            .dataframe {{
                font-size: 0.85rem;
                display: block;
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
            }}
            
            .dataframe table {{
                min-width: 100%;
            }}
            
            .dataframe th,
            .dataframe td {{
                padding: 0.5rem 0.25rem;
                white-space: nowrap;
            }}
        }}
        
        /* Very small screens - make tables scrollable */
        @media (max-width: 480px) {{
            .dataframe {{
                font-size: 0.75rem;
            }}
            
            .dataframe th,
            .dataframe td {{
                padding: 0.4rem 0.2rem;
                font-size: 0.75rem;
            }}
        }}
        
        /* ======= Spinner ======= */
        .stSpinner > div {{
            border-top-color: {ACCENT_PRIMARY};
        }}
        
        /* ======= Sidebar Navigation ======= */
        [data-testid="stSidebar"] a {{
            color: {TEXT_SECONDARY};
            text-decoration: none;
            padding: 0.75rem 1rem;
            border-radius: 10px;
            display: block;
            transition: all 0.2s ease;
            margin: 0.25rem 0;
        }}
        
        [data-testid="stSidebar"] a:hover {{
            background: rgba(139, 92, 246, 0.1);
            color: {ACCENT_PRIMARY};
            transform: translateX(4px);
        }}
        
        /* ======= Scrollbar ======= */
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        
        ::-webkit-scrollbar-track {{
            background: rgba(15, 23, 42, 0.5);
        }}
        
        ::-webkit-scrollbar-thumb {{
            background: {ACCENT_GRADIENT};
            border-radius: 4px;
        }}
        
        ::-webkit-scrollbar-thumb:hover {{
            background: {ACCENT_PRIMARY};
        }}
        
        /* ======= Mobile Responsive ======= */
        /* Tablet and below */
        @media (max-width: 768px) {{
            .block-container {{
                max-width: 100vw;
                padding: 1rem 0.5rem;
                padding-top: 0.5rem;
            }}
            
            h1 {{
                font-size: 2rem !important;
                line-height: 1.2;
                margin-bottom: 0.5rem;
            }}
            
            h2 {{
                font-size: 1.5rem !important;
                margin-top: 1.5rem;
            }}
            
            h3 {{
                font-size: 1.25rem !important;
            }}
            
            /* Sidebar adjustments */
            [data-testid="stSidebar"] {{
                width: 100% !important;
                min-width: 100% !important;
            }}
            
            /* Buttons - larger touch targets */
            .stButton > button {{
                min-height: 48px;
                font-size: 1rem;
                padding: 0.875rem 1.5rem;
            }}
            
            /* Inputs - larger and easier to tap */
            .stTextInput > div > div > input,
            .stSelectbox > div > div > select,
            .stNumberInput > div > div > input {{
                min-height: 48px;
                font-size: 16px; /* Prevents zoom on iOS */
                padding: 0.875rem 1rem;
            }}
            
            /* File uploader */
            .stFileUploader {{
                padding: 1.5rem;
                min-height: 120px;
            }}
            
            /* Cards - full width on mobile */
            [data-testid="stMarkdownContainer"] > div {{
                width: 100% !important;
            }}
        }}
        
        /* Mobile phones */
        @media (max-width: 480px) {{
            .block-container {{
                padding: 0.75rem 0.5rem;
                padding-top: 0.25rem;
            }}
            
            h1 {{
                font-size: 1.75rem !important;
                margin-bottom: 0.25rem;
            }}
            
            h2 {{
                font-size: 1.35rem !important;
                margin-top: 1rem;
            }}
            
            h3 {{
                font-size: 1.15rem !important;
            }}
            
            /* Even larger touch targets for phones */
            .stButton > button {{
                min-height: 52px;
                font-size: 1.05rem;
                padding: 1rem 1.5rem;
                margin: 0.5rem 0;
            }}
            
            /* Inputs */
            .stTextInput > div > div > input,
            .stSelectbox > div > div > select,
            .stNumberInput > div > div > input {{
                min-height: 52px;
                font-size: 16px;
            }}
            
            /* Expanders - easier to tap */
            .streamlit-expanderHeader {{
                min-height: 48px;
                padding: 1rem;
                font-size: 1rem;
            }}
            
            /* Better spacing */
            .element-container {{
                margin-bottom: 1rem;
            }}
            
            /* Hide sidebar on mobile by default, show as overlay */
            [data-testid="stSidebar"] {{
                position: fixed;
                top: 0;
                left: 0;
                height: 100vh;
                z-index: 999;
                transform: translateX(-100%);
                transition: transform 0.3s ease;
            }}
            
            [data-testid="stSidebar"][aria-expanded="true"] {{
                transform: translateX(0);
            }}
        }}
        
        /* Very small phones */
        @media (max-width: 360px) {{
            h1 {{
                font-size: 1.5rem !important;
            }}
            
            h2 {{
                font-size: 1.2rem !important;
            }}
            
            .stButton > button {{
                font-size: 0.95rem;
                padding: 0.875rem 1.25rem;
            }}
        }}
        
        /* Landscape mobile */
        @media (max-width: 900px) and (orientation: landscape) {{
            .block-container {{
                padding-top: 0.5rem;
            }}
            
            h1 {{
                font-size: 1.75rem !important;
            }}
        }}
        
        /* Touch device optimizations */
        @media (hover: none) and (pointer: coarse) {{
            /* Larger tap targets for touch devices */
            button, a, input, select {{
                min-height: 44px; /* iOS minimum */
            }}
            
            /* Remove hover effects on touch */
            .stButton > button:hover {{
                transform: none;
            }}
            
            /* Better spacing for touch */
            .element-container {{
                margin-bottom: 1.25rem;
            }}
        }}
        
        /* Prevent text size adjustment on iOS */
        html {{
            -webkit-text-size-adjust: 100%;
            text-size-adjust: 100%;
        }}
        
        /* Better scrolling on mobile */
        body {{
            -webkit-overflow-scrolling: touch;
        }}
        
        /* ======= Mobile Column Stacking ======= */
        @media (max-width: 768px) {{
            /* Force single column on mobile */
            [data-testid="column"] {{
                width: 100% !important;
                flex: 1 1 100% !important;
            }}
        }}
        
        /* ======= Mobile Selectbox/Dropdown ======= */
        @media (max-width: 480px) {{
            .stSelectbox > div > div > select {{
                font-size: 16px !important; /* Prevents zoom on iOS */
                padding: 1rem !important;
            }}
        }}
        
        /* ======= Mobile Viewport Fix ======= */
        @media (max-width: 768px) {{
            /* Ensure proper viewport handling */
            html {{
                -webkit-text-size-adjust: 100%;
                -ms-text-size-adjust: 100%;
            }}
            
            /* Better tap highlighting */
            * {{
                -webkit-tap-highlight-color: rgba(139, 92, 246, 0.2);
            }}
        }}
        
        /* ======= Mobile Sidebar Toggle ======= */
        @media (max-width: 768px) {{
            /* Make sidebar toggle more visible on mobile */
            [data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] {{
                background: rgba(139, 92, 246, 0.2);
                border: 1px solid rgba(139, 92, 246, 0.4);
                border-radius: 8px;
                padding: 0.5rem;
                min-width: 44px;
                min-height: 44px;
            }}
        }}
        
        /* ======= Animations ======= */
        @keyframes fadeIn {{
            from {{
                opacity: 0;
                transform: translateY(10px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .main .block-container {{
            animation: fadeIn 0.5s ease-out;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
