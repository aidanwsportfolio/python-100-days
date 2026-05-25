import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

new_password_list = [] #create new list to fill
for i in range(0, nr_letters): #for every item in the range 0 to nr_letters
    new_password_list.append(random.choice(letters)) #add a random item to new_password list

    '''the above logic applies to symbols, along with numbers'''

for i in range(0, nr_symbols):#for every item in the range 0 to however many in nr_symbols
    new_password_list.append(random.choice(symbols)) #add a random symbol to the new password list

for i in range(0, nr_numbers): #for every item in the range 0 to however many in nr_numbers
    new_password_list.append(random.choice(numbers)) #add a random number to the new password list

print(new_password_list) #print the original list
random.shuffle(new_password_list) #shuffle the list
print(new_password_list) #print the shuffled list

password = "" #same as "".join
for i in new_password_list:
    password += i

print(f"Your generated password is: {password}")

