# get the audio from microphone and translate it in a text form
# options
# choose the language
# choose the recognizer
# return text as output
import speech_recognition as sr

from src.IO.Output import Output


class Micro:
    def __init__(self, output_):
        self.language = "fr-FR"
        self.listener = sr.Recognizer()
        self.output_ = output_

    def listen(self):

        with sr.Microphone() as source:
            self.listener.adjust_for_ambient_noise(source, 0.2)
            audio = self.listener.listen(source)
        try:
            text = self.listener.recognize_google(audio, language=self.language)
            print(text)
            return text
        except sr.UnknownValueError:
            self.listen()
        except sr.RequestError:
            self.listen()

    def set_language(self, language):
        self.language = language
