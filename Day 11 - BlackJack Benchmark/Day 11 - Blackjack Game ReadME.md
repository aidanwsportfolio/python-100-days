# Day 11 - Blackjack Game

## Overview
This project is a command-line Blackjack game built with Python. The player competes against the computer by drawing cards and trying to reach a score as close to 21 as possible without going over.

The game includes card dealing, score calculation, Blackjack detection, Ace handling, computer drawing logic, replay functionality, and outcome comparison.

---

## Project Instructions
Create a simplified Blackjack game where:

- The player and computer each begin with two cards
- The player can choose to draw another card or pass
- The computer continues drawing until reaching a score of at least 17
- Aces can count as either 11 or 1
- A two-card score of 21 counts as Blackjack
- The game determines whether the player wins, loses, or draws
- The player can choose to play again after each round

---

## Features

- Random card dealing
- Player and computer hands
- Blackjack detection
- Ace adjustment from 11 to 1
- Bust detection
- Computer drawing rules
- Win, loss, and draw outcomes
- Replay functionality
- ASCII art logo support through a separate `art.py` file

---

## My Solution
This project separates the game into multiple functions so that each part of the Blackjack logic has a specific responsibility.

The `deal_card()` function returns a randomly selected card from the card list.

The `calculate_score()` function totals the cards in a hand and handles special Blackjack rules. A two-card score of 21 returns `0`, which is used to represent Blackjack. The function also changes an Ace from 11 to 1 when the total score would otherwise exceed 21.

The `compare()` function determines the final game result by checking for:

- Player Blackjack
- Computer Blackjack
- Player bust
- Computer bust
- Higher player score
- Higher computer score
- Draws

The `play_game()` function controls the overall game flow. It creates the hands, deals the initial cards, displays the player's cards and the computer's first card, asks whether the player wants another card, runs the computer's turn, and compares the final scores.

The game also includes a replay loop so the player can begin another round after finishing the current one.

---

## Concepts Practiced

### Python Fundamentals
- Variables
- Lists
- Functions
- Return values
- User input
- Printing output
- Conditional statements
- Loops

### Functions
- Defining reusable functions
- Returning values
- Passing arguments
- Separating program responsibilities
- Calling functions from other functions

### Lists
- Creating card hands
- Appending new cards
- Removing and replacing values
- Checking whether a value exists in a list
- Calculating totals with `sum()`

### Randomization
- Importing the `random` module
- Using `random.choice()`
- Simulating random card draws

### Conditional Logic
- `if` statements
- `elif` statements
- `else` statements
- Nested conditions
- Compound Boolean expressions
- Special-case handling

### Loops
- `while` loops
- Continuing the player's turn
- Controlling the computer's drawing behavior
- Repeating the entire game

### Game Development Concepts
- Turn-based game flow
- State management
- Win and loss conditions
- Replay systems
- Hidden computer information
- Rule-based decision making

---

## Blackjack Rules Used

This version of Blackjack uses the following simplified rules:

- Number cards are worth their displayed value
- Face cards are worth 10
- Aces initially count as 11
- If the score exceeds 21, an Ace can change from 11 to 1
- A two-card score of 21 is treated as Blackjack
- The player loses if their score exceeds 21
- The computer draws cards until reaching at least 17
- The hand closest to 21 wins
- Equal scores result in a draw

---

## Example Gameplay

    Do you want to play a game of blackjack?: 'y' or 'n'
    y

    Your Cards: [10, 7], Current Score: 17
    Computer's First Card: 9

    Type 'y' to get another card, type 'n' to pass:
    n

    Your final hand: [10, 7], final score: 17
    Computer's final hand: [9, 6, 8], final score: 23

    You Win!

---

## Blackjack Example

    Your final hand: [11, 10], final score: 0
    Computer's final hand: [10, 9], final score: 19

    You Win!

In this program, a score of `0` represents Blackjack.

---

## Ace Handling
An Ace starts with a value of 11. If the total score goes over 21, the program replaces one Ace valued at 11 with an Ace valued at 1.

This is handled with:

    while 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)

This allows hands containing an Ace to avoid busting when possible.

---

## How to Run

### Requirements
- Python 3 installed
- `art.py` located in the same folder as the main program
- `art.py` must contain a variable named `logo`

### Run the Program

    python blackjack.py

---

## Challenges Faced
One of the main challenges in this project was managing the different possible game states.

The program needed to correctly handle:

- Natural Blackjack
- Multiple card draws
- Player busts
- Computer busts
- Ace value changes
- Computer drawing behavior
- Immediate game endings
- Replay logic

Another challenge was keeping score calculations accurate after every new card was added.

This project also reinforced the importance of breaking a larger program into smaller functions instead of placing all of the logic in one block.

---

## What I Learned
Through this project, I learned:

- how to organize a larger Python program with functions
- how to use return values to communicate between functions
- how to manage changing game data with lists
- how to create random card draws
- how to model simplified Blackjack rules
- how to handle special cases such as Blackjack and Aces
- how to compare multiple possible outcomes
- how to use loops to control turns and replay the game
- how to stop a function early with `return`

I also gained more experience debugging game flow and making sure later parts of the program only run when the game has not already ended.

---

## Future Improvements
Potential future upgrades for this project include:

- Refactoring repeated score calculations
- Allowing the player to draw multiple times with a new prompt after each card
- Improving the computer drawing logic
- Adding multiple players
- Adding betting and chip balances
- Adding card suits and full card names
- Using a real 52-card deck without unlimited replacement
- Adding input validation
- Adding clearer screen transitions
- Adding a score history
- Building a graphical version with Tkinter or Pygame
- Creating a web-based version
- Adding automated tests for the scoring functions

---

## Author

Aidan Scott

Part of the `python-100-days` repository documenting my progress through 100 days of Python development.