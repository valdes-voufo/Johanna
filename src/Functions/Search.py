import pywhatkit
import wikipedia

class Search:
    def __init__(self, input_, output_):
        self.language = None
        self.input_ = input_
        self.output_ = output_

    def search(self):
        self.language = "vv"  # to be deleted later
        self.output_.speak("que veut tu rechercher ?")
        person = self.input_.listen()
        person = person.lower()
        info = wikipedia.summary(person, 1)
       # wikipedia.set_lang("fr-FR")
        # text = wikipedia.search(person)
        print(info)
        self.output_.speak(info)
