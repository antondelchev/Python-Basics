n = int(input())

count_one = 0
count_two = 0
count_three = 0
count_four = 0
count_five = 0

for i in range(1, n + 1):
    number = int(input())
    if number < 200:
        count_one += 1
    elif 200 <= number <= 399:
        count_two += 1
    elif 400 <= number <= 599:
        count_three += 1
    elif 600 <= number <= 799:
        count_four += 1
    elif number >= 800:
        count_five += 1

percent_one = count_one / n * 100
percent_two = count_two / n * 100
percent_three = count_three / n * 100
percent_four = count_four / n * 100
percent_five = count_five / n * 100

print(f"{percent_one:.2f}%")
print(f"{percent_two:.2f}%")
print(f"{percent_three:.2f}%")
print(f"{percent_four:.2f}%")
print(f"{percent_five:.2f}%")
