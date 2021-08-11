x_one = float(input())
y_one = float(input())
x_two = float(input())
y_two = float(input())
x = float(input())
y = float(input())

if x_one < x_two and y_one < y_two:
    if x == x_two and (y_one < y < y_two):
        print("Border")
    elif x == x_one and (y_one < y < y_two):
        print("Border")
    elif (x_one <= x <= x_two) and y == y_one:
        print("Border")
    elif (x_one <= x <= x_two) and y == y_two:
        print("Border")
    else:
        print("Inside / Outside")
