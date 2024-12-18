
# Low-Resource Language Chatbot

This project implements a multilingual chatbot using **Llama 3** integrated with **Ollama**. It supports multiple languages and evaluates the chatbot's responses using BLEU and ROUGE metrics.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview
The **Low-Resource Language Chatbot** project aims to create a chatbot that supports multiple languages, including English, Spanish, French, Amharic, and Hindi. It uses **Llama 3** via **Ollama API** to generate responses and `transformers` library for BLEU and ROUGE score evaluations.

### Features:
- **Multilingual Support**: Select and interact with the chatbot in various languages.
- **Response Evaluation**: Uses BLEU and ROUGE metrics to evaluate the quality of chatbot responses.
- **User Interface**: A simple web interface using **Flask** to interact with the chatbot.

## Prerequisites
Before running the project, ensure you have the following installed:

- Python (version 3.8 or higher)
- `pip` package manager
- ngrok (to expose the local server publicly)

### Recommended Setup:
- **Python**: [Download Python](https://www.python.org/downloads/)
- **Pip**: Comes bundled with Python by default.
- **Ngrok**: [Download Ngrok](https://ngrok.com/download) for exposing local development servers.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/low-resource-chatbot.git
   cd low-resource-chatbot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask application:
   ```bash
   python app.py
   ```

4. Expose the local server using ngrok:
   ```bash
   ngrok http 5000
   ```
   Note: Replace `5000` with the port the Flask app is running on if it’s different.

5. Access the chatbot:
   - You can now open the chatbot at `http://127.0.0.1:5000` or the ngrok URL.

## Usage
1. **Start the Chatbot**:
   - Run the Flask application with `python app.py`.
   - Open `http://127.0.0.1:5000` in your web browser.

2. **Interact with the Chatbot**:
   - Type your message in the input field.
   - Select a language from the dropdown menu.
   - Click "Send" to get a response from the chatbot.
   - View BLEU and ROUGE metrics on the chat UI.

3. **View Metrics**:
   - BLEU and ROUGE metrics are displayed along with the chatbot response. These metrics help evaluate the coherence and fluency of responses in different languages.

## Project Structure
```
low_resource_chatbot/
│
├── app.py                # Main Flask application
├── chatbot_logic.py      # Core chatbot logic
├── evaluation.py         # BLEU and ROUGE evaluation
├── requirements.txt      # Dependencies
├── templates/            # HTML templates
│   └── index.html        # Chatbot UI
└── static/               # CSS and static files
    └── styles.css        # Styling
```

## Dependencies
- `flask`: Web framework for Python.
- `requests`: HTTP requests library.
- `rouge-score`: ROUGE metric evaluation.
- `transformers`: Library for various NLP tasks including BLEU evaluation.
- `sentencepiece`: Sentence tokenization library.
- `torch`: PyTorch library for deep learning.
- `ngrok`: Expose your localhost to the internet for testing purposes.

### `requirements.txt`:
```plaintext
flask
requests
rouge-score
transformers
sentencepiece
torch
ngrok
```

## Contributing
Feel free to fork this repository and submit pull requests. All contributions are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
