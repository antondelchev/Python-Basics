time1_seconds = int(input())
time2_seconds = int(input())
time3_seconds = int(input())

total_time = time1_seconds + time2_seconds + time3_seconds

total_mins = total_time / 60
total_secs = total_time % 60
if total_secs <= 9:
    print(f"{int(total_mins)}:0{total_secs}")
else:
    print(f"{int(total_mins)}:{total_secs}")
