from pathlib import Path

import streamlit as st

# Nasconde il menu laterale, il footer e l'header
hide_sidebar = """
    <style>
        [data-testid="stSidebarNav"] { display: none; }
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Stile personalizzato per i bottoni */
        .stButton > button {
            width: 100%;
            height: 60px;
            font-size: 18px;
            font-weight: 600;
            border-radius: 12px;
            border: 2px solid transparent;
            transition: all 0.3s ease;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
            border: 2px solid #667eea;
        }

        /* Centratura dei page link */
        .stButton {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Stile per il titolo principale */
        .main-title {
            text-align: center;
            font-size: 3.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 2rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }

        /* Container per le colonne */
        .card-container {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .card-container:hover {
            transform: translateY(-5px);
        }

        /* Stile per i sottotitoli */
        .card-title {
            text-align: center;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            color: #2c3e50;
        }

        /* Aggiunge spazio e centratura */
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem 1rem;
        }

        /* Stile per l'immagine */
        .welcome-image {
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            margin: 2rem 0;
        }

        /* Responsività */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2.5rem;
            }
            .card-container {
                margin: 0.5rem;
                padding: 1.5rem;
            }
        }
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

BASE_PATH = Path(__file__).resolve().parent
BACKGROUND_PATH = Path(f"{BASE_PATH}/data/img/sfondo_welcome.png")

st.set_page_config(layout="wide")

if "isCustom" not in st.session_state:
    st.session_state.isCustom = False

if "nwords" not in st.session_state:
    st.session_state.nwords = 100

# Container principale
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Titolo principale con stile personalizzato
st.markdown('<h1 class="main-title">Welcome to QuestMasterAI 👋</h1>', unsafe_allow_html=True)

# Spazio vuoto per respiro visivo
st.markdown("<br>", unsafe_allow_html=True)

# Immagine centrata con stile
col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
with col_img2:
    st.markdown('<div class="welcome-image">', unsafe_allow_html=True)
    st.image(BACKGROUND_PATH, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Spazio tra immagine e bottoni
st.markdown("<br>", unsafe_allow_html=True)

# Selettore numero di parole
st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <h3 style="color: #2c3e50; font-size: 1.3rem; margin-bottom: 1rem;">⚙️ Story Settings</h3>
    </div>
""", unsafe_allow_html=True)

col_setting1, col_setting2, col_setting3 = st.columns([1, 2, 1])
with col_setting2:
    st.markdown("""
        <div class="card-container" style="margin: 1rem 0; padding: 1.5rem;">
            <p style="text-align: center; color: #34495e; margin-bottom: 1rem; font-weight: 500;">
                📝 Choose story length (number of words)
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.session_state.nwords = st.selectbox(
        "Select number of words:",
        options=[100, 150, 200, 300, 500, 750, 1000],
        index=0,  # Default a 100 parole
        key="nwords_selector",
        label_visibility="collapsed"
    )

st.markdown("<br>", unsafe_allow_html=True)

# Colonne per i bottoni con cards
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div class="card-container">
            <h3 class="card-title">🎨 Create Your Story</h3>
            <p style="text-align: center; color: #7f8c8d; margin-bottom: 1.5rem;">
                Unleash your creativity and generate unique AI-powered adventures
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/create_story.py", label="🚀 GENERATE AI STORY")

with col2:
    st.markdown("""
        <div class="card-container">
            <h3 class="card-title">🎮 Ready to Play</h3>
            <p style="text-align: center; color: #7f8c8d; margin-bottom: 1.5rem;">
                Jump right into our carefully crafted built-in adventure
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/play_story.py", label="🎯 PLAY DEVELOPERS STORY")

# Chiudi container principale
st.markdown('</div>', unsafe_allow_html=True)

# Footer minimalista (opzionale)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; color: #bdc3c7; font-size: 0.9rem; margin-top: 3rem;">
        ✨ Choose your adventure and let the magic begin ✨
    </div>
""", unsafe_allow_html=True)