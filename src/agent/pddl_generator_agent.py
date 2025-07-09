import json
import logging
from src.utils.constant import get_lore, get_problem_valid_example, get_domain_valid_example
from src.utils.utils import api_generate_GEMINI, extract_and_save_pddl


# Codice ANSI per il verde
GREEN = "\033[92m"
RESET = "\033[0m"
# Configurazione logging con formato colorato
logging.basicConfig(
    level=logging.INFO,
    format=GREEN + '%(levelname)s: %(message)s' + RESET
)



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

def generate_pddl(lore):

    logging.info("Generating PDDL...")
    prompt=generate_prompt(lore)

    response=api_generate_GEMINI(prompt)

    logging.info("GEMINILLM processo completato.")

    return response


lore= get_lore()
response = generate_pddl(lore)
extract_and_save_pddl(response)

