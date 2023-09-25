import pyttsx3
import re
import time

class Speech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def text_to_speech(self, text):
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate - 50)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

        # Split text into sentences using regular expressions
        sentences = re.split(r'(?<=[.!?])\s', text)

        for sentence in sentences:
            if self.INTERRUPTED:
                break
            self.engine.say(sentence)
            self.engine.run
