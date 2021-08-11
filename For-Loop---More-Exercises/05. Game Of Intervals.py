rounds_number = int(input())

range_one = 0
range_two = 0
range_three = 0
range_four = 0
range_five = 0
invalid_numbers = 0

score = 0

for i in range(1, rounds_number + 1):
    number = int(input())
    if 0 <= number <= 9:
        range_one += 1
        score += 0.2 * number
    elif 10 <= number <= 19:
        range_two += 1
        score += 0.3 * number
    elif 20 <= number <= 29:
        range_three += 1
        score += 0.4 * number
    elif 30 <= number <= 39:
        range_four += 1
        score += 50
    elif 40 <= number <= 50:
        range_five += 1
        score += 100
    else:
        invalid_numbers += 1
        score = score / 2

first_range_number_percent = range_one / rounds_number * 100
second_range_number_percent = range_two / rounds_number * 100
third_range_number_percent = range_three / rounds_number * 100
fourth_range_number_percent = range_four / rounds_number * 100
fifth_range_number_percent = range_five / rounds_number * 100
invalid_number_percent = invalid_numbers / rounds_number * 100

print(f"{score:.2f}")
print(f"From 0 to 9: {first_range_number_percent:.2f}%")
print(f"From 10 to 19: {second_range_number_percent:.2f}%")
print(f"From 20 to 29: {third_range_number_percent:.2f}%")
print(f"From 30 to 39: {fourth_range_number_percent:.2f}%")
print(f"From 40 to 50: {fifth_range_number_percent:.2f}%")
print(f"Invalid numbers: {invalid_number_percent:.2f}%")
