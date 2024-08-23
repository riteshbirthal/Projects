from esp8266 import light_on, lights_off, devil_on
from utils import *
import random
from constants import *
import threading

NAME='Jarvis'
hello_text = ['hello', f'hello {NAME.lower()}', 'hello buddy']
restart_text = ["restart", f"restart {NAME.lower()}", "restart system", f"restart system {NAME.lower()}", f"{NAME.lower()} restart system", f"{NAME.lower()} restart", "reboot", f"reboot {NAME.lower()}", "reboot system", f"reboot system {NAME.lower()}", f"{NAME.lower()} reboot system",f"{NAME.lower()} reboot"]
shutdown_text = ["shutdown", f"shutdown {NAME.lower()}", "shutdown system", f"shutdown system {NAME.lower()}", f"{NAME.lower()} shutdown system", f"{NAME.lower()} shutdown"]


def main():
  welcome(NAME)
  count = 0
  while True:
    battery(NAME)
    text = audio_input()
    if(text == "1"):
      count += 1
    else:
      count = 0
    if count > 80:
      return
    try:
      print(f'You said: {text}')
      text = text.lower()
      if text in about_text:
        speak_for(NAME, random.choice(["I am fine. How about you?","I am good. How are you?"]))
      elif text in hello_text:
        speak_for(NAME, random.choice(['Hello Sir','Yes Sir']))
      elif "who are you" == text:
        speak_for(NAME, f"Hello Sir, I am {NAME}.")
      elif text in love_text:
        speak_for(NAME, random.choice(["I love you too",'love you too']))
      elif text in light_on_text:
        #speak_for(NAME, random.choice(light_on_reply))
        #light_on()
        light_on_sp = threading.Thread(target=speak_for, args=(NAME,random.choice(light_on_reply)))
        light_on_t = threading.Thread(target=light_on)
        light_on_sp.start()
        light_on_t.start()
      elif text in light_off_text:
        # speak_for(NAME, random.choice(lights_off_reply))
        # lights_off()
        light_off_sp = threading.Thread(target=speak_for, args=(NAME,random.choice(lights_off_reply)))
        light_off_t = threading.Thread(target=lights_off)
        light_off_sp.start()
        light_off_t.start()
      elif text in devil_light_text:
        # speak_for(NAME, random.choice(devil_light_reply))
        # devil_on()
        devil_light_on_sp = threading.Thread(target=speak_for, args=(NAME,random.choice(devil_light_reply)))
        devil_light_on_t = threading.Thread(target=devil_on)
        devil_light_on_sp.start()
        devil_light_on_t.start()
      elif ("open new terminal" == text) or ("new terminal" == text):
        pyautogui.hotkey('windows','t')
      elif text in screenshot_text:
        speak_for(NAME, "screenshot taken.")
        screenshot()
      elif ("open camera" == text.lower()) or ("take a photo" == text.lower()):
        speak_for(NAME, "opening Camera")
        Camera(NAME)
      elif (f"{NAME} play music" == text) or ("play music" == text):
        speak_for(NAME, "playing music")
        music()
      elif "open youtube" == text:
        speak_for(NAME, "opening youtube")
        youtube()
      elif (f"{NAME} play movie" == text) or ("play movie" == text):
        speak("At this moment only those movies are available which are on YouTube.")
        youtube()
      elif text in shutdown_text:
        speak_for(NAME, "Your system is going to shutdown.")
        lights_off()
        shutdown()
      elif text in restart_text:
        speak_for(NAME, "System restarting.")
        restart()
      elif text in exit_text:
        return
    except KeyboardInterrupt:
      return
    except Exception as e:
      print('Exception Occured:', e)
      if text != "1":
        print('you said ' + text)
