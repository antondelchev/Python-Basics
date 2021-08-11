import math

number_magnolii = int(input())
number_ziumbiuli = int(input())
number_roses = int(input())
number_cactuses = int(input())
gift_price = float(input())

total_income = number_magnolii * 3.25 + number_ziumbiuli * 4 + number_roses * 3.5 + number_cactuses * 8
taxes = total_income * 0.05
money_left = total_income - taxes

if money_left >= gift_price:
    extra_money = money_left - gift_price
    print(f"She is left with {math.floor(extra_money)} leva.")
else:
    needed_money = gift_price - money_left
    print(f"She will have to borrow {math.ceil(needed_money)} leva.")
