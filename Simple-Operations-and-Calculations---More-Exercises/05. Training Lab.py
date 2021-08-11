w = float(input())
h = float(input())

if 3 <= h and h <= w and w <= 100:
    h_left = h * 100 - 100
    work_spaces_h = h_left // 70
    print(work_spaces_h)
    work_spaces_w = w * 100 // 120
    print(work_spaces_w)
    total_work_spaces = (int(work_spaces_h) * int(work_spaces_w)) - 3
    print(total_work_spaces)
