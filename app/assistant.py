import time
import pyttsx3
import speech_recognition as sr

class VoiceAssistant:
    def __init__(self, speech, gpt3_api):
        self.speech = speech
        self.gpt3_api = gpt3_api
        self.INTERRUPTED = False
        self.ACTIVATION_KEYWORDS = ["hey ai", "hey assistant", "hey jarvis", "hey sakura", "Hey Snehal", "Hey Baby", "what's up", "what's good"]

    def handle_stop_keyword(self):
        self.INTERRUPTED = True
        time.sleep(2)
        self.INTERRUPTED = False
        self.speech.text_to_speech("Speech stopped. How can I assist you?")

    def continuously_listen(self):
        r = sr.Recognizer()
        while True:
            with sr.Microphone() as source:
                try:
                    audio = r.listen(source, timeout=5)
                    if audio is not None:
                        text = r.recognize_google(audio).lower()
                        if any(keyword in text for keyword in self.ACTIVATION_KEYWORDS):
                            self.speech.text_to_speech("Yeah, tell me.")
                            self.listen_and_respond()
                        elif "hey stop" in text or "stop" in text:
                            self.handle_stop_keyword()
                except (sr.WaitTimeoutError, sr.UnknownValueError):
                    pass  # No speech detected or unable to recognize speech
                except sr.RequestError:
                    print("Could not request results. Check your network connection.")
                except Exception as e:
                    print(f"An error occurred: {e}")
                time.sleep(1)

    def listen_and_respond(self):
        query = self.listen_to_user()
        print(f"You said: {query}")
        response = self.gpt3_api.chat_with_gpt(query)
        print(f"Response from GPT-3: {response}")
        self.speech.text_to_speech(response)

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
