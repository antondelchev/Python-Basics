upper_limit_hundreds = int(input())
upper_limit_tens = int(input())
upper_limit_singles = int(input())

for i in range(1, upper_limit_hundreds + 1):
    for j in range(2, upper_limit_tens + 1):
        counter = 0
        for num in range(1, j + 1):
            if j % num == 0:
                counter += 1
        for k in range(1, upper_limit_singles + 1):
            if i % 2 == 0 and k % 2 == 0:
                one = i
                two = j
                three = k
                if counter <= 2:
                    print(f"{one} {two} {three}")
