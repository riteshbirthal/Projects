from click import argument
from gtts import gTTS
import playsound
from psutil import sensors_battery
import pyttsx3
from datetime import datetime, timedelta
import speech_recognition as sr
import os
import psutil
import pyautogui
import time
import webbrowser
import threading
import subprocess
from esp8266 import *
import json
from mail import*
from mail_data import *
import random
from mail_data import battery_low

def system(command:str):
  os.system(command)

def restart():
  os.system("reboot")

def shutdown():
  os.system("shutdown 0")

def firefox(text):
  os.system(f"firefox --search {text}") 

def youtube(name:str):
  system("firefox youtube.com")
  time.sleep(5)
  speak_for(name, "Tell me, What do you want to search?")
  pyautogui.press('tab',presses=6)
  pyautogui.press('enter')
  time.sleep(10)
  pyautogui.press(['tab','enter'])
  time.sleep(10)

def screenshot():
  pyautogui.press('prtscr')

def music():
  webbrowser.open('Online Playlist Link like Youtube')

def speak(text):
  tts = gTTS(text=text, lang="en")
  filename = "audio.mp3"
  tts.save(filename)
  playsound.playsound(filename)

def speak_with_voice(voice_id:int, text:str):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice',voices[voice_id].id)
  engine.setProperty('rate',140)
  engine.say(text)
  engine.runAndWait()

def speak_for(name:str, text:str):
  if name == 'Jarvis':
    speak_with_voice(3, text)
  elif name == 'Veronica':
    speak(text)

def audio_input():
  try:
    r = sr.Recognizer()
    with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source,phrase_time_limit=2)
      text = r.recognize_google(audio)
      print('You said :', text)
      if type(text) == list:
        return text[0]
      return text if type(text) == str else "1"
  except KeyboardInterrupt:
    raise KeyboardInterrupt
  except:
    return "1"

def welcome(name:str):
  h = int(datetime.now().hour)
  if h>=4 and h < 12:
    speak_for(name, f"Good Morning Sir, I am {name}.")
  elif h>= 12 and h < 18:
    speak_for(name, f"Good Afternoon Sir, I am {name}.")
  elif h>=18 and  h<24:
    speak_for(name, f"Good Evening Sir, I am {name}.")
  else:
    speak_for(name, "Its time to Sleep. Do you want to work more Sir?")
    while True:
      text = "1"
      text = audio_input()
      if("no" == text.lower()) or ("nahi" == text.lower()):
        speak_for(name,"Okay. Good Night Sir.")
        if charger()=="Plugged In":
          speak_for(name,"Please remove charger before going to sleep.")
        lights_off()
        shutdown()
      elif("yes" == text.lower()) or ("exit" == text.lower()):
        speak_for(name, "Okay Sir.")
        return

def battery1(name:str):
  while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    percent = round(float(percent),2)
    percent2 = str(percent)
    plugged = "Plugged In" if plugged else "Unplugged"
    if (percent < 30) and (plugged == "Unplugged"):
      speak_for(name, "Battery is low. Only "+ percent2 +"percent battery remains. Please Plug In.")
    elif ((percent == 100.0 or percent == 100 or percent == 100.00) and plugged == "Plugged In"):
      speak_for(name, "Battery is Fully charged. Please unplug your charger.")
    else:
      return

def charger():
  battery = psutil.sensors_battery()
  plugged = battery.power_plugged
  plugged = "Plugged In" if plugged else "Unplugged"
  return plugged

def battery(name:str):
  battery = psutil.sensors_battery()
  plugged = battery.power_plugged
  percent = str(battery.percent)
  percent = round(float(percent),2)
  percent2 = str(percent)
  plugged = "Plugged In" if plugged else "Unplugged"
  if (percent < 10) and (plugged == "Unplugged"):
    speak_for(name, "Battery is very low. System is going to shutdown.")
    shutdown()
  elif (percent < 30) and (plugged == "Unplugged"):
    speak_for(name, "Battery is low. Only "+ percent2 +"percent battery remains. Please Plug In.")
    if return_td_val("battery_mail"):
      rec_id, sub, msg = battery_low()
      thread_fun(mail, name, None, {rec_id, sub, msg}, 2)
      update_td_val("battery_mail", 0)
  elif ((percent == 100.0 or percent == 100 or percent == 100.00) and plugged == "Plugged In"):
    speak_for(name, "Battery is Fully charged. Please unplug your charger.")
  if ((percent > 80) or (plugged=="Plugged In")) and return_td_val("battery_mail")==0:
    update_td_val("battery_mail", 1)

def Camera(name:str):
  process = subprocess.Popen("cheese")
  print(process.pid)
  time.sleep(2)
  speak_for(name, "If you want to take photo say PHOTO")
  while True:
    battery(name)
    command = audio_input()
    try:
      if ("close camera" == command.lower()) or ("exit" == command) or ("quit" == command) or ("close" == command):
        process.kill()
        return
      elif ("take a photo" == command.lower()) or ("photo" == command.lower()):
        pyautogui.press('space')
    except:
      continue

def thread_fun(fun, name:str, text:str, arg=None, speak_first=1):
  if speak_first==1 and text!=None:
    threading.Thread(target=speak_for, args=(name, text)).start()
  if arg==None and fun!="None":
    threading.Thread(target=fun).start()
  else:
    if fun!="None":
      threading.Thread(target=fun, args=arg).start()
  if speak_first==0 and text!=None:
    threading.Thread(target=speak_for, args=(name, text)).start()

def update_td_val(value_name :str, value):
  with open('var.json', 'r') as file:
    data = json.load(file)
    data["today"][value_name] = value

  with open('var.json', 'w') as file:
    json.dump(data, file, indent=2)

def return_td_val(value_name :str):
  with open('var.json', 'r') as file:
    data = json.load(file)
    return data["today"][value_name]

def update_today():
  with open('var.json', 'r') as file:
    data = json.load(file)
    data["today"] = data["tomorrow"].copy()
    data["tomorrow"]["date"] = (datetime.now()+timedelta(1)).date().isoformat()

  with open('var.json', 'w') as file:
    json.dump(data, file, indent=2)


def mail_sending(name:str):
    t = True
    count = 0
    while t:
        if count > 90:
            return
        speak_for(name, random.choice(mail_receiver_text))
        receiver = audio_input()
        if receiver=="1":
            count = count + 1
            pass
        elif mail_list(receiver)[0]==1:
            count = 0
            receiver_id = mail_list(receiver)[1]
            speak_for(name, f"You want to mail {receiver}.")
            print(receiver, receiver_id)
            speak_for(name, "say Yes for confirmation, otherwise say No.")
            while True:
                if count > 90:
                    return
                text = audio_input()
                if text == "yes":
                    t = False
                    break
                elif text =="no":
                    break
                elif text=="1":
                    count = count + 1
                else:
                    count = 0
                speak_for(name,f"Is receiver mail ID {receiver_id}, Okay?")
        else:
            count = 0
    time.sleep(1)
    t = True
    count = 0
    while t:
        if count > 90:
            return
        speak_for(name, random.choice(mail_subject_text))
        subject = audio_input()
        if subject=="1":
            count = count + 1
            pass
        else:
            count = 0
            speak_for(name, f"Mail subject is {subject}.")
            print(subject)
            speak_for(name, "say Yes for confirmation, otherwise say No.")
            while True:
                if count > 90:
                    return
                text = audio_input()
                if text == "yes":
                    t = False
                    break
                elif text =="no":
                    break
                elif text=="1":
                    count = count + 1
                else:
                    count = 0
                speak_for(name, f"Is mail subject: {subject}, Okay?")
    time.sleep(1)
    t = True
    msg = ""
    count = 0
    while t:
        if count > 90:
            return
        speak_for(name, random.choice(mail_message_text) + " or say exit to end the message")
        msge = audio_input()
        if msge=="1":
            count = count + 1
            pass
        elif msge in mail_exit_text:
            t = False
            count = 0
        else:
            count = 0
            speak_for(name, f"Your message is : {msge}.")
            print(msg)
            print("New line is:")
            print(" " + msge + " ")
            speak_for(name, "say Yes for confirmation, otherwise say No.")
            while True:
                if count > 90:
                    return
                text = audio_input()
                if text == "yes":
                    msg = msg + " " + msge
                    break
                elif text =="no":
                    break
                elif text=="1":
                    count = count + 1
                else:
                    count = 0
                speak_for(name,"Is message: {msge}, Okay?")
    time.sleep(1)
    count = 0
    while True:
        if count > 90:
            return
        speak_for(name, random.choice(mail_confirmation_text))
        answer = audio_input().lower()
        if answer=="1":
            count = count + 1
            pass
        elif answer=="yes":
            mail(receiver, subject, msg)
            speak_for(name, random.choice(mail_sent_text))
            return
        elif answer=="no":
            with open('draft_mail.txt', 'a') as file:
                file.write("Receiver Mail: " + receiver + "\n")
                file.write("Mail Subject: " + subject + "\n")
                file.write("Message: " + msg + "\n \n")
            return
        else:
            count = 0

def current_time(name:str):
  speak_for(name,"time is" + str(datetime.now().hour) + ":" + str(datetime.now().minute))

def test_mail(name:str):
  while True:
    speak_for(name, random.choice(rec_name_text))
    rec = audio_input()
    if mail_list(rec)[0]==1:
      rec_id, sub, msg = test(rec)
      mail(rec_id, sub, msg)
      speak_for(name, random.choice(mail_sent_text))
      return
