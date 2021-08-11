n = int(input())

for rows in range(1, n + 1):
    for columns in range(1, n + 1):
        if rows == 1 or rows == n:
            print("+", end=" ")

            for i in range(1, n - 1):
                print("-", end=" ")

            print("+")
            break
        else:
            print("|", end=" ")

            for i in range(1, n - 1):
                print("-", end=" ")

            print("|")
            break
