num_one = int(input())
num_two = int(input())

num_one_as_str = str(num_one)
num_two_as_str = str(num_two)

for number in range(num_one, num_two + 1):
    even_sum = 0
    odd_sum = 0
    for position in range(0, 6):

        current_number_as_str = str(number)
        current_symbol = current_number_as_str[position]

        if position % 2 == 0:
            even_sum += int(current_symbol)
        else:
            odd_sum += int(current_symbol)

    if even_sum == odd_sum:
        print(number, end=" ")
