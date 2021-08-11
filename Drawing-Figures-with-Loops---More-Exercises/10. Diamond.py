n = int(input())

row_counter = 0
counter_2 = 0
counter_3 = 0

top_done = False
bottom_done = False

current_row = 0

max_lines_top_even = int(n / 2) - 1
start_lines_for_bottom_even = 1

max_lines_odd = int(n / 2) + 1
start_lines_for_bottom_odd = 1
odd_lines = 3
odd_lines_less = n - 4
max_odd_limit = max_lines_odd

# number of rows
if n > 2:
    row_counter = 3
    for i in range(3, n + 1, 2):
        if i != 3 and i != 4:
            row_counter += 2

elif n <= 2:
    row_counter = 1

# drawing
for row in range(1, row_counter + 1):
    current_row += 1
    for columns in range(1, n + 1):
        row_done = False
        # n <= 2
        if n % 2 == 0 and n <= 2:
            print("**", end="")
            print()
            row_done = True
            break
        elif n % 2 != 0 and n <= 2:
            print("*", end="")
            print()
            row_done = True
            break

        # n > 2
        if n > 2:
            # top even
            if n % 2 == 0:
                if not top_done:
                    for i in range(1, max_lines_top_even + 1):
                        print("-", end="")
                    print("*", end="")
                    for i in range(0, row - 1):
                        print("--", end="")
                    print("*", end="")
                    for i in range(1, max_lines_top_even + 1):
                        print("-", end="")
                    print()
                    max_lines_top_even -= 1
                    counter_2 += 1
                    row_done = True

                if counter_2 == int(n / 2):
                    top_done = True
                    start_lines_for_next = 1

            # top odd
            else:
                if counter_2 < int(n / 2) + 1:
                    for i in range(1, max_lines_odd):
                        print("-", end="")
                    print("*", end="")
                    if row == 2:
                        print("-", end="")
                    if row > 2:
                        for j in range(1, odd_lines + 1):
                            print("-", end="")
                        odd_lines += 2
                    if counter_2 >= 1:
                        print("*", end="")
                    for i in range(1, max_lines_odd):
                        print("-", end="")
                    print()
                    max_lines_odd -= 1
                    counter_2 += 1
                    row_done = True

                if counter_2 == int(n / 2) + 1:
                    top_done = True

            # bottom even
            if n % 2 == 0:
                if top_done:
                    for i in range(1, start_lines_for_bottom_even + 1):
                        print("-", end="")
                    print("*", end="")
                    for i in range(row + 1, n - 1):
                        print("--", end="")
                    print("*", end="")
                    for i in range(1, start_lines_for_bottom_even + 1):
                        print("-", end="")
                    print()
                    start_lines_for_bottom_even += 1
                    counter_3 += 1
                    row_done = True

                if counter_3 == int(n / 2) - 1:
                    bottom_done = True

            # bottom odd
            else:
                if top_done:
                    for i in range(1, start_lines_for_bottom_odd + 1):
                        print("-", end="")
                    print("*", end="")
                    if current_row == n - 2:
                        print("-", end="")
                        print("*", end="")
                    elif current_row != n - 2 and current_row != n - 1:
                        for j in range(1, odd_lines_less + 1):
                            print("-", end="")
                        print("*", end="")
                        odd_lines_less -= 2
                    for i in range(1, start_lines_for_bottom_odd + 1):
                        print("-", end="")
                    print()
                    start_lines_for_bottom_odd += 1
                    counter_3 += 1
                    row_done = True

                if counter_3 == int(n / 2):
                    bottom_done = True
        if row_done:
            break

    if top_done and bottom_done:
        break
