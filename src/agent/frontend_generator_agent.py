import logging
from src.utils.utils import api_generate_GEMINI, extract_html_title_and_story



def generate_story_and_title_prompt(previous_actions, last_action, n_words):

    return f"""You are a skilled storyteller. Based on the following previous actions:{previous_actions}, 
    generate a short story describing the current action : {last_action}. The story must contain exactly {n_words} words and should follow the 
    narrative thread logically. Also, create a fitting title that reflects the current event. Keep the tone engaging and 
    coherent with the established story context.
    
    Format the output as follows:
    The title must be enclosed within <TITLE> and </TITLE>
    The story must be enclosed within <STORY> and </STORY>"""



def generate_and_extract_story(previous_actions, last_action, n_words=100):
    prompt = generate_story_and_title_prompt(previous_actions, last_action, n_words)
    response = api_generate_GEMINI(prompt)

    return extract_html_title_and_story(response)


