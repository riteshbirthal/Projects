from calendar import day_name
import os
from datetime import datetime
from utils import *

#constants
stat_mech_text = ['join stastical mechanics lecture', 'joint stastical mechanics lecture', 'join for 12 lecture']

qm2_text = ['join quantum mechanics lecture', 'join quantum lecture', 'joint quantum lecture']

mm2_text = ['join mathematical method lecture', 'join mm2 lecture', 'join mathematical lecture', 'join 422 lecture']

me685_text = ['join 685 lecture', 'join numerical method lecture', 'join numerical lecture']

lect_text = ['join lecture', 'join current lecture', 'join ongoing lecture']

def stat_mech():
  os.system("xdg-open 'Meet-Link'")

def quant_mech_2():
  os.system("xdg-open 'Meet-Link'")

def math_method_2():
  os.system("xdg-open 'Meet-Link'")

def ME685A():
  pass

def exp_phy_2():
  pass

def lecture(name:str):
  h = int(datetime.now().hour)
  d = int(datetime.today().weekday())
  m = int(datetime.now().minute)
  if d==0 and ((h==9 and m>=50) or (h==10)):
    stat_mech()
  elif d==1:
    if ((h==11 and m>=50) or (h==12)):
      quant_mech_2()
    elif ((h==15 and m>=20) or (h==16)):
      speak_for(name, 'Open mail inbox for lecture link.')
    else:
      speak_for(name,'No lecture scheduled for this moment.')
  elif d==2:
    if ((h==9 and m>=50) or (h==10 and m<50)):
      stat_mech()
    elif ((h==10 and m>=50) or (h==11 and m<50)):
      math_method_2()
    elif ((h==11 and m>=50) or (h==12)):
      quant_mech_2()
    else:
      speak_for(name,'No lecture scheduled for this moment.')
  elif d==3:
    if ((h==13 and m>=50) or (h==14)):
      stat_mech()
    else:
      speak_for(name,'No lecture scheduled for this moment.')
  elif d==4:
    if ((h==10 and m>=50) or (h==11 and m<50)):
      quant_mech_2()
    elif ((h==11 and m>=50) or (h==12)):
      stat_mech()
    elif ((h==15 and m>=20) or (h==16)):
      speak_for(name, 'Open mail inbox for lecture link.')
    else:
      speak_for(name,'No lecture scheduled for this moment.')
  elif d==5:
    if ((h==13 and m>=50) or (h==14)):
      stat_mech()
    else:
      speak_for(name,'No lecture scheduled for this moment.')
  elif d==6:
    speak_for(name, 'Just enjoy the day, because it is SUNDAY.')
  else:
    speak_for(name,'No lecture scheduled for this moment.')
