tabs_number = int(input())
salary = int(input())

lost_money = 0

if 1 <= tabs_number <= 10:
    for i in range(1, tabs_number + 1):
        tab_name = input()
        if tab_name == "Facebook":
            lost_money += 150
        elif tab_name == "Instagram":
            lost_money += 100
        elif tab_name == "Reddit":
            lost_money += 50
        if salary - lost_money <= 0:
            print("You have lost your salary.")
            exit(0)

money_left = salary - lost_money
print(money_left)
