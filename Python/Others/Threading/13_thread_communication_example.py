# Traffic Light Signal

import threading
import time

e = threading.Event()

def light_switch():
    while True:
        print("Light is green")
        e.set()
        time.sleep(5)
        print("Light is red")
        e.clear()
        time.sleep(5)

def traffic_message():
    e.wait()
    while e.is_set():
        print("You can Go!")
        time.sleep(1)
        e.wait()

t1 = threading.Thread(target=light_switch)
t2 = threading.Thread(target=traffic_message)

t1.start()
t2.start()


# File handling
# Description: read 5 line from one text file and write to another text file
#              until it reaches to end of file