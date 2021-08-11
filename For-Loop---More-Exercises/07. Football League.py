stadium_capacity = int(input())
fans_number = int(input())

number_sector_a = 0
number_sector_b = 0
number_sector_v = 0
number_sector_g = 0

for i in range(1, fans_number + 1):
    current_fan_sector = input()
    if current_fan_sector == "A":
        number_sector_a += 1
    elif current_fan_sector == "B":
        number_sector_b += 1
    elif current_fan_sector == "V":
        number_sector_v += 1
    elif current_fan_sector == "G":
        number_sector_g += 1

percent_a = number_sector_a / fans_number * 100
percent_b = number_sector_b / fans_number * 100
percent_v = number_sector_v / fans_number * 100
percent_g = number_sector_g / fans_number * 100
percent_current_vs_capacity = fans_number / stadium_capacity * 100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{percent_current_vs_capacity:.2f}%")
