from pathlib import Path

import streamlit as st
from PIL import Image

# Nasconde il menu laterale, il footer e l’header
hide_sidebar = """
    <style>
        [data-testid="stSidebarNav"] { display: none; }
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

BASE_PATH=Path(__file__).resolve().parent
BACKGROUND_PATH=Path(f"{BASE_PATH}/data/img/sfondo_welcome.png")


st.title("Benvenuto in QuestMasterAI 👋")

st.image(BACKGROUND_PATH)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Gioca La Nostra Storia")
    st.page_link("pages/create_story.py", label="gioca la Nostra Storia", icon="🏠")

with col2:
    st.subheader("Crea la nuova Storia")
    #st.page_link("pages/page_1.py", label="Crea la nuova Storia", icon="1️⃣")
