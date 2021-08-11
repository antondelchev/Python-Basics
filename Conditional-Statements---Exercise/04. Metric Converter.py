distance = float(input())
distance_from = input()
distance_to = input()
converted = 0

if distance_from == "mm" and distance_to == "cm":
    converted = distance / 10
elif distance_from == "mm" and distance_to == "m":
    converted = distance / 1000
elif distance_from == "cm" and distance_to == "mm":
    converted = distance * 10
elif distance_from == "cm" and distance_to == "m":
    converted = distance / 100
elif distance_from == "m" and distance_to == "mm":
    converted = distance * 1000
elif distance_from == "m" and distance_to == "cm":
    converted = distance * 100

print(f"{converted:.3f}")
