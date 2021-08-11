first_number = int(input())
second_number = int(input())
magic_number = int(input())

counter = 0
found = False

for i in range(first_number, second_number + 1):
    for j in range(first_number, second_number + 1):
        counter += 1
        if i + j == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{counter} combinations - neither equals {magic_number}")
