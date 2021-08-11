import math

income = float(input())
grade_score = float(input())
min_wage = float(input())
scholarship = 0
social_scholarship = 0

if grade_score <= 4.5:
    print("You cannot get a scholarship!")

if income > min_wage and grade_score < 5.5:
    print("You cannot get a scholarship!")

if income > min_wage and grade_score <= 4.5:
    print("You cannot get a scholarship!")

if income == min_wage and grade_score < 5.5:
    print("You cannot get a scholarship!")

if income < min_wage and grade_score >= 5.5:
    social_scholarship = min_wage * 0.35
    scholarship = grade_score * 25
    if social_scholarship == scholarship:
        print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")
    elif social_scholarship > scholarship:
        print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
    else:
        print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")
elif income < min_wage and grade_score > 4.5:
    social_scholarship = min_wage * 0.35
    print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
elif grade_score >= 5.5:
    scholarship = grade_score * 25
    print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")
