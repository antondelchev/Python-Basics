first_num_upper_limit = int(input())
second_num_upper_limit = int(input())
third_num_upper_limit = int(input())

for first in range(1, first_num_upper_limit + 1):
    if first % 2 != 0:
        continue
    else:
        first_num = first
    for second in range(2, second_num_upper_limit + 1):
        counter = 0
        second_num = 0
        for i in range(1, second + 1):
            if second % i == 0:
                counter += 1
            if counter > 2:
                continue
        if counter <= 2:
            second_num = second
        if second_num == 0:
            continue
        for third in range(1, third_num_upper_limit + 1):
            if third % 2 != 0:
                continue
            else:
                third_num = third
                print(f"{first_num} {second_num} {third_num}")
