# Name: Juliana Marie D. Espenocilla
# Section: 4-BSIT C
# Activity: P4 - Safe Menu Program
# Date: November 2026

while True:
    print("\n===== MENU =====")
    print("1. Division")
    print("2. Open File")
    print("3. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = num1 / num2

        elif choice == "2":
            filename = input("Enter file name: ")

            file = open(filename, "r")
            content = file.read()

        elif choice == "3":
            print("Program Ended")
            break

        else:
            raise ValueError("Invalid Menu choice.")

    

    finally:
        print("Operation completed.")