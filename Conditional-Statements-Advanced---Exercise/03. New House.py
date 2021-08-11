flower_type = input()
flowers_number = int(input())
budget = int(input())

price = 0

if flower_type == "Roses":
    price = 5 * flowers_number
    if flowers_number > 80:
        price = 0.9 * price
elif flower_type == "Dahlias":
    price = 3.8 * flowers_number
    if flowers_number > 90:
        price = 0.85 * price
elif flower_type == "Tulips":
    price = 2.8 * flowers_number
    if flowers_number > 80:
        price = 0.85 * price
elif flower_type == "Narcissus":
    price = 3 * flowers_number
    if flowers_number < 120:
        price = price + 0.15 * price
elif flower_type == "Gladiolus":
    price = 2.5 * flowers_number
    if flowers_number < 80:
        price = price + 0.2 * price

if price <= budget:
    money_left = budget - price
    print(f"Hey, you have a great garden with {flowers_number} {flower_type} and {money_left:.2f} leva left.")
else:
    money_needed = price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
