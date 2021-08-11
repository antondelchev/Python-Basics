space_width = int(input())
space_length = int(input())
space_height = int(input())

command = input()

volume_of_room = space_width * space_length * space_height
volume_of_box = 1
volume_taken = 0

while command != "Done":
    number_of_boxes = int(command)
    volume_taken += number_of_boxes
    if volume_taken >= volume_of_room:
        print(f"No more free space! You need {volume_taken - volume_of_room} Cubic meters more.")
        break
    else:
        command = input()

if command == "Done":
    print(f"{volume_of_room - volume_taken} Cubic meters left.")
