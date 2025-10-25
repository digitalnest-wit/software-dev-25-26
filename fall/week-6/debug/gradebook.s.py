# Student Grade System (BUGGY VERSION)

def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

def get_letter_grade(average: float):
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade


def calculate_weighted_grade(homework: float, tests: float, final: float):
    weighted = (homework * 0.3) + (tests * 0.5) + (final * 0.2)
    return weighted

def is_passing(grade: float):
    passing_grade = 60
    if grade > passing_grade:
        return True
    else:
        return False

def display_report(name: str, average: float, letter: str):
    grade_status = "passing" if is_passing(average) else "failing"
    print(f"\nStudent Report for {name}")
    print(f"Average: {average}")
    print(f"Letter Grade: {letter}")
    print(f"Status: {grade_status}")


# Main program
print("Student Grade System")
print("====================")

student_name = input("Enter student name: ")

homework_score = float(input("Enter homework score (0-100): "))
test_score = float(input("Enter test score (0-100): "))
final_score = float(input("Enter final exam score (0-100): "))

final_average = calculate_weighted_grade(final=final_score, homework=homework_score, tests=test_score)

letter_grade = get_letter_grade(final_average)

display_report(student_name, final_average, letter_grade)

passing_grade = 70
if is_passing(final_average):
    print(f"\nCongratulations! {student_name} is passing with a {passing_grade}%")
else:
    print(f"\n{student_name} needs improvement.")
