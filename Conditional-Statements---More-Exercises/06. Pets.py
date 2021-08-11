import math

days_away = int(input())
total_food_kg = int(input())
dog_food_daily_kg = float(input())
cat_food_daily_kg = float(input())
turtle_food_daily_grams = float(input())

turtle_food_daily_kg = turtle_food_daily_grams / 1000

kg_food_total_dog = days_away * dog_food_daily_kg
kg_food_total_cat = days_away * cat_food_daily_kg
kg_food_total_turtle = days_away * turtle_food_daily_kg

kg_total_consumed = kg_food_total_dog + kg_food_total_cat + kg_food_total_turtle

if total_food_kg >= kg_total_consumed:
    food_left = total_food_kg - kg_total_consumed
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    food_needed = kg_total_consumed - total_food_kg
    print(f"{math.ceil(food_needed)} more kilos of food are needed.")
