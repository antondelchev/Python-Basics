exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

converted_mins_exam = exam_hour * 60 + exam_minutes
converted_mins_arrival = arrival_hour * 60 + arrival_minutes

if converted_mins_exam < converted_mins_arrival:
    total_mins_difference = converted_mins_arrival - converted_mins_exam
    hours_over = total_mins_difference // 60
    mins_over = total_mins_difference % 60
    print("Late")
    if total_mins_difference <= 59:
        print(f"{mins_over} minutes after the start")
    else:
        print(f"{hours_over}:{mins_over:02d} hours after the start")
elif converted_mins_exam == converted_mins_arrival or 0 < (converted_mins_exam - converted_mins_arrival) <= 30:
    total_mins_difference = converted_mins_exam - converted_mins_arrival
    hours_under = total_mins_difference // 60
    mins_under = total_mins_difference % 60
    print("On time")
    if 0 < total_mins_difference <= 59:
        print(f"{mins_under} minutes before the start")
    elif total_mins_difference > 59:
        print(f"{hours_under}:{mins_under:02d} hours before the start")
elif converted_mins_exam - converted_mins_arrival > 30:
    total_mins_difference = converted_mins_exam - converted_mins_arrival
    hours_under = total_mins_difference // 60
    mins_under = total_mins_difference % 60
    print("Early")
    if 0 < total_mins_difference <= 59:
        print(f"{mins_under} minutes before the start")
    elif total_mins_difference > 59:
        print(f"{hours_under}:{mins_under:02d} hours before the start")
