deposit = float(input())
deposit_time = int(input())
annual_percentage_rate = float(input())

total_interest = deposit * annual_percentage_rate / 100
interest_per_month = total_interest / 12
total_amount = deposit + deposit_time * interest_per_month

print(total_amount)
