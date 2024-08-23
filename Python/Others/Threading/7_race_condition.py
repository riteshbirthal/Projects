# Race Condition : a bug in concurrency programming
# It is a bug generated when you do multiprocessing. It occurs
# because two or more threads tries to update the same variable
# and results into unreliable output.
# Concurrent accesses to shared resource can lead to race condition.

# Thread synchronization Technique
# a common approach is to protect the critical section of code.(Prevent concurrent access)
# We have following thread synchronization techniques.
#   Using Locks
#   Using R-Lock
#   Using Semaphores


# Example 1
# var = value
# t1(adder thread) : adds a something to var
# t2(subtractor thread) : subtract something from var

# if they run parallely then output will be unexpected...

# Example 2
from threading import *

class Bus:
    def __init__(self, name, available_seats):
        self.available_seats = available_seats
        self.name = name
        
    def reserve(self, required_seats):
        print("Available seats are: ", self.available_seats)
        if self.available_seats >= required_seats:
            nm = current_thread().name
            print(f"{required_seats} are allocated to {nm}")
            print("Congralutions. You got the seats..")
            self.available_seats -= required_seats
        else:
            print("Sorry. Required seats are not available.")

b1 = Bus("Travellers Travels 1", 2)
t1 = Thread(target=b1.reserve, args=(1,), name="Jay")
t2 = Thread(target=b1.reserve, args=(2,), name="Raj")
t1.start()
t2.start()