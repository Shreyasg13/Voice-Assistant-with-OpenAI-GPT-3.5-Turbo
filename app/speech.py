import pyttsx3
import re

class Speech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.INTERRUPTED = False

    def text_to_speech(self, text):
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate - 50)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

        sentences = re.split(r'(?<=[.!?])\s', text)
        for sentence in sentences:
            if self.INTERRUPTED:
                break
            self.engine.say(sentence)
            self.engine.runAndWait()
            
    def stop_speech(self):
        self.INTERRUPTED = True
