# 
# IDLE app:-
#   Thread 1: Main Thread
#   Thread 2: Thread for interactive shell
#   Thread 3: Thread for Editor
#   Thread 4: Thread for python interpreter
#   Thread 5: Thread for text highlighting
#   Thread 6: Thread for memory management
# 
# Types of Threads:
#   Non-Daemon Threads (Non-Supportive Threads)
#   Daemon Threads (Supportive Threads)
# 
# For IDLE App, Thread 1 to 4 are Non Daemon Threads and 5, 6 are Daemon Threads
# 
# Non-Daemon Threads:-
#   A program will not terminate until all non-daemon threads gets completed
# 
# Daemon Threads:-
#   Daemon threads will automatically closed after closing all non-daemon threads
#   Definition: A daemon thread is a thread which runs continuously in background
#               and provide support to other non-daemon threads
#
# Use of Daemon Threads:-
#   Daemon threads are often used for tasks such as monitoring,
#   background services, or cleanup operations
#
#   t1.daemon = True      Daemon thread
#   cannot change nature of thread to daemon or non-daemon while it is running
#   
#   Note:- Main Thread is Non-Daemon
#

# Checking nature of Main Thread
import threading

obj = threading.current_thread()

print("Daemon nature of Main Thread: ", obj.daemon)

# Changing nature of thread
def display():
    print("Inside display function")
    t2 = threading.Thread(target=test)
    print("Daemon nature of t2: ", t2.daemon)
    t2.start()
    

def test():
    print("Inside test function")

# t1 got Non-daemon nature from its parent i.e. Main Thread
t1 = threading.Thread(target=display)
print("Daemon nature of t1 is: ", t1.daemon)
t1.daemon = True
# t1.setDaemon(True)
print("Daemon nature of t1: ", t1.daemon)
t1.start()
# t1.daemon = True    # will get error

print("This is Main Thread")

