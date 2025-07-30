import streamlit as st

from src.phase_1 import do_phase_1

hide_sidebar = """
    <style>
        [data-testid="stSidebarNav"] { display: none; }
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Stile coerente con le pagine precedenti */
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

        /* Container per le sezioni */
        .card-container {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .card-container:hover {
            transform: translateY(-2px);
        }

        /* Container principale */
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem 1rem;
        }

        /* Stile per i separatori */
        .divider {
            height: 2px;
            background: linear-gradient(90deg, transparent, #667eea, #764ba2, transparent);
            border: none;
            margin: 2rem 0;
            border-radius: 1px;
        }

        /* Stile per l'area di testo */
        .stTextArea > div > div > textarea {
            border-radius: 12px;
            border: 2px solid rgba(102, 126, 234, 0.3);
            transition: all 0.3s ease;
        }

        .stTextArea > div > div > textarea:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        /* Stile per l'expander */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
        }

        /* Footer personalizzato */
        .custom-footer {
            text-align: center;
            color: #7f8c8d;
            font-size: 1.1rem;
            margin-top: 3rem;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.02);
            border-radius: 15px;
        }

        /* Success message migliorato */
        .success-message {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            font-weight: 600;
            margin: 1rem 0;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }

        /* Responsività */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2.5rem;
            }
            .card-container {
                padding: 1.5rem;
            }
        }
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

st.set_page_config(
    page_title="Create Your Story",
    page_icon="📚",
    layout="wide"
)

# Container principale
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-title">📚 Story Generator</h1>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Instructions section
st.header("📝 Instructions for creating the perfect story opening")

# Card container per le istruzioni
st.markdown('<div class="card-container">', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🎯 Essential elements to include:

    **👤 The Protagonist:**
    - Who is the main character?
    - What are their distinctive characteristics?
    - What is their initial situation?

    **🎯 The Final Goal:**
    - What does the protagonist want to achieve?
    - What is their main dream or desire?
    - Why is this goal important to them?
    """)

with col2:
    st.markdown("""
    ### 🚧 Obstacles and Conflicts:

    **⚔️ Challenges to overcome:**
    - What difficulties must they face?
    - Who or what opposes the protagonist?
    - What are the risks or consequences?

    **🌍 The Setting:**
    - Where and when does the story take place?
    - What is the general environment?
    - What atmosphere do you want to create?
    """)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Example
with st.expander("💡 Example of a well-structured opening"):
    st.markdown("""
    *"Prince Aldric of Valdoria, heir to a kingdom plagued by an ancient curse, dreams of breaking 
    the dark magic that has withered his lands for generations. When he discovers a prophecy hidden 
    in the royal archives speaking of a Crystal of Eternal Light, he decides to embark on a perilous 
    quest to the Forbidden Mountains. However, he must face his overprotective father who forbids 
    him from leaving the castle, a treacherous council plotting to usurp the throne in his absence, 
    and the Shadow Legion - dark creatures that guard the crystal. Set in the mystical realm of 
    Valdoria, where magic flows through ancient forests and towering peaks hide deadly secrets, 
    Prince Aldric must choose between the safety of his gilded cage and a dangerous journey 
    that could either save his kingdom or destroy it forever."*

    **Elements present:**
    - **Protagonist:** Prince Aldric, young heir burdened by responsibility
    - **Goal:** Break the ancient curse and save his kingdom
    - **Obstacles:** Overprotective father, treacherous council, Shadow Legion
    - **Setting:** Mystical realm of Valdoria with magic and ancient curses
    """)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Input field for the opening
st.header("✍️ Write your story opening")

user_input = st.text_area(
    "Enter your story opening here:",
    height=200,
    placeholder="Start writing your story here... Remember to include all the essential elements!",
    help="Minimum 50 characters required. Make sure to include protagonist, goal, obstacles and setting."
)

# Character counter
char_count = len(user_input)
MININUM_LENGTH_PROMPT = 50
if char_count < MININUM_LENGTH_PROMPT:
    st.markdown(f"<p style='color: red;'>Characters entered: {char_count}/50 (minimum required)</p>",
                unsafe_allow_html=True)
else:
    st.markdown(f"<p style='color: green;'>Characters entered: {char_count} ✓</p>",
                unsafe_allow_html=True)

# Real-time validation
errors = []
warnings = []

if user_input:
    # Minimum length check
    if len(user_input.strip()) < MININUM_LENGTH_PROMPT:
        errors.append("⚠️ The story opening must contain at least 50 characters")

    # Content checks (simple)
    incipit_lower = user_input.lower()

    # Suggestions for improvement
    if len(user_input.strip()) < 100:
        warnings.append("💡 Consider adding more details to make the opening more engaging")

    if not any(word in incipit_lower for word in ['wants', 'dreams', 'desires', 'seeks', 'goal', 'aims', 'wishes']):
        warnings.append("💡 Try to make the protagonist's goal clearer")

    if not any(word in incipit_lower for word in
               ['but', 'however', 'obstacle', 'problem', 'difficulty', 'challenge', 'against']):
        warnings.append("💡 Consider adding the obstacles the protagonist must face")

# Show errors and warnings
if errors:
    for error in errors:
        st.error(error)

if warnings:
    for warning in warnings:
        st.warning(warning)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

if "nwords" not in st.session_state:
    st.session_state.nwords = 100

# Button to proceed
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🚀 Proceed with this story", type="primary", use_container_width=True):
        if not user_input.strip():
            st.error("❌ Please enter a story opening before proceeding!")
        elif len(user_input.strip()) < 50:
            st.error("❌ The opening is too short! It must contain at least 50 characters.")
        else:
            with st.spinner("Generating the story...",show_time=True):
                isValid = do_phase_1(user_input)
                #isValid = True
                if isValid:
                    st.markdown("""
                        <div class="success-message">
                            🎉 Perfect! You can now proceed to play your fantastic story!
                        </div>
                    """, unsafe_allow_html=True)
                    st.session_state.isCustom = True
                    st.balloons()

                    st.markdown("<br>", unsafe_allow_html=True)
                    col_link1, col_link2, col_link3 = st.columns([1, 2, 1])
                    with col_link2:
                        st.page_link("pages/play_story.py", label="🎮 PLAY YOUR STORY", icon="🚀")
                else:
                    st.error("Error during the validation of your story. Please change your input")
                    st.rerun()

# Footer
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown(
    "<div class='custom-footer'>"
    "💫 Create incredible stories starting from a well-structured opening!"
    "</div>",
    unsafe_allow_html=True
)

# Chiudi container principale
st.markdown('</div>', unsafe_allow_html=True)