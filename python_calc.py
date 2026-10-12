def add(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "error! division by 0 is not allowed"
    return a / b


def even_odd(n):
    if n % 2 == 0:
        return "EVEN"
    return "ODD"


def percentage(a, b):
    if b == 0:
        return "error cannot find percentage with b equal 0"
    return (a / b) * 100


while True:
    print("\n=== PYTHON CALCULATOR ===")
    print("1) ADDITION")
    print("2) SUBTRACTION")
    print("3) MULTIPLICATION")
    print("4) DIVISION")
    print("5) CHECK EVEN/ODD")
    print("6) PERCENTAGE")
    print("7) EXIT")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", add(a, b))

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", subtraction(a, b))

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", multiply(a, b))

    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", divide(a, b))

    elif choice == "5":
        n = float(input("Enter a number: "))
        print("Result:", even_odd(n))

    elif choice == "6":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", percentage(a, b))

    elif choice == "7":
        print("Exiting calculator...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")