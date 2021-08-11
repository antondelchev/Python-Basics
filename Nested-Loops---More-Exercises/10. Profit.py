total_coins_one_lv = int(input())
total_coins_two_lv = int(input())
total_notes_five = int(input())
pay_sum = int(input())

for i in range(0, total_coins_one_lv + 1):
    for j in range(0, total_coins_two_lv + 1):
        for k in range(0, total_notes_five + 1):
            num_coins_one = 0
            num_coins_two = 0
            num_notes_five = 0
            paid = 0

            if k * 5 <= pay_sum:
                paid += k * 5
                num_notes_five += k
            if j * 2 <= pay_sum:
                paid += j * 2
                num_coins_two += j
            if i * 1 <= pay_sum:
                paid += i * 1
                num_coins_one += i

            if paid == pay_sum:
                print(f"{num_coins_one} * 1 lv. + {num_coins_two} * 2 lv. + {num_notes_five} * 5 lv. = {pay_sum} lv.")
