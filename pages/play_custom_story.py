import json

import streamlit as st

from src.utils.constant import STORY_PATH

hide_sidebar = """
    <style>
        [data-testid="stSidebarNav"] { display: none; }
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

st.set_page_config(page_title="Inizia il gioco", layout="centered")
st.title("Gioca la storia appena creata")

@st.cache_data
def load_story():
    with open(STORY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

story = load_story()

if "current_state" not in st.session_state:
    st.session_state.current_state = "start"

state = st.session_state.current_state

scene = story[state]
st.markdown(f"### {scene['text']}")

print(scene.get("actions"))
if scene.get("actions"):
    for action_text, next_state in scene["actions"].items():
        if st.button(action_text):
            st.session_state.current_state = next_state
            st.rerun()
else:
    st.success(" Fine dell'avventura. Ricarica la pagina per ricominciare.")
