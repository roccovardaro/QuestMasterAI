import json
import logging
from src.utils.constant import get_lore, get_domain, get_problem, get_sas_plan, get_story_example
from src.utils.utils import api_generate_GEMINI, extract_and_save_story


def generate_prompt_for_story():

    lore=get_lore()
    domain=get_domain()
    problem=get_problem()
    plan=get_sas_plan()
    story_example=get_story_example()

    prompt = f"""You are an interactive storyteller.
        Given these PDDL files and this lore, create a JSON representation of the story as a finite state machine (FSM).
        
        Write json in <JSON> </JSON>

        Lore: {json.dumps(lore, indent=2)}

        DOMAIN.PDDL:
        {domain}

        PROBLEM.PDDL:
        {problem}

        SAS_PLAN
        {plan}

        Generate a story.json with the following structure and nothing else. Use the example structure as a reference, but make it more original and dynamic:
        
        Example story:
        {story_example}
        
        Return yor response like plain text in ASCII character inside 
        
        """
    return prompt


def generate_story():

    prompt=generate_prompt_for_story()
    response=api_generate_GEMINI(prompt)
    logging.info(response)
    return response
