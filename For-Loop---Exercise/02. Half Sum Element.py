import sys

n = int(input())

current_max = -sys.maxsize
total_sum = 0

for i in range(n):
    number = int(input())
    total_sum += number
    if number > current_max:
        current_max = number

if current_max == (total_sum - current_max):
    print("Yes")
    print(f"Sum = {current_max}")
else:
    print("No")
    print(f"Diff = {abs(total_sum - current_max - current_max)}")
