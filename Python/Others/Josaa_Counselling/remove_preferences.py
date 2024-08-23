import time
from button_detection import *
    
remove_path = 'remove.png'
remove_ok_path = 'remove_ok.png'
cancel_changes_path = 'cancel_changes.png'

time.sleep(5)
while True:
    flag = 1
    if clicking_button(remove_path, 0.8)==False:
        if clicking_button(cancel_changes_path)==False:
            flag = 2
    time.sleep(1)
    if flag==2:
        print("Remove button not found...")
        break
    clicking_button(cancel_changes_path)
    
    if clicking_button(remove_ok_path)==False:
        if clicking_button(cancel_changes_path)==False:
            flag = 3
    time.sleep(1)
    if flag==3:
        print("Ok button not found...")
        break
