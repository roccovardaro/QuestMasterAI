

import google.generativeai as genai
import os # Importa il modulo os per accedere alle variabili d'ambiente

from dotenv import load_dotenv

# 1. Configura la tua API key
# È VIVAMENTE CONSIGLIATO caricare la tua API key da una variabile d'ambiente
# per motivi di sicurezza e per evitare di esporla direttamente nel codice.
# Assicurati di aver impostato una variabile d'ambiente chiamata GEMINI_API_KEY
# con il valore della tua chiave API.

load_dotenv()
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except KeyError:
    print("Errore: La variabile d'ambiente 'GEMINI_API_KEY' non è impostata.")
    print("Per favore, imposta la variabile d'ambiente con la tua chiave API di Gemini.")
    exit() # Esce dal programma se la chiave non è impostata

# 2. Inizializza il modello (non è necessario creare un 'client' esplicito come nell'esempio precedente)
# Il modulo genai gestisce la comunicazione con l'API direttamente dopo la configurazione.
model = genai.GenerativeModel(os.getenv("GOOGLE_MODEL_NAME")) # Ho usato gemini-1.5-flash, che è più recente e performante.
                                                 # Puoi scegliere il modello che preferisci, ad es. "gemini-pro"

# 3. Effettua la richiesta di generazione di contenuto
prompt = "Spiega come funziona l'IA in poche parole"
response = model.generate_content(prompt)

# 4. Stampa il risultato
print(response.text)