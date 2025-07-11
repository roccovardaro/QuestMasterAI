import json
import logging
from src.utils.constant import get_lore, get_problem_valid_example, get_domain_valid_example, get_lore_example, \
    get_domain, get_problem
from src.utils.utils import api_generate_GEMINI, extract_and_save_pddl, extract_and_save_lore

# Codice ANSI per il verde
GREEN = "\033[92m"
RESET = "\033[0m"
# Configurazione logging con formato colorato
logging.basicConfig(
    level=logging.INFO,
    format=GREEN + '%(levelname)s: %(message)s' + RESET
)


def generate_lore_prompt(story_prompt: str):
    return f""" You are a JSON expert and worldbuilding specialist. Given a short fantasy story as input <STORY>{story_prompt} </STORY> , your task is to generate a lore.json content that follows exactly the same structure as in the example below. 
    You must not change or invent a different structure — just fill it using the information from the story.
    The output must be strictly valid JSON and must be wrapped inside <LORE> and </LORE> tags.
    If any field is missing in the story, use logical assumptions based on the narrative, but never remove or change any keys.
    Example Lore: 
    {json.dumps((get_lore_example()))}
    Return yor response like plain text in ASCII character inside 
    """


def generate_lore(story_prompt: str):

    prompt=generate_lore_prompt(story_prompt)
    logging.info(f"Generazione lore")
    response=api_generate_GEMINI(prompt)
    logging.info(response)
    return response

def generate_prompt(lore):
    return f"""
          You are a PDDL modeler. Given the following quest description, generate:
          1. A DOMAIN.PDDL file with predicates and actions, each with comments.
          2. A PROBLEM.PDDL file with an initial state and goal consistent with the domain.

          Lore:
          {json.dumps(lore, indent=2)}

          Return yor response like plain text in ASCII character inside 
          <DOMAIN_PDDL> 

          </DOMAIN_PDDL> 
          blocks for the domain, 
          and 
          <PROBLEM_PDDL>  

          </PROBLEM_PDDL> for the problem.
          
          In your response pay attention to the pddl syntax. Each pddl block is encapsulated in ( and ). Example (define (guard-awake ?location) A guard is awake at the specified location)
          Here an example of valid domain:
        {get_domain_valid_example()}
        Here an example of valid problem:
        {get_problem_valid_example()}
          """

def generate_prompt_with_error(lore, error:str):
    return f"""
              You are a PDDL modeler. Given the following quest description, generate:
              1. A DOMAIN.PDDL file with predicates and actions, each with comments.
              2. A PROBLEM.PDDL file with an initial state and goal consistent with the domain.

              Lore:
              {json.dumps(lore, indent=2)}

              Return yor response like plain text in ASCII character inside 
              <DOMAIN_PDDL> 

              </DOMAIN_PDDL> 
              blocks for the domain, 
              and 
              <PROBLEM_PDDL>  

              </PROBLEM_PDDL> for the problem.
              In your response pay attention to the pddl syntax. Each pddl block is encapsulated in ( and ). Example (define (guard-awake ?location) A guard is awake at the specified location
              The PDDL files generated previously contain an error during validation. Please check and correct the syntax and semantics of the file, ensuring it complies with the PDDL standard.
              Given the following PDDL files:
              Domain 
              {get_domain()}
              Problem
              {get_problem()}
              "The PDDL files generated previously contain an error during validation.
              Error:
              {error}
               Please check and correct the syntax and semantics of the file, ensuring it complies with the PDDL standard.
              )"""


def generate_pddl(error=False, error_str=""):

    lore=get_lore()
    logging.info("Generating PDDL...")
    if(not error):
        prompt=generate_prompt(lore)
    else:
        prompt=generate_prompt_with_error(lore,error_str)

    response=api_generate_GEMINI(prompt)

    logging.info("Generazione PDDL completata.")

    return response



story="""Elia era una ragazza semplice, figlia di contadini, che amava raccontare storie agli animali del bosco.
       Quando una siccità colpì il villaggio, si disse che la Fonte Magica nel cuore della foresta si era spenta. Nessuno osava cercarla, ma Elia partì con una lanterna e la sua voce.
       Nel silenzio del bosco, seguì un cervo dorato fino alla sorgente. L’acqua era ferma. Elia raccontò una storia di speranza, proprio come faceva sotto il salice.
       La Fonte si risvegliò. Tornò la pioggia. Nessuno seppe davvero cosa accadde, ma da quel giorno, al villaggio si ascoltavano le storie di Elia con occhi nuovi."""


