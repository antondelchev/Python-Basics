students_attended = int(input())

students_b_grade = 0
students_c_grade = 0
students_d_grade = 0
students_f_grade = 0

grades_total = 0

for i in range(1, students_attended + 1):
    grade = float(input())
    if grade < 3.0:
        students_f_grade += 1
        grades_total += grade
    elif 3 <= grade <= 3.99:
        students_d_grade += 1
        grades_total += grade
    elif 4 <= grade <= 4.99:
        students_c_grade += 1
        grades_total += grade
    elif 5 <= grade <= 6:
        students_b_grade += 1
        grades_total += grade

students_b_grade_percent = students_b_grade / students_attended * 100
students_c_grade_percent = students_c_grade / students_attended * 100
students_d_grade_percent = students_d_grade / students_attended * 100
students_f_grade_percent = students_f_grade / students_attended * 100
average_grade = grades_total / students_attended

print(f"Top students: {students_b_grade_percent:.2f}%")
print(f"Between 4.00 and 4.99: {students_c_grade_percent:.2f}%")
print(f"Between 3.00 and 3.99: {students_d_grade_percent:.2f}%")
print(f"Fail: {students_f_grade_percent:.2f}%")
print(f"Average: {average_grade:.2f}")
