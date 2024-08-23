import veronica
import jarvis
import speech_recognition as sr
from utils import *

veronica_text = ["veronica start", "veronica wake up", "wake up veronica", "veronica turn on", "turn on veronica", "turn on yourself veronica", "veronica turn on yourself","veronika start", "veronika wake up", "wake up veronika"]
jarvis_text = ["jarvis start", "jarvis wake up", "wake up jarvis",  "jarvis turn on", "turn on jarvis", "turn on yourself jarvis", "jarvis turn on yourself"]

def main():
  while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = round(float(str(battery.percent)),2)
    plugged = "Plugged In" if plugged else "Unplugged"
    if ((percent > 80) or (plugged=="Plugged In")) and return_td_val("battery_mail")==0:
      update_td_val("battery_mail", 1)
    elif (percent < 30) and (plugged == "Unplugged") and return_td_val("battery_mail"):
      rec_id, sub, msg = battery_low()
      thread_fun(mail, "Veronica", None, {rec_id, sub, msg}, 2)
      update_td_val("battery_mail", 0)
    elif percent < 15:
      shutdown()
    text = audio_input()
    try:
      if text.lower() in veronica_text:
        speak_for('Veronica', f"{veronica.NAME} starting")
        veronica.main()
        speak_for('Veronica', f"{veronica.NAME} stopped")
      elif text.lower() in jarvis_text:
        speak_for('Jarvis', f"{jarvis.NAME} starting")
        jarvis.main()
        speak_for('Jarvis', f"{jarvis.NAME} stopped")
    except:
      if text != "1":
        print('you said ' + text)


if __name__ == '__main__':
  main()
