world_record = float(input())
distance_meters = float(input())
time_for_one_meter = float(input())

time_needed = distance_meters * time_for_one_meter
slowing_down_time = (distance_meters // 15) * 12.5
total_time = time_needed + slowing_down_time

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    time_above = total_time - world_record
    print(f"No, he failed! He was {time_above:.2f} seconds slower.")
