#
# Need of Condition object:-
#       To communicate with multiple threads
#       Event object:- communication between two threads
#
# Steps:-
#       Create condition object
#       Syntax: con = threading.Condition([lock_object])
#       lock_object is optional, otherwise default is used
#
# Condition Object Methods:
# acquire():-
#       This method is used to acquire the lock
#       
# release():-
#       This method is used to release the lock
#
# wait(timeout=0):-
#       This method is used to block the thread
#       Thread will wait until it gets signal
#
# notify():-
#       Wake up one thread
#
# notify_all():-
#       Wake up multiple threads
#
# Note: These methods must be called only when the calling thread has acquired the lock
#
#
#
#

import threading
import time


def write_data():
    con.acquire()
    with open('report.txt', 'w') as file:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for day in days:
            temp = input(f"Enter the temperature for {day}: ")
            file.write(temp + "\n")
    con.notify_all()
    con.release()


def max_temp():
    con.acquire()
    con.wait(timeout=0)
    with open('report.txt', 'r') as file:
        data = file.readlines()
        mx = float(data[0].strip("\n"))
        for temp in data[1:]:
            temp = float(temp.strip("\n"))
            if temp > mx:
                mx = temp
        print("Maximum temperature is: ", mx)
    con.release()


def avg_temp():
    con.acquire()
    con.wait(timeout=0)
    with open('report.txt', 'r') as file:
        data = file.readlines()
        sm = 0
        for temp in data[1:]:
            temp = float(temp.strip("\n"))
            sm = sm + temp
        avg = sm/len(data)
        print("Average temperature of the week is: ", avg)
    con.release()


con = threading.Condition()

t1 = threading.Thread(target=write_data)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)

t1.start()
t2.start()
t3.start()
