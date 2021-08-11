movie = input()

student_ticket = 0
standard_ticket = 0
kid_ticket = 0

while movie != "Finish":
    available_seats = int(input())
    tickets_sold = 0

    ticket_type = input()

    while ticket_type != "End":
        tickets_sold += 1
        if ticket_type == "standard":
            standard_ticket += 1
        elif ticket_type == "student":
            student_ticket += 1
        elif ticket_type == "kid":
            kid_ticket += 1

        if tickets_sold == available_seats:
            break
        ticket_type = input()

    print(f"{movie} - {tickets_sold / available_seats * 100:.2f}% full.")
    movie = input()

total_tickets = standard_ticket + student_ticket + kid_ticket

print(f"Total tickets: {total_tickets}")
print(f"{student_ticket / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_ticket / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_ticket / total_tickets * 100:.2f}% kids tickets.")
