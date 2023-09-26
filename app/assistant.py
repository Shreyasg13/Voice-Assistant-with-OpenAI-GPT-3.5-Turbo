import time
import pyttsx3
import speech_recognition as sr
import logging  # 1. Import the necessary logging module

logging.basicConfig(level=logging.INFO, filename='voice_assistant.log', format='%(asctime)s [%(levelname)s] - %(message)s')
class VoiceAssistant:
    def __init__(self, speech, gpt3_api):
        self.speech = speech
        self.gpt3_api = gpt3_api
        self.ACTIVATION_KEYWORDS = ["Hey GooRoo","hey ai", "hey assistant", "hey jarvis", "hey computer","what's up","what's good","bazinga","Hey Sakura"]


    def continuously_listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Assistant started and is listening...")  # Debug line
            while True:
                try:
                    print("Ready to capture audio...")  # Debug line
                    audio = r.listen(source, timeout=5)
                    if audio is not None:
                        text = r.recognize_google(audio).lower()
                        logging.info(f"Input Speech: {text}")
                        print(f"Input Speech: {text}")  # Debug line
                        if any(keyword in text for keyword in self.ACTIVATION_KEYWORDS):
                            self.speech.text_to_speech("Yeah, How can I assist you?.")
                            self.listen_and_respond()
                        elif "hey stop" in text or "stop" in text:
                            self.handle_stop_keyword()
                except (sr.WaitTimeoutError, sr.UnknownValueError):
                    print("No speech detected or unable to recognize speech.")  # Debug line
                except sr.RequestError:
                    logging.error("Could not request results. Check your network connection.")
                    print("Could not request results. Check your network connection.")  # Debug line
                except Exception as e:
                    logging.error(f"An error occurred: {e}")
                    print(f"An error occurred: {e}")  # Debug line
                time.sleep(1)


    def listen_and_respond(self):
        self.speech.INTERRUPTED = False
        query = self.listen_to_user()
        logging.info(f"User's query: {query}")
        
        response = self.gpt3_api.chat_with_gpt(query)
        logging.info(f"Response from GPT-3: {response}")
        
        self.speech.text_to_speech(response)


    def handle_stop_keyword(self):
        self.speech.stop_speech()
        time.sleep(2)
        self.speech.INTERRUPTED = False
        self.speech.text_to_speech("Speech stopped. How can I assist you?")




    def listen_to_user(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return "Could not understand audio"
            except sr.RequestError:
                return "API unavailable"

    def process_command(self, command):
        if "stop" in command:
            self.handle_stop_keyword()
        else:
            return self.gpt3_api.chat_with_gpt(command)
