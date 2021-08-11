start_number = int(input())

for i in range(1111, 10000):
    less_digits_or_division_by_zero = False
    num_as_str = str(i)
    for index, number in enumerate(num_as_str):
        counter = 4
        if int(number) > 0:
            if start_number % int(number) != 0:
                counter -= 1
            if counter < 4 or int(number) < 0:
                less_digits_or_division_by_zero = True
                break
        else:
            less_digits_or_division_by_zero = True
            break
    if not less_digits_or_division_by_zero:
        print(i, end=" ")
