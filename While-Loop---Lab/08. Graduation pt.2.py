name = input()

current_class = 1
grade_score_total = 0
poor_grades_counter = 0

while current_class < 13:
    current_grade = float(input())
    if current_grade < 4:
        poor_grades_counter += 1
        if poor_grades_counter > 1:
            break
        current_class -= 1
        grade_score_total += current_grade
    else:
        current_class += 1
        grade_score_total += current_grade

average_success = grade_score_total / 12

if current_class == 13:
    print(f"{name} graduated. Average grade: {average_success:.2f}")
else:
    print(f"{name} has been excluded at {current_class + 1} grade")
