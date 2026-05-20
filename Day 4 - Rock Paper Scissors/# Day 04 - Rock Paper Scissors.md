# Day 04 - Rock Paper Scissors

## Overview
Rock Paper Scissors is a text-based Python game where the player competes against the computer in the classic hand game. The player selects either Rock, Paper, or Scissors, and the computer randomly generates its own choice to determine the outcome.

This project focuses on conditional logic, randomization, user interaction, and game flow control while also incorporating ASCII art for a more engaging experience.

---

## Project Instructions
Create a Rock Paper Scissors game where:
- The user chooses Rock, Paper, or Scissors
- The computer randomly selects its choice
- The program determines whether the player wins, loses, or ties
- ASCII art is displayed for both choices

---

## Features
- Interactive user input system
- Random computer opponent
- ASCII art representations of Rock, Paper, and Scissors
- Win, lose, and tie outcomes
- Multiple conditional game paths
- Input validation for invalid options

---

## My Solution
This project uses Python conditionals and the `random` module to simulate a Rock Paper Scissors match between the player and the computer.

The user selects:
- `0` for Rock
- `1` for Paper
- `2` for Scissors

The computer then randomly generates its own selection using:

    random.randint(0, 2)

The program compares both choices and determines the game result using conditional logic.

ASCII art is printed to visually represent each move, creating a more interactive and polished terminal experience.

---

## Concepts Practiced

### Python Fundamentals
- Variables
- Strings
- Integers
- User input
- Printing output

### Conditional Logic
- `if` statements
- `elif` statements
- `else` statements
- Nested conditionals

### Randomization
- Importing modules
- Using Python's `random` module
- Generating random integers

### Game Development Concepts
- Game flow control
- Decision-based outcomes
- User interaction
- Input handling

### Additional Features
- ASCII art formatting
- Text-based game structure

---

## Example Gameplay

### Winning Example

    What do you choose?
    Type 0 for Rock, 1 for Paper, and 2 for Scissors:
    0

    You chose
    ROCK ASCII ART

    Computer Chose
    SCISSORS ASCII ART

    You Win!

---

### Tie Example

    What do you choose?
    Type 0 for Rock, 1 for Paper, and 2 for Scissors:
    1

    You chose
    PAPER ASCII ART

    Computer Chose
    PAPER ASCII ART

    Tie!

---

### Invalid Input Example

    invalid option

---

## How to Run

### Requirements
- Python 3 installed

### Run the Program

    python rock_paper_scissors.py

---

## Challenges Faced
One challenge during development was organizing all of the game outcomes logically while avoiding conflicting conditions.

This project also reinforced:
- how to structure game logic
- how to use random number generation
- how to compare multiple outcomes
- how to debug conditional branches

---

## What I Learned

Through this project, I learned:
- how to use Python's `random` module
- how to simulate a computer opponent
- how to structure multiple game outcomes
- how to improve terminal applications with ASCII art
- how to manage user choices and branching logic

I also gained more confidence using:
- nested conditionals
- program flow control
- interactive game mechanics

---

## Future Improvements

Potential future upgrades for this project include:
- Adding replay functionality
- Adding score tracking
- Adding multiplayer support
- Refactoring repetitive logic into functions
- Using lists to simplify choice handling
- Adding better input validation
- Building a GUI version using Tkinter or Pygame
- Creating an online multiplayer version

---

## Author

Aidan Scott

Part of the `python-100-days` repository documenting my progress through 100 days of Python development.