vegetable_price_kg = float(input())
fruit_price_kg = float(input())
vegetables_kg = int(input())
fruit_kg = int(input())

total_price_euro = (vegetable_price_kg * vegetables_kg + fruit_price_kg * fruit_kg) / 1.94

print(f"{total_price_euro:.2f}")
