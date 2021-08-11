distance_km = int(input())
day_or_night = input()
price = 0

if 20 <= distance_km < 100:
    price = 0.09 * distance_km
elif distance_km >= 100:
    price = 0.06 * distance_km
elif day_or_night == "day":
    price = 0.7 + distance_km * 0.79
elif day_or_night == "night":
    price = 0.7 + distance_km * 0.9

print(f"{price:.2f}")
