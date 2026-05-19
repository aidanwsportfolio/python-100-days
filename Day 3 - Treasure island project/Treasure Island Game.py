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
print("Welcome player one... this is Treasure Island!")
print("Go find the treasure. Get to work!")

direction = input("Do you want to go left or right? Type R for right, and L for left: \n")
if direction == "R" or direction == "r":
    print("You fall into a hole, game over") #
elif direction == "L" or direction == "l":
    will_swim = input("You go left and make it through! will you swim or wait? type 'S' to swim, or 'W' to wait: \n")
    if will_swim == "S" or will_swim == "s": #nested inside of the elif
        print("you've been attacked by trout. Game over")
    elif will_swim == "W" or will_swim == "w":
        print("You waited for a Water Taxi and made it through!")
        which_door = input("now which door are you gonna open, Red 'R', Blue 'B', or Yellow 'Y'\n")
        if which_door == "R" or which_door == "r": #nested inside of the elif, this will not work if on it's on branch
            print("You were burned by a fire, game over.")
        elif which_door == "B" or which_door == "b":
            print("You were eaten by beasts, game over twin.")
        elif which_door == "Y" or which_door == "y":
            print("YOU WIN! , what a champ!")
        else:
            print("Game over. That literally wasn't an option.")
    else:
        print("Game over.")

else:
    print("Game over.")


