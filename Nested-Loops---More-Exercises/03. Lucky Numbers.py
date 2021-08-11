number = int(input())

for one in range(1, 10):
    first = one
    for two in range(1, 10):
        second = two
        sum_first_pair = first + second
        for three in range(1, 10):
            third = three
            for four in range(1, 10):
                fourth = four
                sum_second_pair = third + fourth
                if sum_first_pair == sum_second_pair and number % sum_first_pair == 0:
                    print(f"{first}{second}{third}{fourth}", end=" ")
