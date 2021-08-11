number = int(input())

counter = 0
fourth = ""

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if number == a * b + c * d and a < b and c > d:
                    counter += 1
                    print(f"{a}{b}{c}{d}", end=" ")
                    if counter == 4:
                        fourth = f"{a}{b}{c}{d}"

print()
if fourth != "":
    print(f"Password: {fourth}")
else:
    print("No!")
