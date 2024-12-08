from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Configure API
genai.configure(api_key="AIzaSyBKcY3eOLnn_07Uc-hhiwwwzzfCI8yls4s")
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize messages
messages = [
    {"role": "system", "content": "You are بصير (Baseer), an Arabic-speaking AI assistant specifically designed to help blind people."},
    {"role": "assistant", "content": "مرحباً! أنا بصير، مساعدك الشخصي. كيف يمكنني مساعدتك اليوم؟"}
]

@app.route('/')
def welcome():
    return "Welcome To Basser API"

# Chat route
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        prompt = data.get('message')
        
        if not prompt:
            prompt = "No message provided"
            return jsonify({'error': 'No message provided'}), 400

        messages.append({"role": "user", "content": prompt})

        system_prompt = """You are بصير (Baseer), an Arabic-speaking AI assistant specifically designed to help blind people. 
        Your responses should be in Arabic and focused on providing helpful, clear, and detailed assistance for visually impaired individuals. 
        Be extra descriptive when explaining visual concepts and always prioritize accessibility in your suggestions."""
        
        full_prompt = f"{system_prompt}\n\nUser: {prompt}"
        response = model.generate_content(full_prompt)
        
        # Extract just the text content
        assistant_response = response.text.strip()
        messages.append({"role": "assistant", "content": assistant_response})
        
        return jsonify({
            'response': assistant_response,
            'messages': messages
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get chat history
@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)