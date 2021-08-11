active_days = int(input())
cake_chefs = int(input())
number_of_cakes = int(input())
number_of_gofreti = int(input())
number_of_pancakes = int(input())

total_cakes_price = active_days * cake_chefs * number_of_cakes * 45
total_gofreti_price = active_days * cake_chefs * number_of_gofreti * 5.8
total_pancakes_price = active_days * cake_chefs * number_of_pancakes * 3.2

total_money_earned = total_pancakes_price + total_gofreti_price + total_cakes_price
expenses = total_money_earned / 8

final_money_earned = total_money_earned - expenses

print(final_money_earned)
