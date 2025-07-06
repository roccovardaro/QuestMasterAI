import requests

try:
    r = requests.get("http://localhost:11434")
    if r.ok:
        print("✅ Ollama è attivo.")
    else:
        print("⚠️ Ollama ha risposto ma con errore:", r.status_code)
except requests.exceptions.ConnectionError:
    print("❌ Ollama NON è attivo.")