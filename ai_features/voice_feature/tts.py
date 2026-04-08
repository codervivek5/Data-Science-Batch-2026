import pyttsx3
import asyncio

from sqlalchemy.util import await_only


def voice(message):
    engine = pyttsx3.init()
    voice_type = 4

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[voice_type].id)
    result = engine.say(message)

    engine.runAndWait()

    return result

if __name__ == "__main__":
    voice("Agar tu apne bot se stickers bhejna chahta hai ya khud ka sticker pack banana hai, bol — step-by-step setup bata dunga")
    # voice(responce)