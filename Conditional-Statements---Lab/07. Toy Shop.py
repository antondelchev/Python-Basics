holiday_price = float(input())
total_puzzles = int(input())
total_dolls = int(input())
total_bears = int(input())
total_minions = int(input())
total_trucks = int(input())
discount = 0
rent = 0

toys_total = total_puzzles + total_dolls + total_bears + total_minions + total_trucks
total_price = total_puzzles * 2.60 + total_dolls * 3 + total_bears * 4.10 + total_minions * 8.20 + total_trucks * 2

if toys_total >= 50:
    discount = total_price * 0.25
income = total_price - discount
rent = income * 0.10
money_left = income - rent

if money_left >= holiday_price:
    money_after_holiday = money_left - holiday_price
    print(f"Yes! {money_after_holiday:.2f} lv left.")
else:
    money_needed = holiday_price - money_left
    print(f"Not enough money! {money_needed:.2f} lv needed.")
