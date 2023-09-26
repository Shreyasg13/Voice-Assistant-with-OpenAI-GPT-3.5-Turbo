import sys
sys.path.append("..")
from app.assistant import VoiceAssistant
from app.speech import Speech
from app.gpt3_api import GPT3API

speech_instance = Speech()
gpt3_instance = GPT3API(config_file_path="../config.yaml")
assistant_instance = VoiceAssistant(speech_instance, gpt3_instance)

def test_stop_keyword():
    response = assistant_instance.process_command("stop")
    assert response == "Stopping the assistant."
