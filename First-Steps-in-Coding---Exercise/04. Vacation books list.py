total_pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

hours_to_read_book = total_pages / pages_per_hour
hours_per_day = hours_to_read_book / days_to_read

print(hours_per_day)
