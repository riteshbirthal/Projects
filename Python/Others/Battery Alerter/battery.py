import psutil
from gtts import gTTS
import pyttsx3
import playsound

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "audio.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def speak1(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[24].id)
    engine.setProperty('rate',160)
    engine.say(text)
    engine.runAndWait()

def battery():
    var = 1
    while var:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        #print("%d",int(percent[2]) - int('0'))
        percent = round(float(percent),2)
        percent2 = str(percent)
        plugged = "Plugged In" if plugged else "Unplugged"
        if (percent < 30) and (plugged == "Unplugged"):
            speak("Battery is low. Only "+ percent2 +"percent battery remains. Please Plug In.")
        elif ((percent == 100.0 or percent == 100 or percent == 100.00) and plugged == "Plugged In"):
            speak("Battery is Fully charged. Please unplug your charger.")
        else:
            var = 0

battery()