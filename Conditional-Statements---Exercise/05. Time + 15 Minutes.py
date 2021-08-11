hours = int(input())
minutes = int(input())

sum_mins = hours * 60 + minutes + 15

if 0 <= hours <= 23 and 0 <= minutes <= 59:
   total_hours = sum_mins // 60
   mins_formatted = sum_mins % 60
   hours_formatted = total_hours % 24
   if mins_formatted <= 9:
      print(f"{hours_formatted}:0{mins_formatted}")
   else:
       print(f"{hours_formatted}:{mins_formatted}")
