import os
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_community.llms import Ollama

import logging

# Configurazione logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

def api_generate_GEMINI(prompt:str):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel(os.getenv("GOOGLE_MODEL_NAME"))
    response = model.generate_content(prompt)
    return response.text

def api_generate_OLLAMA(prompt:str):
    model = os.getenv("OLLAMA_MODEL")
    return invoke_ollama_llm(prompt, model)

def invoke_ollama_llm(prompt: str,
               model_name: str,
               base_url: str = "http://localhost:11434",
               temperature: float = 0.7,
               **kwargs) -> str:
    """
    Invoca un modello LLM locale tramite Ollama usando LangChain.

    Args:
        prompt: Stringa di prompt da inviare al modello
        model_name: Nome del modello da utilizzare (es. "llama2", "mistral", "codellama")
        base_url: URL base del server Ollama
        temperature: Temperatura per la generazione (0.0 - 1.0)
        **kwargs: Parametri aggiuntivi per Ollama (top_k, top_p, num_predict, etc.)

    Returns:
        str: Risposta generata dal modello

    Raises:
        ValueError: Se il prompt non è valido
        Exception: Se si verifica un errore durante l'invocazione
    """

    # Validazione input
    if not prompt or not isinstance(prompt, str):
        raise ValueError("Il prompt deve essere una stringa non vuota")

    if not 0.0 <= temperature <= 1.0:
        raise ValueError("La temperatura deve essere tra 0.0 e 1.0")

    try:
        logger.info(f"Inizializzazione modello {model_name} su {base_url}")

        # Inizializza il modello Ollama
        llm = Ollama(
            model=model_name,
            base_url=base_url,
            temperature=temperature,
            **kwargs
        )

        logger.info(f"Invocazione del modello con prompt di {len(prompt)} caratteri")

        # Invoca il modello
        response = llm.invoke(prompt)

        logger.info("Risposta ricevuta con successo")

        # Restituisce la risposta pulita
        logging.info(response)
        return response

    except Exception as e:
        logger.error(f"Errore durante l'invocazione del modello: {e}")
        raise Exception(f"Errore nella generazione: {str(e)}")


