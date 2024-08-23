import pandas as pd
import time
import keyboard
from button_detection import *


dataframe1= pd.read_excel('Josaa_Seat_Preferences.xlsx', sheet_name='Sheet13')
dataframe1 = dataframe1[["Institute", "Program Name", "City"]]
# temp = dataframe1["City"]
# print(temp)
time.sleep(5)
path = ['cancel_changes.png', 'clear_filter.png', 'institutes.png', 'program.png', 'filter.png', 'add.png', 'Ok.png']


for index, row in dataframe1.iterrows():
    if keyboard.is_pressed('q'):
        break
    print(row['City'], row['Program Name'])
    flag = 1
    clicking_button(path[0])
    if clicking_button(path[1], 0.8)==False:
        if clicking_button(path[0])==False:
            flag = 2
        elif clicking_button(path[1], 0.8)==False:
            flag = 2
    time.sleep(1)
    if flag==2:
        print("Clear Filter button not found...")
        break
    clicking_button(path[0])
    
    print("===Clicking Insitute Field===")
    if clicking_button(path[2], 0.8)==False:
        if clicking_button(path[0])==False:
            flag = 2
        elif clicking_button(path[2], 0.8)==False:
            flag = 2
    time.sleep(1)
    if flag==2:
        print("Institute button not found...")
        break
    clicking_button(path[0])
    
    print("===Entering Institute Data===")
    pyautogui.write(row['City'])
    time.sleep(1)
    
    clicking_button(path[0])
    
    print("===Pressing Enter Key===")
    pyautogui.press('enter')
    time.sleep(1)

    print("===Clicking Text Field===")    
    if clicking_button(path[3], 0.8)==False:
        if clicking_button(path[0])==False:
            flag = 3
        elif clicking_button(path[3], 0.8)==False:
            flag = 3
    time.sleep(1)
    if flag==3:
        print("Program button not found...")
        break
    
    clicking_button(path[0])
    
    print("===Entering Academic Program Data===")
    pyautogui.write(row['Program Name'])
    time.sleep(1)
    
    clicking_button(path[0])
    
    print("===Pressing Filter Button===")
    if clicking_button(path[4], 0.8)==False:
        if clicking_button(path[0])==False:
            flag = 4
        elif clicking_button(path[4], 0.8)==False:
            flag = 4
    time.sleep(1)
    if flag==4:
        print("Program button not found...")
        break
    
    clicking_button(path[0])
    
    print("===Pressing Add Button===")
    if clicking_button(path[5])==False:
        clicking_button(path[0])
        time.sleep(1)
        if clicking_button(path[5]) == False:
            print("This branch not found....")
        else:
            print("Branch added successfully")
    else:
        print("Branch added successfully")
    
    clicking_button(path[0])
    time.sleep(1)
    
    if clicking_button(path[6])==False:
        clicking_button(path[0])
        time.sleep(1)
        if clicking_button(path[6]):
            print("Branch added successfully")
    else:
        print("Branch added successfully")
    print("===Sleeping For 1 second===")
    time.sleep(1)
