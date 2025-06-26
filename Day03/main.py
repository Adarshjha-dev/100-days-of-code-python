print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____ 
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your goal is to survive the journey and discover the hidden treasure.")

choice1 = input("You are on a jungle path that splits in two directions.\n"
                "Do you go into the \"cave\" or follow the \"river\"?\n").lower()

if choice1 == "river":
    choice2 = input("You follow the river and reach a fast-moving stream.\n"
                    "A small, empty boat is tied to a post on the shore.\n"
                    "Do you \"wait\" and use the boat, or try to \"swim\" across?\n").lower()

    if choice2 == "wait":
        choice3 = input("You wait. After some time, a local arrives and helps you cross safely.\n"
                        "On the other side, you find an ancient temple with three doors:\n"
                        "One marked with a \"snake\", one with a \"lion\", and one with a \"bird\".\n"
                        "Which door do you choose?\n").lower()

        if choice3 == "bird":
            print("Inside, you find a quiet room filled with glittering treasure. You win!")
        elif choice3 == "snake":
            print("It leads to a pit of snakes. Game over.")
        elif choice3 == "lion":
            print("The tunnel collapses. You're trapped. Game over.")

    else:
        print("You try to swim, but the current is too strong. You drown. Game over.")

else:
    print("You enter the cave and trigger a hidden trap. Game over.")
