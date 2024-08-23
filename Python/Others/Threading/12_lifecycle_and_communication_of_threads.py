
# Thread Life-Cycle

# create to start thread         -->   Stage 1 (New Thread)
# after calling start method     -->   Stage 2 (Runnable)  has two states: Active and Blocked
# thread can go for IO           -->   Blocked Stage (Sleeping)
# if exception                   -->   Stage 3 (Terminate with Exception)
# else                           -->   Stage 3 (Terminate Normally)



# Thread Communication

# 1. Using Event
#       Only 2 threads can communicate using Event Object.
#       Not applicable for multiple threads communication
#
# Steps:
#       Create an event object
#       Create 2 threads
#       Put Thread 2 in waiting by using wait()
#       Use set() method in/after Thread 1 code.. Set method will change Flag value
#
# set():-
#       Set the internal flag to True
#       If flag is True, waiting thread is awakened
#
# reset():-
#       Reset the internal flag to false
#       Other thread will wait() again
#
# is_set():-
#       Return True if and only if the internal Flag is True
#       example-    if event.is_set():
#                       code
#
# wait([timeout]):-
#       Calling this function keep other thread on wait until flag is set to True
#       timeout is optional parameter, default value is -1
#       wait(15) ... will wait for signal for 15sec. after which it will start executing code if it doesn't get any signal
#
#
#
#

import threading
import time

e = threading.Event()

def task():
    print("Application started...")
    time.sleep(5)
    e.set()

def end():
    e.wait()
    if e.is_set():
        print("Application exited...")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=end)

t1.start()
t2.start()


 