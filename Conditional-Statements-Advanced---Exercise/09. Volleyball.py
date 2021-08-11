import math

year_type = input()
holidays = int(input())
weekends_home_town = int(input())

weekends_sofia = 48 - weekends_home_town

volleyball_sofia = 3 / 4 * weekends_sofia
volleyball_home_town = weekends_home_town
volleyball_holidays = 2 / 3 * holidays

volleyball_total = volleyball_sofia + volleyball_home_town + volleyball_holidays

if year_type == "leap":
    volleyball_total = 1.15 * volleyball_total
    print(math.floor(volleyball_total))
elif year_type == "normal":
    print(math.floor(volleyball_total))
