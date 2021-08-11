import sys

number_of_pairs = int(input())

max_pair_sum = -sys.maxsize
min_pair_sum = sys.maxsize
difference_with_previous = 0
current = 0

for i in range(1, number_of_pairs + 1):
    pair_first_number = int(input())
    pair_second_number = int(input())
    current_pair_sum = pair_first_number + pair_second_number

    if current_pair_sum > max_pair_sum:
        difference_with_previous = current_pair_sum - current
        max_pair_sum = current_pair_sum
    else:
        difference_with_previous = current - current_pair_sum
        min_pair_sum = current_pair_sum

    if max_pair_sum != current_pair_sum:
        current = min_pair_sum
    else:
        current = max_pair_sum

if number_of_pairs == 1:
    print(f"Yes, value={max_pair_sum}")
else:
    if max_pair_sum == min_pair_sum:
        print(f"Yes, value={max_pair_sum}")
    else:
        print(f"No, maxdiff={difference_with_previous}")
