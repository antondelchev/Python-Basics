fuel_type = input()
fuel_liters = float(input())
club_card = input()

price_gas_no_club = fuel_liters * 0.93
price_gasoline_no_club = fuel_liters * 2.22
price_diesel_no_club = fuel_liters * 2.33

price_gas_club = fuel_liters * 0.93 - 0.08 * fuel_liters
price_gasoline_club = fuel_liters * 2.22 - 0.18 * fuel_liters
price_diesel_club = fuel_liters * 2.33 - 0.12 * fuel_liters

if fuel_liters < 20:
    if fuel_type == "Gas" and club_card == "No":
        print(f"{price_gas_no_club:.2f} lv.")
    elif fuel_type == "Gas" and club_card == "Yes":
        print(f"{price_gas_club:.2f} lv.")

    if fuel_type == "Gasoline" and club_card == "No":
        print(f"{price_gasoline_no_club:.2f} lv.")
    elif fuel_type == "Gasoline" and club_card == "Yes":
        print(f"{price_gasoline_club:.2f} lv.")

    if fuel_type == "Diesel" and club_card == "No":
        print(f"{price_diesel_no_club:.2f} lv.")
    elif fuel_type == "Diesel" and club_card == "Yes":
        print(f"{price_diesel_club:.2f} lv.")

if fuel_liters > 25:
    if fuel_type == "Gas" and club_card == "No":
        print(f"{(price_gas_no_club * 0.9):.2f} lv.")
    elif fuel_type == "Gas" and club_card == "Yes":
        print(f"{(price_gas_club * 0.9):.2f} lv.")

    if fuel_type == "Gasoline" and club_card == "No":
        print(f"{(price_gasoline_no_club * 0.9):.2f} lv.")
    elif fuel_type == "Gasoline" and club_card == "Yes":
        print(f"{(price_gasoline_club * 0.9):.2f} lv.")

    if fuel_type == "Diesel" and club_card == "No":
        print(f"{(price_diesel_no_club * 0.9):.2f} lv.")
    elif fuel_type == "Diesel" and club_card == "Yes":
        print(f"{(price_diesel_club * 0.9):.2f} lv.")

if 20 <= fuel_liters <= 25:
    if fuel_type == "Gas" and club_card == "No":
        print(f"{(price_gas_no_club * 0.92):.2f} lv.")
    elif fuel_type == "Gas" and club_card == "Yes":
        print(f"{(price_gas_club * 0.92):.2f} lv.")

    if fuel_type == "Gasoline" and club_card == "No":
        print(f"{(price_gasoline_no_club * 0.92):.2f} lv.")
    elif fuel_type == "Gasoline" and club_card == "Yes":
        print(f"{(price_gasoline_club * 0.92):.2f} lv.")

    if fuel_type == "Diesel" and club_card == "No":
        print(f"{(price_diesel_no_club * 0.92):.2f} lv.")
    elif fuel_type == "Diesel" and club_card == "Yes":
        print(f"{(price_diesel_club * 0.92):.2f} lv.")
