strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

money_for_strawberries = strawberries_kg * strawberries_price
money_for_raspberries = strawberries_price / 2 * raspberries_kg
money_for_oranges = (strawberries_price / 2 - (0.4 * strawberries_price / 2)) * oranges_kg
money_for_bananas = (strawberries_price / 2 - (0.8 * strawberries_price / 2)) * bananas_kg

money_total = money_for_strawberries + money_for_raspberries + money_for_oranges + money_for_bananas

print(money_total)
