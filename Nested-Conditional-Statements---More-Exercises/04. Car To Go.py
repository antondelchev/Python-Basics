budget = float(input())
season = input()

price = 0
car_type = ""
car_class = ""

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = 0.35 * budget
    elif season == "Winter":
        car_type = "Jeep"
        price = 0.65 * budget
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price = 0.45 * budget
    elif season == "Winter":
        car_type = "Jeep"
        price = 0.8 * budget
if budget > 500:
    car_class = "Luxury class"
    car_type = "Jeep"
    price = 0.9 * budget

print(car_class)
print(f"{car_type} - {price:.2f}")
