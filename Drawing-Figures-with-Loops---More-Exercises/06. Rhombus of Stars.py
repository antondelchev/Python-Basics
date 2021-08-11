n = int(input())

row_count = 1
done = False

for rows in range(1, n * 2):
    if row_count > n * 2 - 1:
        break
    for columns in range(1, row_count + 1):

        if row_count == 1:
            for i in range(1, n):
                print(" ", end="")
            print("*", end="")
            print()
            row_count += 1
            break

        elif 1 < row_count < n:
            for i in range(row_count, n):
                print(" ", end="")
            for j in range(1, row_count + 1):
                print("*", end=" ")
            row_count += 1
            print()
            break

        elif row_count == n:
            for i in range(1, n + 1):
                print("*", end=" ")
            print()
            row_count += 1
            break

        elif n < row_count < n * 2 - 1:
            for i in range(n, row_count):
                print(" ", end="")
            for j in range(row_count - n, n):
                print("*", end=" ")
            row_count += 1
            print()
            break

        elif row_count == n * 2 - 1:
            for i in range(1, n):
                print(" ", end="")
            print("*", end="")
            done = True
            break
    if done:
        break
