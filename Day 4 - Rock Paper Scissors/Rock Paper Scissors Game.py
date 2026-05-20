import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_RPS_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: \n"))

#logic for rock
if user_RPS_choice == 0:
    print("You chose\n" + rock)
    computer_RPS_choice = random.randint(0,2)
    if computer_RPS_choice == 0:
        print("Computer Chose\n" + rock)
        print("\n Tie!")
    elif computer_RPS_choice == 1:
        print("You chose\n" + paper)
        print("\n You Lose")
    elif computer_RPS_choice == 2:
        print("You chose\n" + scissors)
        print("\n You Win!")
#Logic for paper
if user_RPS_choice == 1:
    print("You chose\n" + paper)
    computer_RPS_choice = random.randint(0,2)
    if computer_RPS_choice == 0:
        print("Computer Chose\n" + rock)
        print("\n You Win!")
    elif computer_RPS_choice == 1:
        print("You chose\n" + paper)
        print("\n Tie!")
    elif computer_RPS_choice == 2:
        print("You chose\n" + scissors)
        print("\n You Lose!")
#Logic for scissors
if user_RPS_choice == 2:
    print("You chose\n" + scissors)
    computer_RPS_choice = random.randint(0,2)
    if computer_RPS_choice == 0:
        print("Computer Chose\n" + rock)
        print("\n You Lose!")
    elif computer_RPS_choice == 1:
        print("You chose\n" + paper)
        print("\n You Win!")
    elif computer_RPS_choice == 2:
        print("You chose\n" + scissors)
        print("\n Tie!")
else:
    print("invalid option")