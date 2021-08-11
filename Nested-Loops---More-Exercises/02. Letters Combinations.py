letter_one = input()
letter_two = input()
letter_three_skip = input()

letter_one_as_num = ord(letter_one)
letter_two_as_num = ord(letter_two)
letter_three_skip_as_num = ord(letter_three_skip)

counter = 0

for first in range(letter_one_as_num, letter_two_as_num + 1):
    if chr(first) == letter_three_skip:
        continue
    else:
        print_one = chr(first)
    for second in range(letter_one_as_num, letter_two_as_num + 1):
        if chr(second) == letter_three_skip:
            continue
        else:
            print_two = chr(second)
        for third in range(letter_one_as_num, letter_two_as_num + 1):
            print_three = chr(third)
            if print_three == letter_three_skip:
                continue
            else:
                print(f"{print_one}{print_two}{print_three}", end=" ")
                counter += 1

print(counter)
