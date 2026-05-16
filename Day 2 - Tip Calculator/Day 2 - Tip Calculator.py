print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percentage_of_tip = tip / 100 #the percentage of tip represented as a base 10 decimal
total_tip = bill * percentage_of_tip #the total tip amount is the bill divided by the selected percentage of the tip
total_bill = bill + total_tip # the total bill is the bill plus the tip
splited_bill = total_bill / people #the individual split of the bill is the bill divided by the amount of people

print(f"Each person should pay ${splited_bill:.2f}")
'''this prints the data above with an f string so I can directly import
the splitted_bill variable, and format the float to round to 2 decimal places.
I could've also used the round function "round(splitted_bill, 2)" to achieve the 
same result.'''
