hrizantemi_bought = int(input())
roses_bought = int(input())
laleta_bought = int(input())
season = input()
holiday_or_not = input()

hrizantemi_price_total = 0
roses_price_total = 0
laleta_price_total = 0
first_discount = 0
second_discount = 0

if (season == "Spring" or season == "Summer") and holiday_or_not == "N":
    hrizantemi_price_total = 2 * hrizantemi_bought
    roses_price_total = 4.1 * roses_bought
    laleta_price_total = 2.5 * laleta_bought
    if season == "Spring" and laleta_bought > 7:
        first_discount = 0.05 * (hrizantemi_price_total + roses_price_total + laleta_price_total)
elif (season == "Autumn" or season == "Winter") and holiday_or_not == "N":
    hrizantemi_price_total = 3.75 * hrizantemi_bought
    roses_price_total = 4.5 * roses_bought
    laleta_price_total = 4.15 * laleta_bought
    if season == "Winter" and roses_bought >= 10:
        first_discount = 0.1 * (hrizantemi_price_total + roses_price_total + laleta_price_total)
elif (season == "Spring" or season == "Summer") and holiday_or_not == "Y":
    hrizantemi_price_total = 2 * hrizantemi_bought * 1.15
    roses_price_total = 4.1 * roses_bought * 1.15
    laleta_price_total = 2.5 * laleta_bought * 1.15
    if season == "Spring" and laleta_bought > 7:
        first_discount = 0.05 * (hrizantemi_price_total + roses_price_total + laleta_price_total)
elif (season == "Autumn" or season == "Winter") and holiday_or_not == "Y":
    hrizantemi_price_total = 3.75 * hrizantemi_bought * 1.15
    roses_price_total = 4.5 * roses_bought * 1.15
    laleta_price_total = 4.15 * laleta_bought * 1.15
    if season == "Winter" and roses_bought >= 10:
        first_discount = 0.1 * (hrizantemi_price_total + roses_price_total + laleta_price_total)

after_first_discount = (hrizantemi_price_total + roses_price_total + laleta_price_total) - first_discount

if (hrizantemi_bought + roses_bought + laleta_bought) > 20:
    second_discount = 0.2 * after_first_discount

final_price = after_first_discount - second_discount + 2

print(f"{final_price:.2f}")
