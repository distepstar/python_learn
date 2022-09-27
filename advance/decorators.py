import time

# Decorators
def my_decorator(function):
    # adding agrs and kwargs to allow arguments pass in to the wrapper
    def wrapper(*args, **kwargs):
        print("I am decorating your function!")
        return_value = function(*args, **kwargs)
        return return_value
    return wrapper

# using annotation to call decorator
# what if the function has parameters inside it?
@my_decorator
def hello_world(person):
    print(f"Hello {person}!")
    return f"Hello World! {person}"

# Executing the wrapper function inside the my_decorator function
# this is not the typical way to call the decorators in python
print(hello_world("Louis"))

print("\n")
print("practical example #1 - logging")
# practical example #1 - logging
def logged(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open("logfile.txt", 'a+') as f:
            fname = func.__name__
            print(f"{fname} return value {value}")
            f.write(f"{fname} return value {value}\n")
        return value
    return wrapper

@logged
def add(x, y):
    return x + y

print(add(10, 20))


print("\n")
print("practical example #1 - logging")
# practical example #2 - Timing
def timed(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        after = time.time()
        fname = func.__name__
        print(f"{fname} took {after-before} seconds to execute")
        return value
    return wrapper

@timed
def my_func(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result

# print(my_func(9000))
