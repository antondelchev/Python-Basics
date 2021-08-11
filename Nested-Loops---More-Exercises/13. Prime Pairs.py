start_first_pair = int(input())
start_second_pair = int(input())
difference_first_pair_end = int(input())
difference_second_pair_end = int(input())

end_first_pair = start_first_pair + difference_first_pair_end
end_second_pair = start_second_pair + difference_second_pair_end

for ab in range(start_first_pair, end_first_pair + 1):
    counter_1 = 0
    first_pair = ""
    for i in range(1, ab + 1):
        if ab % i == 0:
            counter_1 += 1
        if counter_1 <= 2:
            first_pair = ab

    for cd in range(start_second_pair, end_second_pair + 1):
        counter_2 = 0
        second_pair = ""
        for j in range(1, cd + 1):
            if cd % j == 0:
                counter_2 += 1
            if counter_2 <= 2:
                second_pair = cd

        if first_pair != "" and second_pair != "":
            if counter_1 <= 2 and counter_2 <= 2:
                print(f"{first_pair}{second_pair}")
