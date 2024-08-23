# Barrier Object:-
#   Allows threads to wait for each other at a specific point in their
#   execution before proceeding futher
# 

import threading
import time

number_of_players = 4
barrier = threading.Barrier(number_of_players)

def player(name):
    print(f"{name} started")
    score = 0
    for i in range(5):
        time.sleep(2)
        print(f"{name} is playing..")
        
    # barrier
    barrier.wait()
    
    # code for session killing
    
    # code for displaying final results
    print(f"{name} scored {score}")
    barrier.wait()
    # code for sending winning amount into accounts
    print(f"sending winning amount to {name}")
   
Threads = []    
player_names = ["Player 1", "Player 2", "Player 3", "Player 4"]

for name in player_names:
    thread = threading.Thread(target=player, args=(name, ))
    Threads.append(thread)
    thread.start()
    
