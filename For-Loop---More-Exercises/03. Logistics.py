number_of_loads = int(input())

tonnes_total = 0

bus_tonnes_total = 0
truck_tonnes_total = 0
train_tonnes_total = 0

bus_price_total = 0
truck_price_total = 0
train_price_total = 0

for i in range(1, number_of_loads + 1):
    tonnes = int(input())
    tonnes_total += tonnes
    if tonnes <= 3:
        bus_tonnes_total += tonnes
        bus_price_total += tonnes * 200
    elif 4 <= tonnes <= 11:
        truck_tonnes_total += tonnes
        truck_price_total += tonnes * 175
    elif tonnes >= 12:
        train_tonnes_total += tonnes
        train_price_total += tonnes * 120

average_ton_price = (bus_price_total + truck_price_total + train_price_total) / tonnes_total
percent_tonnes_bus = bus_tonnes_total / tonnes_total * 100
percent_tonnes_truck = truck_tonnes_total / tonnes_total * 100
percent_tonnes_train = train_tonnes_total / tonnes_total * 100

print(f"{average_ton_price:.2f}")
print(f"{percent_tonnes_bus:.2f}%")
print(f"{percent_tonnes_truck:.2f}%")
print(f"{percent_tonnes_train:.2f}%")
