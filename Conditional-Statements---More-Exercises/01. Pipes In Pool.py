volume_of_pool_liters = int(input())
pipe1_liters_per_hour = int(input())
pipe2_liters_per_hour = int(input())
worker_hours_out = float(input())

liters_filled = pipe1_liters_per_hour * worker_hours_out + pipe2_liters_per_hour * worker_hours_out

if liters_filled > volume_of_pool_liters:
    overflow = liters_filled - volume_of_pool_liters
    print(f"For {worker_hours_out} hours the pool overflows with {overflow:.2f} liters.")

if liters_filled <= volume_of_pool_liters:
    pipe1_filled_percent = (pipe1_liters_per_hour * worker_hours_out) / liters_filled * 100
    pipe2_filled_percent = (pipe2_liters_per_hour * worker_hours_out) / liters_filled * 100
    liters_filled_percent = liters_filled / volume_of_pool_liters * 100
    print(f"The pool is {liters_filled_percent}% full. \
Pipe 1: {pipe1_filled_percent:.2f}%. Pipe 2: {pipe2_filled_percent:.2f}%.")
