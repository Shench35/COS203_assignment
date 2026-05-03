# Task 1: Grade Checker - Single file with functions

def get_score():
    score = float(input("Enter score: "))
    return score

def get_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"

def display_result(score, grade):
    print(f"Score: {score} | Grade: {grade}")

def main():
    score = get_score()
    grade = get_grade(score)
    display_result(score, grade)

main()
