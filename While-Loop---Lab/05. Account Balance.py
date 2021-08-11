command = input()
account_funds = 0

while command != "NoMoreMoney":
    add_to_balance = float(command)
    if add_to_balance < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {add_to_balance:.2f}")
    account_funds += add_to_balance
    command = input()

print(f"Total: {account_funds:.2f}")
