days_to_calculate = int(input())

total_doctors = 7
current_day_patients_arrived = 0
treated_patients = 0
untreated_patients = 0

total_treated = 0
total_untreated = 0

for i in range(1, days_to_calculate + 1):
    if i % 3 == 0:
        if total_untreated > total_treated:
            total_doctors += 1
        current_day_patients_arrived = int(input())
    else:
        current_day_patients_arrived = int(input())

    if current_day_patients_arrived < total_doctors:
        treated_patients = current_day_patients_arrived
        untreated_patients = 0
    elif current_day_patients_arrived == total_doctors:
        treated_patients = total_doctors
        untreated_patients = 0
    elif current_day_patients_arrived > total_doctors:
        treated_patients = total_doctors
        untreated_patients = current_day_patients_arrived - treated_patients

    total_treated += treated_patients
    total_untreated += untreated_patients

print(f"Treated patients: {total_treated}.")
print(f"Untreated patients: {total_untreated}.")
