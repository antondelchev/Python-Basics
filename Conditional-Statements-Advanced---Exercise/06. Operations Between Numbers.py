number_one = int(input())
number_two = int(input())
action = input()
result = 0

if action == "+" or action == "-" or action == "*":
    if action == "+":
        result = number_one + number_two
    elif action == "-":
        result = number_one - number_two
    elif action == "*":
        result = number_one * number_two

    if result % 2 == 0:
        print(f"{number_one} {action} {number_two} = {result} - even")
    else:
        print(f"{number_one} {action} {number_two} = {result} - odd")

if action == "/" or action == "%":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    elif action == "/":
        result = number_one / number_two
        print(f"{number_one} {action} {number_two} = {result:.2f}")
    elif action == "%":
        result = number_one % number_two
        print(f"{number_one} {action} {number_two} = {result}")
