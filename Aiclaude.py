from flask import Flask, request, jsonify, render_template
import requests
import os
from flask_cors import CORS

# Specify 'templates' as the folder for HTML templates
app = Flask(__name__, static_folder='.', static_url_path='', template_folder='templates')
CORS(app)

CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
CLAUDE_API_URL = 'https://api.claude.ai/v1/chat'

# Serve the HTML file for the chatbot interface
@app.route('/')
def index():
    return render_template('Aichat.html')  # Case-sensitive, ensure it matches your file name

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
