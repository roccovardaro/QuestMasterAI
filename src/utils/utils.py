import logging
import os
from pathlib import Path
from dotenv import load_dotenv
from src.utils.constant import save_domain, save_problem, save_lore
import google.generativeai as genai

load_dotenv()
def extract_and_save_pddl(response: str) -> None:
    logging.info("Extracting domain and problem PDDL blocks from response...")

    try:
        domain_block = response.split("<DOMAIN_PDDL>")[1].split("</DOMAIN_PDDL>")[0].strip()
        problem_block = response.split("<PROBLEM_PDDL>")[1].split("</PROBLEM_PDDL>")[0].strip()
        save_domain(domain_block)
        save_problem(problem_block)
    except Exception:
        logging.error("Failed to extract PDDL blocks from response.")
        return

    logging.info("✅ domain.pddl and problem.pddl generated.")


def extract_and_save_lore(response: str) -> None:
    logging.info("Extracting Lore from response...")

    try:
        lore_block = response.split("<LORE>")[1].split("</LORE>")[0].strip()
        save_lore(lore_block)

    except Exception:
        logging.error("Failed to extract Lore from response.")
        return

    logging.info("✅ lore.json generated.")


def api_generate_GEMINI(prompt:str):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel(os.getenv("GOOGLE_MODEL_NAME"))
    response = model.generate_content(prompt)
    return response.text


def to_wsl_path(path: Path) -> str:
    """Converte un Path di Windows in path WSL"""

    path = path.resolve()
    return "/mnt/" + path.drive[0].lower() + path.as_posix()[2:]