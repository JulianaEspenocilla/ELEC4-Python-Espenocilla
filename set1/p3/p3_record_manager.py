# Name: Juliana Marie D. Espenocilla
# Section: 4-BSIT C
# Activity: P3 - Student Record Manager
# Date: November 2026

students = []


def add_student():
    name = input("Enter student name: ").strip()

    for student in students:
        if student.lower() == name.lower():
            print("Student already exists.")
            return

    students.append(name)
    print("Student added successfully.")


def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            print("Student removed.")
            return

    print("Student not found.")


def search_student():
    keyword = input("Search name: ").strip().lower()

    found = []

    for student in students:
        if keyword in student.lower():
            found.append(student)

    if found:
        print("\nSearch Results:")
        for student in found:
            print(student)
    else:
        print("No student found.")


def display_students():
    if len(students) == 0:
        print("No students in the list.")
        return

    print("\nStudent List")

    sorted_students = sorted(students)

    for i, student in enumerate(sorted_students, start=1):
        print(f"{i}. {student}")

    print("Total Students:", len(sorted_students))


while True:
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        remove_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid choice")


# List and Set Explanation
# A list can store multiple values and keeps the order
# in which items are added. In this program, the student
# names are stored in a list. A set is used when unique
# values are needed because it automatically prevents
# duplicates. I used a list here and manually checked
# for duplicates before adding a student.