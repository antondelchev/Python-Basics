n = int(input())

bridge_position_odd = (n + 1) / 2
bridge_position_even = (n / 2)

for rows in range(1, n + 1):
    for columns in range(1, 5 * n + 1):
        # top
        if rows == 1:
            for i in range(1, 2 * n + 1):
                print("*", end="")
            for j in range(1, n + 1):
                print(" ", end="")
            for i in range(1, 2 * n + 1):
                print("*", end="")
            print()
            break

        # middle
        if 1 < rows < n:
            print("*", end="")
            for j in range(1, 2 * n - 1):
                print("/", end="")
            print("*", end="")

            # bridge
            if n % 2 != 0:
                if rows == int(bridge_position_odd):
                    for i in range(1, n + 1):
                        print("|", end="")
                else:
                    for j in range(1, n + 1):
                        print(" ", end="")
            else:
                if rows == int(bridge_position_even):
                    for i in range(1, n + 1):
                        print("|", end="")
                else:
                    for j in range(1, n + 1):
                        print(" ", end="")

            print("*", end="")
            for j in range(1, 2 * n - 1):
                print("/", end="")
            print("*", end="")

            print()
            break

        # bottom
        if rows == n:
            for i in range(1, 2 * n + 1):
                print("*", end="")
            for j in range(1, n + 1):
                print(" ", end="")
            for i in range(1, 2 * n + 1):
                print("*", end="")
            print()
            break
