# Important Notes:
# 1. No control on CPU core, which cpu core will be allocated to which thread
# 2. If there are no multiple cores in CPU, then threads will not executed parallely

# import Thread class from threading 
from threading import Thread, current_thread

# Create function containing code for parallel execution
def func(iter, message):
    print("thread1 Thread details: ", current_thread())
    print("thread1 Thread name: ", current_thread().name)
    print("thread1 Thread id: ", current_thread().ident)
    for i in range(iter):
        print(message)
        
# Creating thread
thread1 = Thread(target=func, args=(10, "Hello World"))
# thread1 = Thread(target=func, kwargs={"iter":10, "message":"Hello World"})
 
# if there is only one arguments
# thread1 = Thread(target=func, args=(10,))

# starting the thread
thread1.start()

for i in range(10):
    print("testing parallel execution")