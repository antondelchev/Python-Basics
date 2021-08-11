first_num = int(input())
last_num = int(input())

for one in range(first_num, last_num + 1):
    num_1 = one
    for two in range(first_num, last_num + 1):
        num_2 = two
        for three in range(first_num, last_num + 1):
            num_3 = three
            for four in range(first_num, last_num + 1):
                num_4 = four
                if num_1 < num_4:
                    continue

                if (num_2 + num_3) % 2 != 0:
                    continue

                if (num_1 % 2 == 0 and num_4 % 2 != 0) or (num_1 % 2 != 0 and num_4 % 2 == 0):
                    print(f"{num_1}{num_2}{num_3}{num_4}", end=" ")
