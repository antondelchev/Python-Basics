n = int(input())

count_one = 0
count_two = 0
count_three = 0

for i in range(1, n + 1):
    number = int(input())
    if number % 2 == 0:
        count_one += 1
    if number % 3 == 0:
        count_two += 1
    if number % 4 == 0:
        count_three += 1

percent_one = count_one / n * 100
percent_two = count_two / n * 100
percent_three = count_three / n * 100

print(f"{percent_one:.2f}%")
print(f"{percent_two:.2f}%")
print(f"{percent_three:.2f}%")
