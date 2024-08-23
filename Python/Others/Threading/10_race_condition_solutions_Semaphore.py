# In Lock and R-Lock, at a time only one Thread is allowed to execute.
# 
# But sometimes we may require to execute more than one Threads.
# 
# Semaphore can be used to limit the access to the shared resources
# with limited capacity.
# 
# Semaphore counter
# On thread acquire --- counter -= 1
# On thread release --- counter += 1
# 
# Semaphore can be used to avoid race condition if its thread limit is set to 1

from threading import * 
import time

lock = Semaphore(4)
# lock = BoundedSemaphore(4) # used to avoid inappropriate use of acquire/release

def func(message: str):
    # acquire: decrement counter by 1
    lock.acquire()
    for i in range(4):
        print(message)
        time.sleep(5)
    lock.release()
    # release: increment counter by 1

t1 = Thread(target=func, args=("Thread-1",))
t2 = Thread(target=func, args=("Thread-2",))
t3 = Thread(target=func, args=("Thread-3",))
t4 = Thread(target=func, args=("Thread-4",))
t5 = Thread(target=func, args=("Thread-5",))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()