x = float(input())
y = float(input())
h = float(input())

front_back_area = (x * x * 2) - (1.2 * 2)
side_area = (x * y * 2) - (1.5 * 1.5) * 2

roof_front_back_area = x * h
roof_side = x * y * 2

total_green_paint_liters = (front_back_area + side_area) / 3.4
total_red_paint_liters = (roof_front_back_area + roof_side) / 4.3

print(f"{total_green_paint_liters:.2f}")
print(f"{total_red_paint_liters:.2f}")
