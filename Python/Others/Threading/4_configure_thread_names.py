

from threading import Thread
import os

def func1():
    for i in range(5):
        print("Function 1 is called..")


def func2():
    for i in range(5):
        print("Function 2 is called..")


t1 = Thread(target=func1)
t2 = Thread(target=func2)

t1.name = "fununction1 thread"
t2.name = "fction2 thread"

# t1.setName("function1 thread")
# t2.setName("function2 thread")

print(t1.name)
print(t2.name)

t1.start()
t2.start()

print("Thread ID: ", t1.ident)
print("Native Thread ID: ", t1.native_id)
print("PID: ", os.getpid())

# old method to access names
# print(t1.getName())
# print(t2.getName())


# Thread Identifiers

# 1. Thread identifier : given by process
# 2. Native identifier : given by operating system

# Thread Identifier:
#   Each thread has unique identifier within a Python process
#   Assigned by the Python interpreter
#   Read-only positive integer and unique in process
#   Assigned after starting thread
#   This identifier is stored in an instance variable:- ident 

# Native identifier:
#   Each thread has unique identifier assigned by the OS
#   property name: native_id(assigned after thread has started)
#   Note:-  generally, ident and native_id are same

# PID:
#   Identifier for your process(program)
#   OS Module: getpid()