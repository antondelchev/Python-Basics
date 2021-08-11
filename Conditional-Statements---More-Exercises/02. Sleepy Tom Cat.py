holidays_per_year = int(input())

play_time_mins_yearly = 30000
work_days_play_mins = 63
holidays_play_mins = 127

total_playtime = holidays_per_year * holidays_play_mins + (365 - holidays_per_year)*work_days_play_mins

if total_playtime > play_time_mins_yearly:
    difference = total_playtime - play_time_mins_yearly
    diff_hours = difference // 60
    diff_mins = difference % 60
    print("Tom will run away")
    print(f"{diff_hours} hours and {diff_mins} minutes more for play")
else:
    difference = play_time_mins_yearly - total_playtime
    diff_hours = difference // 60
    diff_mins = difference % 60
    print("Tom sleeps well")
    print(f"{diff_hours} hours and {diff_mins} minutes less for play")
