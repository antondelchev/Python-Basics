word = input()
sum_total = 0

for char in word:
    if char == "a":
        sum_total = sum_total + 1
    elif char == "e":
        sum_total = sum_total + 2
    elif char == "i":
        sum_total = sum_total + 3
    elif char == "o":
        sum_total = sum_total + 4
    elif char == "u":
        sum_total = sum_total + 5

print(sum_total)
