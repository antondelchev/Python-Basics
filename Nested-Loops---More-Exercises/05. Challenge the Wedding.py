men_total = int(input())
women_total = int(input())
tables_total = int(input())

counter = 1

for i in range(1, men_total + 1):
    for j in range(1, women_total + 1):
        if counter <= tables_total:
            print(f"({i} <-> {j})", end=" ")
            counter += 1
