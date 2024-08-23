import threading
import time

def display():
    for i in range(10):
        print("Tracking Order...")
        time.sleep(1)
        

t1 = threading.Thread(target=display)
t1.daemon = True
t1.start()

time.sleep(5)
print("Order Delivered..")