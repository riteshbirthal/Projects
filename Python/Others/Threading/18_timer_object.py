# 
# Timer Object:-
#       Thread will run after t time
# 


import threading

def test():
    for i in range(10):
        print("Hello World!")
    

timer = threading.Timer(3, test)
timer.start()

for i in range(10):
    print("Main Thread....")
