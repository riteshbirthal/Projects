# If an exception occurs in any thread then it has not impact
# on other threads, all other threads will work as usual.
# 
# Exception in thread:
#   The interpreter calles threading.excepthook() with one
#   argument i.e. named tuple with 4 arguments-
#       the exception class
#       exception instance/value
#       a traceback object
#       Thread name
# 
#
#   For Main Thread       -------->     sys.excepthook
#   For Created Thread    -------->     threading.excepthook --> sys.excepthook
#

import threading
from time import sleep

# args is tuple containing 4 values
def custom_hook(args):
    print("Exception occurred in thread")
    print(args[0])
    print(args[1])
    print(args[2]) #traceback object
    print(args[3])
    
    
def display():
    for i in range(5):
        sleep(0.1)
        print("abc" + 1)


def show():
    for i in range(5):
        print("xyz")
        sleep(0.2)
        
        
threading.excepthook = custom_hook  # overriding this function
t1 = threading.Thread(target=display)
t2 = threading.Thread(target=show)
t1.start()
t2.start()
t1.join()
t2.join()

for i in range(5):
    print("Hello World")

print("\n\n\nEnd of Program\n\n\n")