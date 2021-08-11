n = int(input())

row_count = 0
done = False

for rows in range(0, n + 2):
    for columns in range(1, 3 * n + 1):
        if row_count == 0:
            for i in range(1, n + 1):
                print(" ", end="")
            print(" | ")
            row_count += 1
            break

        if 0 < row_count < n:
            for j in range(1, n - row_count + 1):
                print(" ", end="")
            for i in range(1, row_count + 1):
                print("*", end="")
            print(" | ", end="")
            for i in range(1, row_count + 1):
                print("*", end="")
            print()
            row_count += 1
            break

        if row_count == n:
            for i in range(1, n + 1):
                print("*", end="")
            print(" | ", end="")
            for i in range(1, n + 1):
                print("*", end="")
            done = True
            break
    if done:
        break
