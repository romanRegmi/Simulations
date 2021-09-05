import random
from cll import CircularLinkedList

players = {"Joshep":0, "Roman":0, "Jacob":0, "Isaac":0, "Abraham":0}

print("==============================================================")

dead = []
bullet = 1

while(len(players)>1):
    keys = players.keys()
    brave_hearts = CircularLinkedList() #Initialize a circular linked list object
    
    for key in keys:
        brave_hearts.append(key)
    
    for key in keys:
        if random.randint(1,6) <= bullet:
            players[key] = 1
      
        if players[key] == 1:
            dead.append(brave_hearts.find_next(key))
    
    for nms in dead:
        print(nms + " GOT KILLED!!")
        players.pop(nms)
        
    for val in players:
        players[val] = 0
        
    dead = []
    bullet += 1

print("==============================================================")

if len(players)>0:
    winner = list(players.keys())
    print(winner[0] + " WON")
else:
    print("EVERYBODY GOT KILLED")

