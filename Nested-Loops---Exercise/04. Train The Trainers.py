judges_number = int(input())
presentation_name = input()

grade_sum_all_presentations = 0
presentations_number = 0

while presentation_name != "Finish":
    total_score = 0
    for i in range(1, judges_number + 1):
        grade = float(input())
        total_score += grade
    average_score = total_score / judges_number
    grade_sum_all_presentations += total_score
    presentations_number += 1
    print(f"{presentation_name} - {average_score:.2f}.")
    presentation_name = input()

average_assessment = grade_sum_all_presentations / (presentations_number * judges_number)
if presentation_name == "Finish":
    print(f"Student's final assessment is {average_assessment:.2f}.")
