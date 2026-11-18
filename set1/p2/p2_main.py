# Name: Juliana Marie D. Espenocilla
# Section: 4-BSIT C
# Activity: P2 - custom module
# Date: November 2026

import student_utils
from student_utils import get_status
from datetime import datetime

grades = []

print("===== STUDENT GRADE REPORT =====")

for i in range(5):
    while True:
        try:
            grade = float(input(f"Enter Grade {i + 1}: "))

            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Enter a number.")

print("\n===== RESULTS =====")
print("Average:", student_utils.get_average(grades))
print("Highest:", student_utils.get_highest(grades))
print("Lowest:", student_utils.get_lowest(grades))
print("Status:", get_status(grades))

print("\nReport Generated:")
print(datetime.now())