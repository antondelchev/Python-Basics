number_one = int(input())
number_two = int(input())

for first in range(1, number_one + 1):
    first_symbol = first
    for second in range(1, number_one + 1):
        second_symbol = second
        for third in range(97, 97 + number_two):
            third_symbol = chr(third)
            for fourth in range(97, 97 + number_two):
                fourth_symbol = chr(fourth)
                for fifth in range(1, number_one + 1):
                    if fifth > first_symbol and fifth > second_symbol:
                        fifth_symbol = fifth
                        print(f"{first_symbol}{second_symbol}{third_symbol}{fourth_symbol}{fifth_symbol}", end=" ")
