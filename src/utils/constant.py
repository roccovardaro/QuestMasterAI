import logging
from pathlib import Path

GREEN = "\033[92m"
RESET = "\033[0m"
logging.basicConfig(
    level=logging.INFO,
    format=GREEN + '%(levelname)s: %(message)s' + RESET
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
LORE_PATH= Path(f"{BASE_DIR}/data/lore/lore.json")
LORE_EXAMPLE_PATH = Path(f"{BASE_DIR}/data/lore/lore_example.json")
DOMAIN_PATH= Path(f"{BASE_DIR}/data/pddl/domain.pddl")
PROBLEM_PATH= Path(f"{BASE_DIR}/data/pddl/problem.pddl")
DOMAIN_VALID_EXAMPLE_PATH= Path(f"{BASE_DIR}/data/pddl/domain_valid_example.pddl")
PROBLEM_VALID_EXAMPLE_PATH= Path(f"{BASE_DIR}/data/pddl/problem_valid_example.pddl")
DOWNWARD_PATH= Path(f"{BASE_DIR}/downward/fast-downward.py")


def get_lore():
    if LORE_PATH.exists():
        return  LORE_PATH.read_text()
    else:
        raise FileNotFoundError(f"file Lore non trovato in {LORE_PATH}")

def get_lore_example():
    if LORE_EXAMPLE_PATH.exists():
        return LORE_EXAMPLE_PATH.read_text()
    else:
        raise FileNotFoundError(f"file Lore Example non trovato in {LORE_EXAMPLE_PATH}")

#TODO
def save_lore(lore):
    pass

def get_domain():
    if DOMAIN_PATH.exists():
        return DOMAIN_PATH.read_text()
    else:
        raise FileNotFoundError(f"file Domain non trovato in {DOMAIN_PATH}")

def get_problem():
    if PROBLEM_PATH.exists():
        return PROBLEM_PATH.read_text()
    else:
        raise FileNotFoundError(f"file Problem non trovato in {PROBLEM_PATH}")

def get_domain_valid_example():
    if DOMAIN_VALID_EXAMPLE_PATH.exists():
        return DOMAIN_VALID_EXAMPLE_PATH.read_text()
    else:
        FileNotFoundError(f"file Domain Example non trovato in {DOMAIN_VALID_EXAMPLE_PATH}")

def get_problem_valid_example():
    if PROBLEM_VALID_EXAMPLE_PATH.exists():
        return PROBLEM_VALID_EXAMPLE_PATH.read_text()
    else:
        FileNotFoundError(f"file Problem Example non trovato in {PROBLEM_VALID_EXAMPLE_PATH}")

def save_problem(problem: str) -> None:
    PROBLEM_PATH.write_text(problem)
    logging.info(f"Problem salvato in {PROBLEM_PATH}")


def save_domain(domain: str) -> None:
    DOMAIN_PATH.write_text(domain)
    logging.info(f"Domain salvato in {DOMAIN_PATH}")

