# Day 02 - Tip Calculator

## Project Instructions
Create a program that calculates how much each person should pay when splitting a bill, including a selected tip percentage.

The program should:
- Ask for the total bill amount
- Ask for the desired tip percentage
- Ask how many people are splitting the bill
- Calculate the final amount each person should pay

---

## My Solution
This program takes user input for the bill total, tip percentage, and number of people splitting the bill. It converts the tip percentage into a decimal, calculates the total tip amount, adds it to the bill, and divides the final total evenly among the group.

The final amount is formatted using an f-string to always display two decimal places for proper currency formatting.

---

## Concepts Practiced
- Variables
- User input
- Data type conversion
- Mathematical operations
- Floating point numbers
- f-strings
- Formatting decimal values

---

## Example Output

```text
Welcome to the tip calculator!
What was the total bill? $150
What percentage tip would you like to give? 10 12 15 12
How many people to split the bill? 5
Each person should pay $33.60