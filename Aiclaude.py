from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


CLAUDE_API_KEY = os.getenv('C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')
CLAUDE_API_URL = 'https://api.claude.ai/v1/chat'

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    # Make a request to the Claude API
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
   app.run(debug=True, port=5001)

