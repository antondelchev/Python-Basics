destination = input()

while destination != "End":
    budget = float(input())
    saved_money = 0
    while saved_money < budget:
        current_saved = float(input())
        saved_money += current_saved
    print(f"Going to {destination}!")
    destination = input()
