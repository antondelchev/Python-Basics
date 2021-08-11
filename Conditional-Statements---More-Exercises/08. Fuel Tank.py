fuel_type = input()
fuel_liters = float(input())

if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
    if fuel_type == "Diesel" and fuel_liters >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    elif fuel_type == "Gasoline" and fuel_liters >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    elif fuel_type == "Gas" and fuel_liters >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    if fuel_liters < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")
