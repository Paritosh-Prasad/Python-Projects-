# Basic Calculator project no 06

def add(a, b) :
    return a + b

def subtract(a, b) :
    return a - b

def multiply(a, b) :
    return a * b

def divide(a, b) :
    if b == 0 :
        return "Error! Division by zero."
    return a / b

continued = False

while continued == False :
    print("Select operation\n")
    print("1 for Addition.\n2 for Subtraction.\n3 for multiplication.\n4 for division.\n")

    choice = int(input("Enter choice (1/2/3/4) :"))

    num1 = float(input("Enter first number :" ))
    num2 = float(input("Enter second number :" ))


    if choice == 1 :
        print(add(num1, num2))
    elif choice == 2 :
        print(subtract(num1, num2))
    elif choice == 3 :
        print(multiply(num1, num2))
    elif choice == 4 :
        print(divide(num1, num2))
    else :
        print("Invalid input !!!!!!")

    cont = input("You want to continue use of calculator (Y/N) :\n").lower()
    if cont == "y" :
        continued = False
    else :
        print("EXITING CALCULATOR NOW !!!!!!!")
        continued = True

