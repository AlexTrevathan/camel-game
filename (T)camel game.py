#Camel_chaseV3.py
#You need to alter this code and make it your own, if you dont understand it
#you can just finish the code, adding things like dying of thirst.
#As an extension you could make the program ask if the user wants to play again.

import random
our_distance = 0
chasers_distance = 0
thirst = 0
tiredness = 0
DESERT_LENGTH = 100

print("Welcome to the Camel chase game")
print("you have stolen a Camel and you are running from the owners.")
print("You need to stay ahead of the owners and get to the end of the desert")
print("before they catch you. Keep a look out for dehydration and tiredness")
print("----------------- GOOD LUCK ----------------")

game_finished = False
while not game_finished:
    print("1) Go forward and a fast speed")
    print("2) Go forward at a moderate pace")
    print("3) Rest your Camel for the night")
    print("4) Take a drink")
    print("5) Check status")
    print("q) Quit")
    print()
    choice = input(": ")
    if choice == "q" or choice == "Q":
        game_finished = True
    elif choice == "1":
        our_distance = our_distance + random.randrange(9,16)
        chasers_distance = chasers_distance + random.randrange(7,13)
        print("You have gone forward at a fast pace")
        print("We are now", our_distance, "from the base")
        print("The chaser are",chasers_distance,"from the base")
        thirst = thirst + random.randrange(1,4)
        tiredness = tiredness + random.randrange(1,4)
        print("The chasers are",our_distance - chasers_distance, " behind us" )
    elif choice == "2":
        our_distance = our_distance + random.randrange(6,13)
        chasers_distance = chasers_distance + random.randrange(7,13)
        print("You have gone forward at a moderate pace")
        print("We are now", our_distance, "from the base")
        print("The chaser are",chasers_distance,"from the base")
        thirst = thirst + random.randrange(0,2)
        tiredness = tiredness + random.randrange(0,2)
        print("The chasers are",our_distance - chasers_distance, " behind us" )
    elif choice =="3":
        print("You have rested your camel")
        chasers_distance = chasers_distance + random.randrange(7,13)
        print("We are now", our_distance, "from the base")
        print("The chaser are",chasers_distance,"from the base")
        tiredness = 0
        print("The chasers are",our_distance - chasers_distance, " behind us" )
    elif choice =="4":
        print("You have had a drink")
        chasers_distance = chasers_distance + random.randrange(0,2)        
        print("We are now", our_distance, "from the base")
        print("The chaser are",chasers_distance,"from the base")
        thirst = 0
        print("The chasers are",our_distance - chasers_distance, " behind us" )
    if our_distance - chasers_distance <= 0:
        print("You have been caught and for you the chase is over")
        game_finished = True
    if tiredness > 7:
        print("Your Camel is too tired to continue, for you the chase is over")
        game_finished = True
    elif tiredness > 4:
        print("Your Camel is getting tired, you should rest.")
    if our_distance >= DESERT_LENGTH:
        print ("Congratulation you won")
        game_finished = True        
print("Thanks for playing")
