n = int(input())

base_done = False
mid_done = False
roof_done = False

order = 1

for rows in range(1, n + 1):
    for columns in range(1, n + 1):
        # base
        if not base_done and order == 3:
            for j in range(1, int(n / 2) + 1):
                print("|", end="")
                for i in range(1, (n - 2) + 1):
                    print("*", end="")
                print("|", end="")
                print()
                if j == int(n / 2):
                    base_done = True
        # mid
        if not base_done and not mid_done and order == 2:
            for i in range(1, n + 1):
                print("*", end="")
            print()
            mid_done = True
            order += 1
            break
        # top
        if not base_done and not mid_done and order == 1:
            if n % 2 == 0:
                stars = 2
                for i in range(int(n / 2), 1, - 1):
                    for j in range(i, 1, - 1):
                        print("-", end="")
                    for k in range(1, stars + 1):
                        print("*", end="")
                    for j in range(i, 1, - 1):
                        print("-", end="")
                    stars += 2
                    print()
                order += 1
            else:
                stars = 1
                for i in range(int(n / 2 + 1), 1, - 1):
                    for j in range(i, 1, - 1):
                        print("-", end="")
                    for k in range(1, stars + 1):
                        print("*", end="")
                    for j in range(i, 1, - 1):
                        print("-", end="")
                    stars += 2
                    print()
                order += 1

    if base_done and mid_done:
        break
