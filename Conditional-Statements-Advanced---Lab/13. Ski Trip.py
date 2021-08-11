days_number = int(input())
room_type = input()
evaluation = input()
price = 0

hotel_nights = days_number - 1

if room_type == "room for one person" or room_type == "apartment" \
        or room_type == "president apartment":
    if room_type == "room for one person":
        price = hotel_nights * 18
    elif room_type == "apartment" and hotel_nights < 10:
        price = hotel_nights * 25 * 0.7
    elif room_type == "apartment" and 10 <= hotel_nights <= 15:
        price = hotel_nights * 25 * 0.65
    elif room_type == "apartment" and hotel_nights > 15:
        price = hotel_nights * 25 * 0.5
    elif room_type == "president apartment" and hotel_nights < 10:
        price = hotel_nights * 35 * 0.9
    elif room_type == "president apartment" and 10 <= hotel_nights <= 15:
        price = hotel_nights * 35 * 0.85
    elif room_type == "president apartment" and hotel_nights > 15:
        price = hotel_nights * 35 * 0.8
if evaluation == "positive":
    price = price + price * 0.25
elif evaluation == "negative":
    price = price - price * 0.1

print(f"{price:.2f}")
