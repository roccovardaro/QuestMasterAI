import logging

from src.agent.pddl_generator_agent import generate_lore, generate_pddl
from src.agent.reflect_agent import validate_plan_main
from src.agent.story_agent import generate_story
from src.utils.utils import extract_and_save_lore, extract_and_save_pddl, extract_and_save_story

# Codice ANSI per il verde
GREEN = "\033[92m"
RESET = "\033[0m"
# Configurazione logging con formato colorato
logging.basicConfig(
    level=logging.INFO,
    format=GREEN + '%(levelname)s: %(message)s' + RESET
)

story="""Elia era una ragazza semplice, figlia di contadini, che amava raccontare storie agli animali del bosco.
       Quando una siccità colpì il villaggio, si disse che la Fonte Magica nel cuore della foresta si era spenta. Nessuno osava cercarla, ma Elia partì con una lanterna e la sua voce.
       Nel silenzio del bosco, seguì un cervo dorato fino alla sorgente. L’acqua era ferma. Elia raccontò una storia di speranza, proprio come faceva sotto il salice.
       La Fonte si risvegliò. Tornò la pioggia. Nessuno seppe davvero cosa accadde, ma da quel giorno, al villaggio si ascoltavano le storie di Elia con occhi nuovi."""


def do_phase_1(story:str):

    logging.info("Inizio phase 1")
    #1- METODO CHE DALLA STORIA GENERA LA LORE E SALVA LA LORE
    lore_input= generate_lore(story)
    extract_and_save_lore(lore_input)

    #2 - GENERIAMO I FILE PDDL DALLA LORE E CREA I FILE DOMAIN E  PROBLEM
    response = generate_pddl()
    extract_and_save_pddl(response)
    #3. VALIDAZIONE DOMAIN E PROBLEM
    isValid=validate_plan_main()

    #4. GENERAZIONE STORY.JSON
    if(isValid):
        response_story=generate_story()
        extract_and_save_story(response_story)

    logging.info("Fine phase 1")
    return isValid

do_phase_1(story)