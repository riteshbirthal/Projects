# R-Lock:
#  
# You cannot acquire/release multiple times using Lock mechanism
#
# By using R-Lock, we can acquire/release multiple times
# R-Lock is just a modified version of Lock
#
# R-Lock also contains information about current thread
#

from threading import *

rlock = RLock()
class Bus:
    def __init__(self, name, available_seats, rlock):
        self.available_seats = available_seats
        self.name = name
        self.rlock = rlock
        
    def reserve(self, required_seats):
        self.rlock.acquire()
        print("R-Lock 1st: ", self.rlock)
        self.rlock.acquire()
        print("R-Lock 2nd: ", self.rlock)
        print("Available seats are: ", self.available_seats)
        if self.available_seats >= required_seats:
            nm = current_thread().name
            print(f"{required_seats} are allocated to {nm}")
            print("Congralutions. You got the seats..")
            self.available_seats -= required_seats
        else:
            print("Sorry. Required seats are not available.")
        self.rlock.release()
        self.rlock.release()

b1 = Bus("Travellers Travels 1", 2, rlock)
t1 = Thread(target=b1.reserve, args=(2,), name="Jay")
t2 = Thread(target=b1.reserve, args=(2,), name="Raj")
t1.start()
t2.start()