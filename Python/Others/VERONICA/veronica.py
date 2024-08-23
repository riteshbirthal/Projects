from esp8266 import *
from utils import *
import random
from constants import *
from lectures import *
import threading
from mail import *
from mail_data import *

NAME = 'Veronica'
VERSION = '2.0.1'

restart_text = ["restart", f"restart {NAME.lower()}", "restart system", f"restart system {NAME.lower()}", f"{NAME.lower()} restart system", f"{NAME.lower()} restart", "reboot", f"reboot {NAME.lower()}", "reboot system", f"reboot system {NAME.lower()}", f"{NAME.lower()} reboot system",f"{NAME.lower()} reboot"]
shutdown_text = ["shutdown", f"shutdown {NAME.lower()}", "shutdown system", f"shutdown system {NAME.lower()}", f"{NAME.lower()} shutdown system", f"{NAME.lower()} shutdown"]
terminal_text = ["open new terminal", "new terminal", f"{NAME.lower()} open new terminal","open terminal", f"{NAME.lower()} open terminal"]

def main():
  if return_td_val("date")!= datetime.now().date().isoformat():
    update_today()
  if return_td_val("welcome"):
    thread_fun(welcome, NAME, None, {NAME}, 2)
    update_td_val("welcome", 0)
  else:
    thread_fun("None", NAME, "Welcome Back Sir", None, 1)
  count = 0
  var = 0
  while True:
    h = int(datetime.now().hour)
    if return_td_val("date")!= datetime.now().date().isoformat():
      update_today()
    #for battery
    if var%50==0:
      battery(NAME)
      #thread_fun(battery, NAME, None, {NAME}, 2)
    if var>999:
      var = 0
    else:
      var = var + 1
    #audio input and checking
    text = audio_input()
    #count defines how many times(successive) no input is given or taken
    if count > 500:
      return
    try:
      print(f'You said: {text}')
      text = text.lower()
      if text !="1":
        count = 0
      if text == "1":
        count += 1
      elif text in about_text:
        speak_for(NAME, random.choice(about_text_reply))
      elif text in hello_text:
        speak_for(NAME, random.choice(hello_reply_text))
      elif text in intro_text:
        speak_for(NAME, f"Hello Sir, I am {NAME}.")
      elif text in love_text:
        speak_for(NAME, random.choice(love_text_reply))
      elif text in light_on_text:
        thread_fun(light_on, NAME, random.choice(light_on_reply), None, 0)
      elif text in light_off_text:
        thread_fun(lights_off, NAME, random.choice(lights_off_reply), None, 0)
      elif text in devil_light_text:
        thread_fun(devil_on, NAME, random.choice(devil_light_reply), None, 0)
      elif text in terminal_text:
        pyautogui.hotkey('windows','t')
      elif text in screenshot_text:
        thread_fun(screenshot, NAME, "Screenshot taken", None, 1)
      elif ("open camera" == text.lower()) or (f"{NAME.lower()} open camera" == text.lower()):
        speak_for(NAME, "opening Camera")
        Camera(NAME)
      elif (f"{NAME.lower()} play music" == text) or ("play music" == text):
        thread_fun(music, NAME, "playing music", None, 1)
      elif "open youtube" == text:
        speak_for(NAME, "opening youtube")
        youtube(NAME)
      elif (f"{NAME.lower()} play movie" == text) or ("play movie" == text):
        speak_for(NAME, "At this moment only those movies are available which are on YouTube.")
        youtube(NAME)
      elif text in thank_text:
        thread_fun("None", NAME, random.choice(thank_reply_text), None, 1)
      elif text in shutdown_text:
        speak_for(NAME, "Your system is going to shutdown.")
        if charger()=="Plugged In":
          speak_for(NAME,"Please remove charger before going to sleep.")
        shutdown()
      elif text in restart_text:
        speak_for(NAME, "System restarting.")
        restart()
      elif text in stat_mech_text:
        stat_mech()
      elif text in qm2_text:
        quant_mech_2()
      elif text in mm2_text:
        math_method_2()
      elif text in lect_text:
        lecture(NAME)
      elif text in exit_text:
        return
      elif text in current_time_text:
        thread_fun(current_time, NAME, None, {NAME}, 2)
      elif text in mail_sending_text:
        mail_sending(NAME)
      elif text in test_mail_text:
        test_mail(NAME)
      elif text in sleep_text:
        thread_fun(lights_off, NAME, "Okay Sir", None, 0)
        time.sleep(1)
        if charger()=="Plugged In":
          speak_for(NAME,"Please remove charger before going to sleep.")
        if (h>=20) or (h<5):
          shutdown()
        else:
          return
    except KeyboardInterrupt:
      return
    except Exception as e:
      print('Exception Occured:', e)
      if text != "1":
        print('you said ' + text)
        count = 0
