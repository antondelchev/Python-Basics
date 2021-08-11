import sys

n = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize

even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

if n == 0:
    odd_sum = 0
    odd_min = 0
    odd_max = 0
    even_sum = 0
    even_min = 0
    even_max = 0
elif n == 1:
    number = float(input())
    odd_sum += number
    even_sum = 0
    even_min = 0
    even_max = 0
    if number < odd_min:
        odd_min = number
    if number > odd_max:
        odd_max = number
elif n > 0:
    for i in range(1, n + 1):
        number = float(input())
        if i % 2 != 0:
            odd_sum += number
            if number < odd_min:
                odd_min = number
            if number > odd_max:
                odd_max = number
        elif i % 2 == 0:
            even_sum += number
            if number < even_min:
                even_min = number
            if number > even_max:
                even_max = number

print(f"OddSum={odd_sum:.2f},")
if n == 0:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
else:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if n == 0 or n == 1:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
