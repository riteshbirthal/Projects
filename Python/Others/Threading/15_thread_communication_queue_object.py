#
# queue Module:-
#       queue.Queue() class
#       my_queue = queue.Queue(maxsize)
#       maxsize is optional
#
# put(item, block=True):-
#       This method is used to insert elements into queue
#       when block is False, then you get exception in case of inserting element more than maxsize
#
# get():-
#       This method is used to delete elements from queue
#
#
# Benefits:-
#       Thread safe: No Race Condition
#       Implements all the required locking semantics
#
#
#

import time
import threading
import queue

def producer(my_que):
    print("producer: running")
    n = int(input("Enter number of students: "))
    for i in range(n):
        marks = float(input("Enter marks: "))
        my_que.put(marks)
    my_que.put(None) # stopping condition
    print("producer: end")
    

def consumer(my_que):
    print("consumer: running")
    while True:
        item = my_que.get()
        if item is None:
            break
        print(f"Got {item}")
    print("consumer: end")
    
my_que = queue.Queue()
t1 = threading.Thread(target=producer, args=(my_que, ))
t2 = threading.Thread(target=consumer, args=(my_que, ))
t1.start()
t2.start()