start_num = int(input())
end_num = int(input())
magic_num = int(input())

counter = 0
found = False

for i in range(start_num, end_num + 1):
    for j in range(start_num, end_num + 1):
        counter += 1
        if i + j == magic_num:
            print(f"Combination N:{counter} ({i} + {j} = {magic_num})")
            found = True
            break
    if found:
        break

if found is False:
    print(f"{counter} combinations - neither equals {magic_num}")
