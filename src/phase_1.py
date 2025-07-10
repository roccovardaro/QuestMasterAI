from src.agent.pddl_generator_agent import generate_lore, generate_pddl
from src.utils.utils import extract_and_save_lore, extract_and_save_pddl


def do_phase_1(story:str):

    #1- METODO CHE DALLA STORIA GENERA LA LORE E SALVA LA LORE

    lore_input= generate_lore(story)
    extract_and_save_lore(lore_input)

    #2 - GENERIAMO I FILE PDDL DALLA LORE E CREA I FILE DOMAIN E  PROBLEM
    response = generate_pddl()
    extract_and_save_pddl(response)
    #3. VALIDAZIONE DOMAIN E PROBLEM E GENERAZIONE STORY.JSON
