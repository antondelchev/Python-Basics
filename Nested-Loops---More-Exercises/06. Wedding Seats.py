end_sector = input()
rows_in_first_sector = int(input())
odd_row_seats_number = int(input())

end_sector_as_num = ord(end_sector)
add_row = 0
total_seats_num = 0

for sector in range(65, end_sector_as_num + 1):
    add_row += 1
    current_sector = chr(sector)
    number_of_sectors = (end_sector_as_num - 65) + 1
    for row in range(1, rows_in_first_sector + add_row):
        current_row = row
        if row % 2 != 0:
            number_of_seats = odd_row_seats_number
        else:
            number_of_seats = odd_row_seats_number + 2
        for seat in range(97, 97 + number_of_seats):
            current_seat = chr(seat)
            total_seats_num += 1
            print(f"{current_sector}{current_row}{current_seat}")

print(total_seats_num)
