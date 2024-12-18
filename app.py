from flask import Flask, request, jsonify, render_template
from chatbot_logic import get_llama_response
from evaluation import evaluate_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    language = request.json.get('language', 'en')  # Default language is English
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400

    # Get the response from Llama 3
    bot_response = get_llama_response(user_message, language)

    # Evaluate the response using BLEU and ROUGE
    metrics = evaluate_response(user_message, bot_response)

    return jsonify({
        'response': bot_response,
        'metrics': metrics
    })

if __name__ == '__main__':
    app.run(debug=True)
