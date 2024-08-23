import pandas as pd
import pyautogui
import time
import keyboard


dataframe1= pd.read_excel('Josaa_Seat_Preferences.xlsx', sheet_name='Sheet13')
dataframe1 = dataframe1[["Institute", "Program Name", "City"]]
# temp = dataframe1["City"]
# print(temp)
time.sleep(5)


for index, row in dataframe1.iterrows():
    if keyboard.is_pressed('q'):
        break
    print(row['City'], row['Program Name'])
    
    print("===Clicking Insitute Field===")
    pyautogui.click(x=848, y=277)
    time.sleep(1)
    
    print("===Entering Institute Data===")
    pyautogui.write(row['City'])
    time.sleep(1)
    
    print("===Pressing Enter Key===")
    pyautogui.press('enter')
    time.sleep(1)

    print("===Clicking Text Field===")    
    pyautogui.click(x=410, y=329)
    time.sleep(1)
    
    print("===Entering Academic Program Data===")
    pyautogui.write(row['Program Name'])
    time.sleep(1)
    
    print("===Pressing Filter Button===")
    pyautogui.click(x=1319, y=325)
    time.sleep(1)
    
    print("===Pressing Add Button===")
    pyautogui.click(x=745, y=538)
    
    print("===Sleeping For 1 second===")
    time.sleep(1)
