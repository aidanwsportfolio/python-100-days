# Day 03 - Treasure Island

## Overview
Treasure Island is a text-based adventure game created in Python where the player must make a series of choices in order to survive and find hidden treasure. Each decision changes the outcome of the game, leading either to victory or to a game over scenario.

This project focuses heavily on conditional logic, nested decision trees, and program flow control while also introducing basic game design concepts.

---

## Project Instructions
Create a text-based game where the player navigates through different choices to reach hidden treasure.

The game should:
- Ask the player to make decisions at multiple stages
- Use conditional statements to determine outcomes
- End the game when incorrect choices are made
- Allow the player to win if the correct sequence is chosen

---

## Features
- Multiple decision paths
- Several unique game over endings
- Winning path with treasure discovery
- ASCII art introduction screen
- Interactive user input system
- Nested branching story structure

---

## My Solution
This program uses nested `if`, `elif`, and `else` statements to guide the player through different story branches. The game begins with an introductory ASCII art screen before prompting the player to make directional choices.

The player must:
1. Choose the correct direction
2. Decide whether to swim or wait
3. Choose the correct door

Incorrect choices trigger different losing scenarios, while the correct sequence leads to victory.

The project also demonstrates:
- Proper nesting of conditional statements
- Handling invalid user input
- Logical branching
- Interactive storytelling using Python

---

## Concepts Practiced

### Python Fundamentals
- Variables
- Strings
- User input
- Printing output

### Conditional Logic
- `if` statements
- `elif` statements
- `else` statements
- Nested conditionals
- Boolean logic

### Programming Concepts
- Program flow control
- Decision trees
- Input validation
- Interactive applications

### Additional Features
- ASCII art formatting
- Text-based game structure
- Scenario branching

---


### What I learned

Through this project, I learned:

- how nested conditional statements work
- how program flow changes based on user decisions
- how to debug logic and indentation errors
- how to structure a simple interactive game in Python

#### I also gained more confidence using:

- Boolean expressions
- user input handling
- branching logic

### Challenges Faced

One of the main challenges during development was properly nesting conditional statements so that later choices only appeared if the player survived previous stages.

This project helped reinforce:

- indentation structure
- nested logic flow
- debugging conditional branches

### Future Improvements
- Adding more story branches and endings
- Adding an inventory system
- Adding health points or lives
- Allowing full text commands instead of single letters
- Adding replay functionality
- Adding randomized events
- Building a GUI version using Tkinter or Pygame
- Creating a web-based version using Flask
