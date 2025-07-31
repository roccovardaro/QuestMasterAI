import logging

from src.agent.pddl_generator_agent import generate_lore, generate_pddl
from src.agent.reflect_agent import validate_plan
from src.agent.story_agent import generate_story
from src.utils.constant import DOMAIN_PATH, PROBLEM_PATH
from src.utils.utils import extract_and_save_lore, extract_and_save_pddl, extract_and_save_story

# Codice ANSI per il verde
GREEN = "\033[92m"
RESET = "\033[0m"
# Configurazione logging con formato colorato
logging.basicConfig(
    level=logging.INFO,
    format=GREEN + '%(levelname)s: %(message)s' + RESET
)

def do_phase_1(story:str):

    #1- METODO CHE DALLA STORIA GENERA LA LORE E SALVA LA LORE
    logging.info("Inizio phase 1")
    lore_input= generate_lore(story)
    extract_and_save_lore(lore_input)

    #2 - GENERIAMO I FILE PDDL DALLA LORE E CREA I FILE DOMAIN E  PROBLEM E SUCCESSIVAMENTE LI VALIDIAMO
    validation_trial=3
    i = 0
    isValid=False
    validation_error=""
    while (i < validation_trial):
        #2.1 GENERAZIONE PDDL
        logging.info(f"""Generation Number:{i}""")
        response = generate_pddl(validation_error)
        extract_and_save_pddl(response)
        #2.2 VALIDAZIONE
        logging.info(f"""Validation Number: {i}""")
        valid, err_str = validate_plan(DOMAIN_PATH, PROBLEM_PATH)
        if (valid):
            logging.info("PDDL Validato!")
            isValid = True
            break
        validation_error=err_str
        i += 1

    # 4. GENERAZIONE STORY.JSON
    if (isValid):
        logging.info("INIZIO GENERAZIONE STORY.JSON...")
        response_story=generate_story()
        extract_and_save_story(response_story)

    logging.info("Fine phase 1")
    return isValid

