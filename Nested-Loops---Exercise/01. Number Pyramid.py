n = int(input())

current_number = 1
stop = False

for rows in range(1, n + 1):
    for columns in range(1, rows + 1):
        if current_number > n:
            stop = True
            break
        print(current_number, end=" ")
        current_number += 1
    if stop:
        break
    print()
