screening_type = input()
rows = int(input())
columns = int(input())
total_income = 0

total_spaces = rows * columns

if screening_type == "Premiere":
    total_income = total_spaces * 12
elif screening_type == "Normal":
    total_income = total_spaces * 7.5
elif screening_type == "Discount":
    total_income = total_spaces * 5

print(f"{total_income:.2f} leva")
