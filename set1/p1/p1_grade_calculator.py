# Name : Juliana Marie D. Espenocilla
# Section :  4-BSIT C
# Activity: P1 - Student Grade Calculator
# Date :  November 2026

grades = []


def enter_grades():
    grades.clear()

    for i in range(5):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be from 0 to 100.")

            except ValueError:
                print("Invalid input. Try again.")


def get_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades):
    average = get_average(grades)

    if average >= 75:
        return "PASS"
    else:
        return "FAIL"


while True:
    print("\n----- MENU -----")
    print("1. Enter Grades")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        enter_grades()

    elif choice == "2":
        if len(grades) == 0:
            print("No grades entered.")
        else:
            print("\nRESULTS")
            print("Average:", get_average(grades))
            print("Highest:", get_highest(grades))
            print("Lowest:", get_lowest(grades))
            print("Status:", get_status(grades))

    elif choice == "3":
        print("Program Ended")
        break

    else:
        print("Invalid choice")


# A global variable is created outside functions and can be used in different parts of the program.
# In this program, grades is global so the menu can use the grades entered by enter_grades().
# A local variable is created inside a function and can only be used there.
# For example, average inside get_status() is local and is not available in the menu.