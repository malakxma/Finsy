from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
CLAUDE_API_URL = 'https://api.claude.ai/v1/chat'

@app.route('/')
def index():
    return "Welcome to the Chatbot API. Use the /chatbot endpoint to interact with the chatbot."

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    headers = {'Authorization': f'Bearer {CLAUDE_API_KEY}', 'Content-Type': 'application/json'}
    data = {
        'input': user_input,
        'model': 'claude-v1',
        'stream': False
    }

    response = requests.post(CLAUDE_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return jsonify({'response': response.json()}), 200
    else:
        return jsonify({'error': 'Error connecting to Claude API'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
