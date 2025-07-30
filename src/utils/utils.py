import logging

from pathlib import Path
from src.utils.constant import save_domain, save_problem, save_lore, save_story
from src.utils.llm import api_generate_GEMINI, api_generate_OLLAMA

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


def extract_and_save_story(response: str) -> None:
    logging.info("Extracting Story from response...")

    try:
        story_block = response.split("<JSON>")[1].split("</JSON>")[0].strip()
        save_story(story_block)

    except Exception:
        logging.error("Failed to extract Story from response.")
        return

    logging.info("✅ story.json generated.")

def call_API_LLM(prompt:str, useGeminiAPI = True):
    if useGeminiAPI:
        return api_generate_GEMINI(prompt)
    else:
        return api_generate_OLLAMA(prompt)

def to_wsl_path(path: Path) -> str:
    """Converte un Path di Windows in path WSL"""
    path = path.resolve()
    return "/mnt/" + path.drive[0].lower() + path.as_posix()[2:]

def extract_html_title_and_story(response: str):
    try:
        title_block = response.split("<TITLE>")[1].split("</TITLE>")[0].strip()
        story_block = response.split("<STORY>")[1].split("</STORY>")[0].strip()
        return title_block, story_block
    except Exception:
        logging.error("Failed to extract Story or Title from response.")
        return

