import requests

LANGUAGE_PROMPTS = {
    'en': "Respond in English:",
    'es': "Responde en español:",
    'fr': "Répondez en français:",
    'am': "እባኮትን በአማርኛ መልስ ይስጡ:",  # Amharic
    'hi': "हिंदी में उत्तर दें:"
}

def get_llama_response(user_message, language='en'):
    """Send the user's message to Llama 3 via Ollama API and return the response."""
    try:
        url = "http://localhost:11400/chat"  # Ollama API endpoint
        prompt = LANGUAGE_PROMPTS.get(language, LANGUAGE_PROMPTS['en']) + f" {user_message}"

        payload = {
            "model": "llama-3",
            "message": prompt
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get('response', 'I am sorry, I could not understand.')
        else:
            return 'Error: Unable to fetch a response from the model.'
    except Exception as e:
        return f"Error: {str(e)}"

