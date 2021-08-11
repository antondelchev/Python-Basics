num_days = int(input())
num_hours = int(input())

price_total = 0
total_hours = 0

for i in range(1, num_days + 1):
    daily_price = 0
    for j in range(1, num_hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            daily_price += 2.5
        elif i % 2 != 0 and j % 2 == 0:
            daily_price += 1.25
        else:
            daily_price += 1
        if j == num_hours:
            print(f"Day: {i} - {daily_price:.2f} leva")
            price_total += daily_price

print(f"Total: {price_total:.2f} leva")
