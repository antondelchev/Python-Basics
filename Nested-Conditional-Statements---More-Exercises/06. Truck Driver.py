season = input()
km_per_month = float(input())

income_per_km = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        income_per_km = 0.75 * km_per_month
    elif season == "Summer":
        income_per_km = 0.9 * km_per_month
    elif season == "Winter":
        income_per_km = 1.05 * km_per_month
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        income_per_km = 0.95 * km_per_month
    elif season == "Summer":
        income_per_km = 1.1 * km_per_month
    elif season == "Winter":
        income_per_km = 1.25 * km_per_month
elif 10000 < km_per_month <= 20000:
    income_per_km = 1.45 * km_per_month

salary = 0.9 * income_per_km * 4

print(f"{salary:.2f}")
