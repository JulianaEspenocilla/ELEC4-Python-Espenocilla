# Name: Juliana Marie D. Espenocilla
# Section: 4-BSIT C
# Activity: P2 - student_utils
# Date: November 2026

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