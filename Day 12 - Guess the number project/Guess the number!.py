import art
import random

print(art.logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100!")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

random_number = random.randint(1, 100) #generate random number

# Set attempts based on difficulty
total_guesses = 10 if difficulty == "easy" else 5
print(f"You have {total_guesses} attempts to guess the number.")

while total_guesses > 0:
    guess = int(input("Make a guess: "))
    total_guesses -= 1 #subtract 1 from the total guesses

    if guess == random_number:
        print(f"You got it! The number was {random_number}.")
        break
    elif guess > random_number:
        print("Too high.")
    else:
        print("Too low.")

    if total_guesses > 0:
        print("Guess again.")
    else:
        print(f"You ran out of guesses! The number was {random_number}.")
