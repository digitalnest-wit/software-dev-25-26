# Student Grade System

def calculate_average(scores: list[int]) -> float:
    total = sum(scores)
    average = total / len(scores)    
    return average

def get_letter_grade(average: float) -> str:
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

def calculate_weighted_grade(homework: float, tests: float, final: float) -> float:
    weighted = (homework * 0.3) + (tests * 0.5) + (final * 0.2)
    return weighted

def is_passing(grade: float) -> bool:
    passing_grade = 60
    if grade > passing_grade:
        return True
    else:
        return False

def display_report(name: str, average: float, letter: str) -> None:
    if is_passing(average):
        grade_status = "passing" 
    else:
        grade_status = "failing"
    
    print(f"\nStudent Report for {name}")
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {letter}")
    print(f"Status: {grade_status}")


# Main program
print("Student Grade System")
print("====================")

student_name = input("Enter student name: ")

homework_score = float(input("Enter homework score (0-100): "))
test_score = float(input("Enter test score (0-100): "))
final_score = float(input("Enter final exam score (0-100): "))

final_average = calculate_weighted_grade(homework_score, test_score, final_score)

letter_grade = get_letter_grade(final_average)

display_report(student_name, final_average, letter_grade)

if is_passing(final_average):
    print(f"\nCongratulations! {student_name} is passing with a {final_average:.2f}%")
else:
    print(f"\n{student_name} needs improvement.")
