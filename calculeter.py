# CODSOFT Python Internship
# Task 2: Calculator

print("===== SIMPLE CALCULATOR =====")

while True:
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))

    while True:
        print("\nChoose an operation:")
        print("+ for Addition")
        print("- for Subtraction")
        print("* for Multiplication")
        print("/ for Division")

        operation = input("Enter your choice: ")

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2

        else:
            print("Invalid operation! Please try again.")
            continue

        print("Result:", result)

        print("\n1. Perform another operation with the same numbers")
        print("2. Enter new numbers")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            continue
        elif choice == "2":
            break
        elif choice == "3":
            print("Thank you for using the calculator!")
            exit()
        else:
            print("Invalid choice! Starting with new numbers.")
            break