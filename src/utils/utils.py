import logging
import os

from src.utils.constant import save_domain, save_problem
import google.generativeai as genai


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



def api_generate_GEMINI(prompt:str):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel(os.getenv("GOOGLE_MODEL_NAME"))
    response = model.generate_content(prompt)
    return response.text