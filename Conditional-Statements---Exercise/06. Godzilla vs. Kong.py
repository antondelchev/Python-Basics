budget = float(input())
extras_number = int(input())
outfit_price_per_extra = float(input())
discount = 0
final_outfit_price = 0

decor_price = budget * 0.1
outfit_price_total = extras_number * outfit_price_per_extra

if extras_number > 150:
    discount = outfit_price_total * 0.1
    final_outfit_price = outfit_price_total - discount
else:
    final_outfit_price = outfit_price_total

total_costs = final_outfit_price + decor_price

if total_costs <= budget:
    money_left = budget - total_costs
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    money_needed = total_costs - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
