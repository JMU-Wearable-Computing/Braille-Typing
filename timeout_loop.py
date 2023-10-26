import time

current_time = time.time_ns()
start_time = time.time_ns()

timeout = 10E9

print('Beginning timeout...')

while abs(current_time - start_time) < timeout:
    current_time = time.time_ns()

print('Done!')
