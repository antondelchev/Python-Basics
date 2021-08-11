import math

hours_requested = int(input())
days_requested = int(input())
workers_extra_hours = int(input())

work_days_number = days_requested - (0.1 * days_requested)
work_hours = work_days_number * 8

extra_hours = workers_extra_hours * days_requested * 2
total_hours = extra_hours + work_hours

if total_hours >= hours_requested:
    hours_left = total_hours - hours_requested
    print(f"Yes!{math.floor(hours_left)} hours left.")
else:
    hours_left = hours_requested - total_hours
    print(f"Not enough time!{math.ceil(hours_left)} hours needed.")
