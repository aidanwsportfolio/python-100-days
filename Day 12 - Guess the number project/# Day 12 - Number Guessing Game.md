# Day 12 - Number Guessing Game

## Overview
The Number Guessing Game is a command-line Python game where the player attempts to guess a randomly generated number between 1 and 100. The player selects a difficulty level, which determines how many guesses they have to find the correct number before running out of attempts.

This project focuses on loops, conditional logic, randomization, user input, and managing game state throughout multiple rounds of guessing.

---

## Project Instructions
Create a number guessing game where:

- The computer randomly selects a number between 1 and 100
- The player chooses a difficulty level
- Easy mode gives the player 10 guesses
- Hard mode gives the player 5 guesses
- The player receives feedback after each guess
- The game ends when the player guesses correctly or runs out of attempts

---

## Features

- Random number generation
- Easy and hard difficulty modes
- Limited guessing attempts
- High/low feedback after each guess
- Win and lose conditions
- ASCII art title screen using a separate 'art.py' file

---

## My Solution

This project uses Python's 'random' module to generate a secret number between 1 and 100.

The player first selects a difficulty level:

- Easy → 10 guesses
- Hard → 5 guesses

The program then repeatedly asks the player to guess the number. After each incorrect guess, it informs the player whether the guess was too high or too low and decreases the remaining number of attempts.

If the player guesses correctly, the game immediately ends with a victory message. If all attempts are used, the correct answer is revealed.

---

## Concepts Practiced

### Python Fundamentals

- Variables
- Integers
- Strings
- User input
- Printing output

### Conditional Logic

- 'if' statements
- 'elif' statements
- 'else' statements
- Comparison operators

### Loops

- 'while' loops
- Loop control
- Countdown logic

### Randomization

- Importing modules
- Using 'random.randint()'

### Programming Concepts

- State management
- Game loops
- Difficulty selection
- Input-driven program flow
- Win and lose conditions

---

## Example Gameplay

### Easy Mode

    Welcome to the Number Guessing Game!

    I'm thinking of a number between 1 and 100!

    Choose a difficulty.
    Type 'easy' or 'hard':
    easy

    You have 10 attempts to guess the number.

    Make a guess:
    50

    Too low.

    Guess again.

    Make a guess:
    75

    Too high.

    Guess again.

    Make a guess:
    63

    You got it!
    The number was 63.

---

### Losing Example

    You have 5 attempts to guess the number.

    ...

    You ran out of guesses!
    The number was 82.

---

## How to Run

### Requirements

- Python 3 installed
- 'art.py' located in the same folder as the main program
- 'art.py' must contain a variable named 'logo'

### Run the Program

    python number_guessing_game.py

---

## Challenges Faced

One challenge during development was managing the number of remaining guesses while making sure the game stopped immediately after a correct answer.

Another challenge was organizing the game loop so that the player continued receiving feedback after each incorrect guess without repeating unnecessary code.

This project also reinforced:

- loop construction
- game state management
- random number generation
- conditional decision making

---

## What I Learned

Through this project, I learned:

- how to create a complete game loop using a 'while' loop
- how to generate random numbers
- how to manage player attempts
- how to create multiple difficulty settings
- how to provide meaningful feedback to users
- how to terminate a loop using 'break'

I also gained more confidence using:

- conditional logic
- comparison operators
- user interaction
- program flow control

---

## Future Improvements

Potential future upgrades for this project include:

- Allowing the player to play multiple rounds without restarting the program
- Validating user input
- Adding hints based on how close the guess is
- Tracking previous guesses
- Tracking player statistics
- Adding a scoring system
- Adding a leaderboard
- Creating a graphical interface using Tkinter or Pygame
- Creating a web-based version
- Allowing players to choose the number range

---

## Author

Aidan Scott

Part of the 'python-100-days' repository documenting my progress through 100 days of Python development.