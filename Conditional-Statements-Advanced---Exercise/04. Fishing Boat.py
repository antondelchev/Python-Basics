budget = float(input())
season = input()
fishermen_number = int(input())

renting_cost = 0
price = 0

if season == "Spring":
    renting_cost = 3000
elif season == "Summer" or season == "Autumn":
    renting_cost = 4200
elif season == "Winter":
    renting_cost = 2600

if 0 <= fishermen_number <= 6:
    price = renting_cost * 0.9
elif 7 <= fishermen_number <= 11:
    price = renting_cost * 0.85
elif fishermen_number >= 12:
    price = renting_cost * 0.75

if fishermen_number % 2 == 0 and season != "Autumn":
    price = price * 0.95

if budget >= price:
    money_left = budget - price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
