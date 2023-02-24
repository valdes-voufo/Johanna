from src.Functions.Calendar import Calendar
from src.Functions.Music import Music
from src.Functions.Search import Search
from src.IO.Micro import Input
from src.IO.Output import Output
import speech_recognition as sr
from neuralintents import GenericAssistant

output_ = Output()
input_ = Input(output_)
calendar_ = Calendar(input_, output_)
musicPlayer_ = Music(input_, output_)
search_ = Search(input_, output_)


def greeting():
    output_.speak(" bonjour,patron , comment puis-je t'aider")


def quitF():
    output_.speak("au revoir a plus tard")


def merci():
    output_.speak("de rien Patron , je suis la pour te servir")


mapping = {"greeting": greeting,
           "create_note": calendar_.addItems,
           "exit": quitF,
           "merci": merci,
           "play_Music": musicPlayer_.play,
           "search": search_.search}
assistant = GenericAssistant('res/intents.json', intent_methods=mapping)
assistant.train_model()
# assistant.load_model()


output_.speak("bonjour patron")
while True:
    with sr.Microphone() as source:
        message = input_.listen()
        #   message.lower()
        assistant.request(message)
