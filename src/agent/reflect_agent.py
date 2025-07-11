import logging
import subprocess

from src.agent.pddl_generator_agent import generate_pddl
from src.utils.constant import DOWNWARD_PATH, DOMAIN_PATH, PROBLEM_PATH
from src.utils.utils import to_wsl_path, extract_and_save_pddl

# Codice ANSI per il verde
GREEN = "\033[92m"
RESET = "\033[0m"
# Configurazione logging con formato colorato
logging.basicConfig(
    level=logging.INFO,
    format=GREEN + '%(levelname)s: %(message)s' + RESET
)


def command_linux(domain_path,base_dir,problem_path):
    command = f"python3 {base_dir}/fast-downward/fast-downward.py {domain_path} {problem_path} --search \"lazy_greedy([ff()], preferred=[ff()])\""
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result

def command_windows(domain_path,downward_path,problem_path):

    command = f"python3 {to_wsl_path(downward_path)} {to_wsl_path(domain_path)} {to_wsl_path(problem_path)} --search \"lazy_greedy([ff()], preferred=[ff()])\""

    result = subprocess.run(
        [
            "wsl",
            "-d", "Ubuntu",
            "bash", "-c",
            command
        ],
        capture_output=True,
        text=True
    )
    return result

def validate_plan(domain_path, problem_path, system="Windows"):
    """
    :return: bool_result: True se la soluzione è stata trovata, False altrimenti.
            err_str= Errore se presente.
    """
    logging.info("Validating plan with Fast Downward...")

    downward_path=DOWNWARD_PATH
    if(system == "Windows"):
        result = command_windows(domain_path, downward_path, problem_path)
    elif (system == "Linux"):
        result = command_linux(domain_path,downward_path,problem_path)
    else:
        logging.info(f"{system} non è un sistema valido")
        raise ValueError(f"{system} non è un sistema valido")

    output = result.stdout + result.stderr
    logging.info(f"Fast Downward output:\n{result.stdout}\n{result.stderr}")

    bool_result="Solution found" in output or "Plan found" in output
    err_str= result.stderr
    return  bool_result, err_str


def validate_plan_main(k=3):
    i=0
    while(i<k):
        valid, err_str = validate_plan(DOMAIN_PATH,PROBLEM_PATH)
        if(valid):
            logging.info("PDDL Validato!")
            return True
        #PROMPT CON ERRORE
        logging.info(f"""PDDL generato contiene errore: {err_str}""")
        response= generate_pddl(True,err_str)
        extract_and_save_pddl(response)
        #GENERA E SALVA PDDL
        i+=1
    return False