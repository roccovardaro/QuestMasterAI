import streamlit as st

from src.phase_1 import do_phase_1

hide_sidebar = """
    <style>
        [data-testid="stSidebarNav"] { display: none; }
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

st.set_page_config(page_title="Chat LLM", layout="centered")

st.title("💬 Chat con un LLM")
st.markdown("Scrivi un messaggio per interagire con il modello linguistico.")

# Input dell'utente
user_input = st.text_area("✍️ Scrivi qui il tuo messaggio", height=150)

# Bottone per inviare
if st.button("Invia"):
    if user_input.strip() == "":
        st.warning("Per favore, inserisci un messaggio prima di inviare.")
    else:
        with st.spinner("Sto generando la risposta..."):
            isValid = do_phase_1(user_input)
            if isValid:
                st.success("Storia generata correttamente!")
                st.page_link("play_custom_story.py")  # opzionale
            else:
                st.error("Errore durante la generazione della risposta.")
                st.rerun()
