length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent_stuff_filled = float(input())

volume_total = length_cm * width_cm * height_cm
liters_water_total = volume_total * 0.001
water_left = liters_water_total - (percent_stuff_filled / 100 * volume_total * 0.001)

print(water_left)
