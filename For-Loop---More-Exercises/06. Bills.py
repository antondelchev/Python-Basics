months = int(input())

water_bill_per_month = 20
internet_bill_per_month = 15
electricity_bills_total = 0
other_bills_total = 0

for i in range(1, months + 1):
    electricity_current_month = float(input())
    electricity_bills_total += electricity_current_month
    other_bills_current_month = (water_bill_per_month + internet_bill_per_month + electricity_current_month) * 1.2
    other_bills_total += other_bills_current_month

water_total = water_bill_per_month * months
internet_total = internet_bill_per_month * months
all_bills_average = (electricity_bills_total + water_total + internet_total + other_bills_total) / months

print(f"Electricity: {electricity_bills_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {internet_total:.2f} lv")
print(f"Other: {other_bills_total:.2f} lv")
print(f"Average: {all_bills_average:.2f} lv")
