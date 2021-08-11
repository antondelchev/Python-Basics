age = int(input())
washing_machine_price = float(input())
single_toy_price = int(input())

toys_number = 0
money_as_a_gift_each_birthday = 0
money_collected_as_gift = 0
money_total = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money_as_a_gift_each_birthday += 10
        money_collected_as_gift += money_as_a_gift_each_birthday
        money_collected_as_gift -= 1
    else:
        toys_number += 1

sold_toys = toys_number * single_toy_price
money_total = money_collected_as_gift

all_birthdays_funds = sold_toys + money_total

if all_birthdays_funds >= washing_machine_price:
    funds_left = all_birthdays_funds - washing_machine_price
    print(f"Yes! {funds_left:.2f}")
else:
    funds_needed = washing_machine_price - all_birthdays_funds
    print(f"No! {funds_needed:.2f}")
