import pywhatkit


class Music:
    def __init__(self, input_, output_):
        self.language = None
        self.input_ = input_
        self.output_ = output_

    def play(self):
        self.language = "vv"  # to be deleted later
        self.output_.speak("quelle Music veux tu  ecouter?")
        music = self.input_.listen()
        music = music.lower()
        pywhatkit.playonyt(music)
