from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take? Enter a number")

    choice = int(input("> "))
    if choice > 0:
        how_much = int (choice)
    else:
        dead("Man, learn to type a number")

    if 0 < how_much < 50:
        print("Nice, you are not greedy, you win!")
        #exit code here, 0 means no problem, 1 or non zero means problem
        exit(0)
    elif how_much < 0: #won't excute because of not in a while loop? goes to ded
        print("Can't do that")
    else:
        dead("You greedy bastard! Die!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear? Taunt him?")
    bear_moved = False
    #boolean variable

    #main loop meaning while bear not moved
    while True:
        choice = input("> ")
        #this is a local fxn

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" or "taunt him" and not bear_moved:
            #joint condition, bear not moved
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
            #the bear moved
        elif choice == "taunt bear" or "taunt him" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            #goes to the gold room
            gold_room()
        else:
            print("I have no idea what that means.")


def cthulu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    elif "fight" in choice:
        print("Unbelivable, you've defeated the monstrous Cthulu!")
        print("You see a room behind its limping body and go through it")
        gold_room()
    else:
        print("Did you meant to type 'eat my head?'")
        cthulu_room()


def dead(why):
    print(why, "Good job!")
    #quits the loop
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

start()

#5.problem with the gold input, it doesn't allow for certain values none 0/1
