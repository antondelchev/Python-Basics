number = int(input())

counter = 0

for x_one in range(0, number + 1):
    for x_two in range(0, number + 1):
        for x_three in range(0, number + 1):
            if x_one + x_two + x_three == number:
                counter += 1

print(counter)
