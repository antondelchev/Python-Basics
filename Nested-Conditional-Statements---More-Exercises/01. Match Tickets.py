budget = float(input())
category = input()
men_in_group = int(input())

transport_cost = 0
tickets_cost = 0

if 1 <= men_in_group <= 4:
    transport_cost = 0.75 * budget
elif 5 <= men_in_group <= 9:
    transport_cost = 0.6 * budget
elif 10 <= men_in_group <= 24:
    transport_cost = 0.5 * budget
elif 25 <= men_in_group <= 49:
    transport_cost = 0.4 * budget
elif men_in_group > 50:
    transport_cost = 0.25 * budget

if category == "VIP":
    tickets_cost = men_in_group * 499.99
elif category == "Normal":
    tickets_cost = men_in_group * 249.99

total_cost = transport_cost + tickets_cost

if total_cost <= budget:
    money_left = budget - total_cost
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = total_cost - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
