number_of_floors = int(input())
number_of_rooms = int(input())

for i in range(number_of_floors, 0, -1):
    for j in range(0, number_of_rooms):
        if i == number_of_floors:
            print(f"L{i}{j}", end=" ")
        elif i % 2 == 0:
            print(f"O{i}{j}", end=" ")
        elif i % 2 != 0:
            print(f"A{i}{j}", end=" ")

    print()
