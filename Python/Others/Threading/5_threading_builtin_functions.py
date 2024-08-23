# Thread build-in functions

# is_alive() :- Checks if thread is running or not
# main_thread() :- Returns main threads details
# active_count() :- Number of running threads
# enumerate() :- List of all running threads
# get_native_id() :- get native id of thread

from threading import Thread, main_thread, active_count, enumerate, get_native_id
import os

def func1():
    print("Main thread details: ", main_thread())
    print("native id of t1 thread: ", get_native_id())
    for i in range(5):
        print("Function 1 is called..")


def func2():
    for i in range(5):
        print("Function 2 is called..")


t1 = Thread(target=func1)
t2 = Thread(target=func2)
print("Before t1 started: ", t1.is_alive())
t1.start()
print("Number of active threads: ", active_count())
print("Running threads: ", enumerate())
print("native id of main thread: ", get_native_id())
print("After t1 started: ", t1.is_alive())