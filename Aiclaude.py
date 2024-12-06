from flask import Flask, request, jsonify, render_template
import requests
import os
from flask_cors import CORS 
import anthropic

# Specify 'templates' as the folder for HTML templates
app = Flask(__name__, static_folder='.', static_url_path='', template_folder='templates')
CORS(app)

client = anthropic.Anthropic(api_key="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")

# Serve the HTML file for the chatbot interface
@app.route('/')
def index():
    return render_template('Aichat.html')  # Case-sensitive, ensure it matches your file name

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        # Log the full response to see its structure
        print(f"Full API response: {response}")

        assistant_response = response.content[0].text
        return jsonify({'response': assistant_response}), 200
    
    except Exception as e:
        print(f"Error in chatbot route: {e}")
        return jsonify({'error': f"Internal server error: {str(e)}"}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False)

