# Thread Synchronization Technique :
#
# Thread Synchronization is defined as a mechanism which ensures
# that two or more concurrent threads do not simultaneously
# execute some particular program segment known as critical section
#
# There are 3 thread synchronization techniques
#   Using Locks
#   Using R-Locks
#   Using Semaphores
#
#
#
# Locks in Python:
#
# Threading module provides a Lock class to deal with the race conditions
# Lock has two states:
# Locked: The Lock has been acquired by one thread and any thread
# that makes an attempt to acquire it must wait until it is released.
# Unlocked: The lock has not been acquired and can be acquired by the
# next thread that makes an attempt.

# acquire() method:
# change the state of code to locked.
# other threads have to wait until lock is released by current working thread
# Syntax:
#   lock_object.acquire([blocking=True], timeout=-1)  both are optional parameters
#
# Note: Cannot acquire/release multiple time any lock


from threading import *
from time import sleep

# mylock = Lock()

# def task(mylock, message):
#     mylock.acquire()
#     for i in range(5):
#         print(f"task function called with message: {message}")
#     sleep(3)
#     mylock.release()
# t1 = Thread(target=task, args=(mylock, "Thread 1"))
# t2 = Thread(target=task, args=(mylock, "Thread 2"))
# t1.start()
# t2.start()

lock = Lock()
class Bus:
    def __init__(self, name, available_seats, lock):
        self.available_seats = available_seats
        self.name = name
        self.lock = lock
        
    def reserve(self, required_seats):
        self.lock.acquire()
        print("Available seats are: ", self.available_seats)
        if self.available_seats >= required_seats:
            nm = current_thread().name
            print(f"{required_seats} are allocated to {nm}")
            print("Congralutions. You got the seats..")
            self.available_seats -= required_seats
        else:
            print("Sorry. Required seats are not available.")
        self.lock.release()

b1 = Bus("Travellers Travels 1", 2, lock)
t1 = Thread(target=b1.reserve, args=(2,), name="Jay")
t2 = Thread(target=b1.reserve, args=(2,), name="Raj")
t1.start()
t2.start()