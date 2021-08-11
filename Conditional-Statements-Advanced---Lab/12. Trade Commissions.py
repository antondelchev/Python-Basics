city = input()
sales = float(input())
comission = 0

if city == "Sofia" or city == "Plovdiv" or city == "Varna":
    if sales < 0:
        print("error")
    elif 0 <= sales <= 500:
        if city == "Sofia":
            comission = sales * 0.05
        if city == "Plovdiv":
            comission = sales * 0.055
        if city == "Varna":
            comission = sales * 0.045
        print(f"{comission:.2f}")
    elif 500 <= sales <= 1000:
        if city == "Sofia":
            comission = sales * 0.07
        if city == "Plovdiv":
            comission = sales * 0.08
        if city == "Varna":
            comission = sales * 0.075
        print(f"{comission:.2f}")
    elif 1000 <= sales <= 10000:
        if city == "Sofia":
            comission = sales * 0.08
        if city == "Plovdiv":
            comission = sales * 0.12
        if city == "Varna":
            comission = sales * 0.1
        print(f"{comission:.2f}")
    elif sales > 10000:
        if city == "Sofia":
            comission = sales * 0.12
        if city == "Plovdiv":
            comission = sales * 0.145
        if city == "Varna":
            comission = sales * 0.13
        print(f"{comission:.2f}")
else:
    print("error")
