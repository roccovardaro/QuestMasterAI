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

st.set_page_config(
    page_title="Create Your Story",
    page_icon="📚",
    layout="wide"
)

# Main title
st.title("📚 Story Generator")
st.markdown("---")

# Instructions section
st.header("📝 Instructions for creating the perfect story opening")

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

st.markdown("---")

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

st.markdown("---")

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
MININUM_LENGTH_PROMPT= 50
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

st.markdown("---")

# Button to proceed
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🚀 Proceed with this story", type="primary", use_container_width=True):
        if not user_input.strip():
            st.error("❌ Please enter a story opening before proceeding!")
        elif len(user_input.strip()) < 50:
            st.error("❌ The opening is too short! It must contain at least 50 characters.")
        else:
            with st.spinner("Generating the story..."):
                isValid = do_phase_1(user_input)
                if isValid:
                    st.success("🎉 Perfect! You can now proceed to play your fantastic sotry!")
                    st.balloons()
                    st.session_state.isCustom=True
                    st.page_link("pages/play_story.py")

                else:
                    st.error("Error during the validation of your story. Please change your input")
                    st.rerun()
# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "💫 Create incredible stories starting from a well-structured opening!"
    "</div>",
    unsafe_allow_html=True
)