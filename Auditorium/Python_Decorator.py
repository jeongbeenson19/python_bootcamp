import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper():
        first_run = time.time()
        function()
        second_run = time.time()
        time_difference = second_run - first_run
        print(f"{function.__name__} run speed: {time_difference} ")

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


time.time()
fast_function()
slow_function()