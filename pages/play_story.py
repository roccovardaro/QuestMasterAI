import json


import streamlit as st

from src.agent.frontend_generator_agent import generate_and_extract_story
from src.utils.constant import STORY_EXAMPLE_PATH, STORY_PATH
from src.utils.template_html import generate_html

hide_sidebar = """
    <style>
        [data-testid="stSidebarNav"] { display: none; }
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Stile coerente con la pagina welcome */
        .stButton > button {
            width: 100%;
            height: 50px;
            font-size: 16px;
            font-weight: 600;
            border-radius: 12px;
            border: 2px solid transparent;
            transition: all 0.3s ease;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            margin: 0.5rem 0;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
            border: 2px solid #667eea;
        }

        /* Centratura dei bottoni */
        .stButton {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Titolo principale con stile coerente */
        .main-title {
            text-align: center;
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 2rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }

        /* Container per le azioni */
        .actions-container {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }

        .actions-title {
            text-align: center;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            color: #2c3e50;
        }

        /* Container principale */
        .main-container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 2rem 1rem;
        }

        /* Stile per il messaggio di fine */
        .end-message {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            font-size: 1.2rem;
            font-weight: 600;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            margin: 2rem 0;
        }

        /* Spinner personalizzato */
        .stSpinner > div {
            border-top-color: #667eea !important;
        }

        /* HTML content container */
        .story-content {
            margin: 2rem 0;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }

        /* Responsività */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2.5rem;
            }
            .actions-container {
                margin: 1rem 0;
                padding: 1.5rem;
            }
        }
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

st.set_page_config(page_title="Inizia il gioco", layout="centered")

# Container principale
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Titolo principale con stile coerente
st.markdown('<h1 class="main-title">🎮 Play the adventure</h1>', unsafe_allow_html=True)


@st.cache_data
def load_story(PATH):
    with open(PATH, "r") as f:
        return json.load(f)


if st.session_state.isCustom:
    path = STORY_PATH
else:
    path = STORY_EXAMPLE_PATH

story = load_story(path)

# Stato iniziale
if "current_state" not in st.session_state:
    st.session_state.current_state = "start"
    initial_story = story["start"]["text"]
    st.session_state.selected_actions = [initial_story]
    st.session_state.story_title = ""
    st.session_state.story_text = ""

state = st.session_state.current_state
story_length = st.session_state.nwords
scene = story[state]

# Solo se non è già stato calcolato
if not st.session_state.story_text:
    previous_actions = str(st.session_state.selected_actions[:-1])
    last_action = str(st.session_state.selected_actions[-1])
    with st.spinner("✨ Generating your story... Please wait", show_time=True):
        title, current_story = generate_and_extract_story(previous_actions, last_action, story_length)
    st.session_state.story_title = title
    st.session_state.story_text = current_story

# Genera l'HTML solo con i valori già memorizzati
html_code = generate_html(
    st.session_state.story_title,
    st.session_state.story_text,
    st.session_state.selected_actions[-1]
)

# Container per il contenuto della storia
st.markdown('<div class="story-content">', unsafe_allow_html=True)
st.html(html_code)
st.markdown('</div>', unsafe_allow_html=True)

# Gestione dei pulsanti azioni
num_actions = len(scene.get("actions", {}))
if num_actions > 0:
    st.markdown("""
        <div class="actions-container">
            <h3 class="actions-title">🎯 Choose Your Next Action</h3>
        </div>
    """, unsafe_allow_html=True)

    # Crea colonne per i bottoni se sono più di 2
    if num_actions <= 2:
        cols = st.columns(num_actions)
    else:
        cols = st.columns(2)

    actions_list = list(scene["actions"].items())
    for i, (action_text, next_state) in enumerate(actions_list):
        col_index = i % len(cols)
        with cols[col_index]:
            if st.button(action_text, key=f"action_{i}"):
                st.session_state.selected_actions.append(action_text)
                st.session_state.current_state = next_state
                st.session_state.story_text = ""  # forza rigenerazione del testo
                st.rerun()
else:
    st.markdown("""
        <div class="end-message">
            🎊 Congratulations! You've completed the adventure! 🎊
            <br><br>
            <span style="font-size: 1rem; opacity: 0.9;">
                Reload the page to start a new journey
            </span>
        </div>
    """, unsafe_allow_html=True)

# Chiudi container principale
st.markdown('</div>', unsafe_allow_html=True)