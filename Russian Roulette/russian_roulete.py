#Inspired by an IG Post
import random
for n in range (6,0,-1):
    if random.randint(1,n) == 1:
        #Your Bullet/ what happens
        print("u dead")
        exit()
    else:
        print("u lucky")
        n = n - 1

#this code can be made into with an terminal ui(i.e. press enter to continue like a mini game, 2 players)