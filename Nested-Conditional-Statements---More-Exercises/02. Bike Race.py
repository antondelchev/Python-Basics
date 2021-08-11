juniors_number = int(input())
seniors_number = int(input())
race_type = input()

total_participants = juniors_number + seniors_number
participation_fee_total_juniors = 0
participation_fee_total_seniors = 0

if juniors_number > 0:
    if race_type == "trail":
        participation_fee_total_juniors = 5.5 * juniors_number
    elif race_type == "cross-country":
        participation_fee_total_juniors = 8 * juniors_number
    elif race_type == "downhill":
        participation_fee_total_juniors = 12.25 * juniors_number
    elif race_type == "road":
        participation_fee_total_juniors = 20 * juniors_number

if seniors_number > 0:
    if race_type == "trail":
        participation_fee_total_seniors = 7 * seniors_number
    elif race_type == "cross-country":
        participation_fee_total_seniors = 9.5 * seniors_number
    elif race_type == "downhill":
        participation_fee_total_seniors = 13.75 * seniors_number
    elif race_type == "road":
        participation_fee_total_seniors = 21.5 * seniors_number

participation_fee_total = participation_fee_total_juniors + participation_fee_total_seniors

if race_type == "cross-country" and total_participants >= 50:
    participation_fee_total = 0.75 * participation_fee_total

expenses = 0.05 * participation_fee_total
donations = participation_fee_total - expenses

print(f"{donations:.2f}")
