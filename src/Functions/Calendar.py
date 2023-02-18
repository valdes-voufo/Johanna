class Calendar:
    def __init__(self, input_, output_):
        self.language = None
        self.input_ = input_
        self.output_ = output_

    def addItems(self):
        self.language = "vv"  # to be deleted later
        self.output_.speak("quelle tache veux tu ajouter ?")
        note = self.input_.listen()
        note = note.lower()

        self.output_.speak("quel jour ?")
        day = self.input_.listen()
        day = day.lower()

        self.output_.speak("a quelle heure ?")
        time = self.input_.listen()
        time = time.lower()

        self.output_.speak("combien de temps ca dure ? ?")
        duration = self.input_.listen()
        duration = duration.lower()

        with open("Calendar.txt", 'w') as f:
            f.write(note + "__" + day + "__" + time + "__" + duration)
            self.output_.speak("la tache a ete ajouter a ton agenda")
