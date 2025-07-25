import logging

from src.utils.constant import get_html_example
from src.utils.utils import api_generate_GEMINI, extract_html



def generate_html_prompt(previous_actions, last_action):

    html_example= get_html_example()

    return (f"""Given the following story context, where there is a sequence of previous actions followed by a final action, 
    continue the story logically and creatively. Then, generate a beautiful and well-formatted HTML page that presents this continuation. 
    The HTML should include elegant styling (using inline CSS or minimal styles), with appropriate use of headings, paragraphs, 
    and maybe a background or subtle visual theme that fits the narrative tone. Generate maximum 50 words. Wrap the final HTML inside the tags <GEN_HTML> and </GEN_HTML>.

    Previous actions:
    - {previous_actions}
    
    Last action:
    - {last_action}
    
    Write the continuation of the story based on the above, and present it as beautiful HTML between <GEN_HTML> and </GEN_HTML>.

    Example HTML:   
    
    {html_example}
    mantain the same style.

    """)



def generate_and_extract_html(previous_actions, last_action):
    prompt = generate_html_prompt(previous_actions, last_action)
    response = api_generate_GEMINI(prompt)

    html_code=extract_html(response)
    return html_code


