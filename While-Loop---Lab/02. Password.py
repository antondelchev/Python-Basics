name = input()
password = input()

current_input_pass = input()

while current_input_pass != password:
    current_input_pass = input()

print(f"Welcome {name}!")
