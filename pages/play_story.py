import json

import streamlit as st

from src.agent.html_generator_agent import generate_and_extract_html
from src.utils.constant import STORY_EXAMPLE_PATH


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
def load_story():
    with open(STORY_EXAMPLE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


story = load_story()

if "current_state" not in st.session_state:
    st.session_state.current_state = "start"
    initial_story=story["start"]["text"]
    st.session_state.selected_actions=[initial_story]


state = st.session_state.current_state

scene = story[state]
st.markdown(f"### {scene['text']}")


previous_actions=str(st.session_state.selected_actions[:-1])
last_action=str(st.session_state.selected_actions[-1])
html_code=generate_and_extract_html(previous_actions, last_action)
st.html(html_code)

num_actions=len(scene.get("actions"))
if  num_actions>0:
    for action_text, next_state in scene["actions"].items():
        if st.button(action_text):
            st.session_state.selected_actions.append(action_text)
            st.session_state.current_state = next_state
            st.rerun()
else:
    st.success(" Fine dell'avventura. Ricarica la pagina per ricominciare.")
