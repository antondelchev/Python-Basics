import math

area_grapefield = int(input())
grapes_per_sqm = float(input())
liters_wine_target = int(input())
workers_number = int(input())

harvest_total = area_grapefield * grapes_per_sqm
grapes_for_wine = 0.4 * harvest_total
liters_wine_produced = grapes_for_wine / 2.5

if liters_wine_produced < liters_wine_target:
    needed = liters_wine_target - liters_wine_produced
    print(f"It will be a tough winter! More {math.floor(needed)} liters wine needed.")
else:
    wine_extra = liters_wine_produced - liters_wine_target
    extra_per_person = wine_extra / workers_number
    print(f"Good harvest this year! Total wine: {math.floor(liters_wine_produced)} liters.")
    print(f"{math.ceil(wine_extra)} liters left -> {math.ceil(extra_per_person)} liters per person.")
