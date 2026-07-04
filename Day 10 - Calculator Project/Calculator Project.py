import art
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
#func
def calculate():
    print(art.logo)
    n1 = float(input("Please type in the first number?: "))
    for symbol in operator:
        print(symbol)
    operator_choice = input("Please type in an operator: ")
    n2 = float(input("Please type in the second number?: "))
    result =operator[operator_choice](n1, n2)

    if operator_choice in operator:
        print(f"{n1} {operator_choice} {n2} = {result}")
        continue_working = input("Would you like to continue? (y/n): ")
        while continue_working == "y":
            print("\n" * 20)
            n1 = result
            for symbol in operator:
                print(symbol)
            operator_choice = input("Please type in an operator: \n")
            n2 = float(input("Please type in the second number?: "))
            result =operator[operator_choice](n1, n2)
            if operator_choice in operator:
                print(f"{n1} {operator_choice} {n2} = {result}")
                continue_working = input("Would you like to continue? (y/n): ")
        if continue_working == "n":
            print("Thank you for using this program")
        else:
            continue_working = input("Please enter either 'y' or 'n'\n")
calculate()


