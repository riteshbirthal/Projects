from gtts import gTTS
import playsound
import pyttsx3

tld_text = ['com.au', 'co.uk', 'com', 'ca', 'co.in', 'ie', 'co.za', 'ca', 'fr', 'com', 'com', 'com.br', 'pt', 'com.mx', 'es', 'com']
tld_text0 = ['en', 'en', 'en', 'en', 'en', 'en', 'en', 'fr', 'fr', 'zh-CN', 'zh-TW', 'pt', 'pt', 'es', 'es', 'es']

def speak(text, tld:str, lan:str):
  tts = gTTS(text=text, lang=f"{lan}", tld=f"{tld}")
  filename = "audio.mp3"
  tts.save(filename)
  playsound.playsound(filename)

def speak_with_voice(voice_id:int, text:str, rate:int):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[voice_id].id)
  engine.setProperty('rate', rate)
  engine.say(text)
  engine.runAndWait()