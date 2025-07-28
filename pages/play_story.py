import json
import time

import streamlit as st

from src.agent.frontend_generator_agent import generate_and_extract_story
from src.utils.constant import STORY_EXAMPLE_PATH, STORY_PATH
from src.utils.template_html import generate_html

hide_sidebar = """
    <style>
        [data-testid="stSidebarNav"] { display: none; }
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

st.set_page_config(page_title="Inizia il gioco", layout="centered")
st.title("Gioca")

@st.cache_data
def load_story(PATH):
    with open(PATH, "r") as f:
        return json.load(f)

if st.session_state.isCustom:
    path= STORY_PATH
else:
    path= STORY_EXAMPLE_PATH

story = load_story(path)

# Stato iniziale
if "current_state" not in st.session_state:
    st.session_state.current_state = "start"
    initial_story = story["start"]["text"]
    st.session_state.selected_actions = [initial_story]
    st.session_state.story_title = ""
    st.session_state.story_text = ""

state = st.session_state.current_state
scene = story[state]

# Solo se non è già stato calcolato
if not st.session_state.story_text:
    previous_actions = str(st.session_state.selected_actions[:-1])
    last_action = str(st.session_state.selected_actions[-1])
    with st.spinner("Wait for it...", show_time=True):
        title, current_story = generate_and_extract_story(previous_actions, last_action)
    st.session_state.story_title = title
    st.session_state.story_text = current_story



# Genera l'HTML solo con i valori già memorizzati
html_code = generate_html(
    st.session_state.story_title,
    st.session_state.story_text,
    st.session_state.selected_actions[-1]
)
st.html(html_code)

# Gestione dei pulsanti azioni
num_actions = len(scene.get("actions", {}))
if num_actions > 0:
    for action_text, next_state in scene["actions"].items():
        if st.button(action_text):
            st.session_state.selected_actions.append(action_text)
            st.session_state.current_state = next_state
            st.session_state.story_text = ""  # forza rigenerazione del testo
            st.rerun()
else:
    st.success("Fine dell'avventura. Ricarica la pagina per ricominciare.")
