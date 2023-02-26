import time

from gtts import gTTS
import string
import random


async def convert(text="Hello! Example of text") -> str | None:
    if len(text) == 0:
        return None
    while True:
        try:
            random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=40))
            random_name += f"-{time.time()}"
            with open(f"../static/text/{random_name}.mp3", "w") as f:
                f.write(text)
            break
        except:
            pass
    text = text.replace("\n", "")
    audio = gTTS(text=text, lang="ru", slow=False)
    audio.save(f"../static/audio/{random_name}.mp3")

    #os.remove(f"../static/{random_name}.mp3")
    return f"../static/audio/{random_name}.mp3"
