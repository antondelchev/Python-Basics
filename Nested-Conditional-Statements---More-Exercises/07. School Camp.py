season = input()
group_type = input()
pupils_number = int(input())
nights_number = int(input())

sport = ""
price = 0
final_price = 0

if group_type == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
elif group_type == "mixed":
    if season == "Winter":
        sport = "Ski"
        price = 10 * nights_number * pupils_number
    elif season == "Spring":
        sport = "Cycling"
        price = 9.5 * nights_number * pupils_number
    elif season == "Summer":
        sport = "Swimming"
        price = 20 * nights_number * pupils_number

if season == "Winter" and (group_type == "boys" or group_type == "girls"):
    price = 9.6 * nights_number * pupils_number
elif season == "Spring" and (group_type == "boys" or group_type == "girls"):
    price = 7.2 * nights_number * pupils_number
elif season == "Summer" and (group_type == "boys" or group_type == "girls"):
    price = 15 * nights_number * pupils_number

if pupils_number >= 50:
    final_price = 0.5 * price
elif 20 <= pupils_number < 50:
    final_price = 0.85 * price
elif 10 <= pupils_number < 20:
    final_price = 0.95 * price
elif 0 < pupils_number < 10:
    final_price = price

print(f"{sport} {final_price:.2f} lv.")
