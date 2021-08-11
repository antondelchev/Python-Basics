will_money = float(input())
until_year = int(input())

even_year_spendings = 0
odd_year_spendings = 0
current_years_of_the_person = 18

if until_year >= 1800:
    for i in range(1800, until_year + 1):
        if i != 1800:
            current_years_of_the_person += 1
        if i % 2 == 0:
            even_year_spendings += 12000
        else:
            odd_year_spendings += (12000 + 50 * current_years_of_the_person)

total_spendings = even_year_spendings + odd_year_spendings

if will_money >= total_spendings:
    money_left = will_money - total_spendings
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    money_needed = total_spendings - will_money
    print(f"He will need {money_needed:.2f} dollars to survive.")
