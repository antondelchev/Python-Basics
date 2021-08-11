a_num = int(input())
b_num = int(input())
max_num_of_passwords = int(input())

counter = 0

max_reps = a_num * b_num
counter_2 = 0

current_one = 35
current_two = 64

for one in range(current_one, 56):
    current_one = one
    for two in range(current_two, 97):
        current_two = two
        for three in range(1, a_num + 1):
            for four in range(1, b_num + 1):
                first = chr(current_one)
                second = chr(current_two)

                if counter < max_num_of_passwords:
                    print(f"{first}{second}{three}{four}{second}{first}", end="|")
                    counter += 1
                else:
                    quit(0)

                counter_2 += 1
                if counter_2 == max_reps:
                    quit(0)

                current_one += 1
                current_two += 1

                if current_one > 55:
                    current_one = 35
                if current_two > 96:
                    current_two = 64
