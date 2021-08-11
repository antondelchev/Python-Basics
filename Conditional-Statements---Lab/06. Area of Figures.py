import math
type_of_figure = input()
area = 0

if type_of_figure == "square":
    side = float(input())
    area = side * side
elif type_of_figure == "rectangle":
    sidea = float(input())
    sideb = float(input())
    area = sidea * sideb
elif type_of_figure == "circle":
    radius = float(input())
    area = math.pi * radius * radius
elif type_of_figure == "triangle":
    sidea = float(input())
    height = float(input())
    area = (sidea * height) / 2

print(area)
