# If a thread wants to wait for some other thred, then we should go for join() method
from threading import Thread
import time

def func1():
    print("Function 1 started....")
    time.sleep(2)
    print("Function 1 ended.")
    
def func2():
    print("Function 2 staeted...")
    time.sleep(3)
    print("Function 2 ended.")

start = time.time()
func1()
func2()
print("Time without multithreading: ", time.time()-start)

start = time.time()
t1 = Thread(target=func1)
t2 = Thread(target=func2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Time with multithreading: ", time.time()-start)

print("End of Program!!!")
    