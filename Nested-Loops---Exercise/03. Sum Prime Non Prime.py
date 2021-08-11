num_or_command = input()

sum_prime = 0
sum_non_prime = 0

while num_or_command != "stop":
    number = int(num_or_command)
    counter = 0
    if number < 0:
        print("Number is negative.")
    else:
        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1
        if counter > 2:
            sum_non_prime += number
        else:
            sum_prime += number
    num_or_command = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
