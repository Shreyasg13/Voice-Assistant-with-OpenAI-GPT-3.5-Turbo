from flask import Flask, request, jsonify
from app.speech import Speech
from app.gpt3_api import GPT3API
from app.assistant import VoiceAssistant

app = Flask(__name__)

# Create instances of your classes
speech = Speech()
gpt3_api = GPT3API()
assistant = VoiceAssistant(speech, gpt3_api)

@app.route('/')
def index():
    return "Voice assistant service is running!"

@app.route('/voice', methods=['POST'])
def voice_command():
    data = request.get_json()
    if 'command' in data:
        command = data['command']
        response = assistant.process_command(command)
        return jsonify({"response": response})
    else:
        return jsonify({"error": "Invalid request format"})
