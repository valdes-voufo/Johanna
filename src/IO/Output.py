# transform text  to audio
# options
# choose the language
# choose the voice
# speak

import pyttsx3


class Output:
    def __init__(self):
        self.speaker = pyttsx3.init()
        self.setup_voice(3)

    def setup_voice(self, number=3):
        self.speaker.setProperty('rate', 150)
        voices = self.speaker.getProperty('voices')
        self.speaker.setProperty('voice', voices[3].id)

    def speak(self, text):
        print(text)
        self.speaker.say(text)
        self.speaker.runAndWait()
