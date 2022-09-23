# Generators
# Example - Seq 1, to 9,000,000

import sys

def my_generator(n):
    # example of yield 
    for x in range(n):
        # yield is similar to return statement, but it will return values or objects
        yield x ** 3

values = my_generator(100)
# get size of values in bytes
# print(sys.getsizeof(values))
# next keywords will give you the next yield state
# print(next(values))
# print(next(values))

# for x in values:
#     print(x)

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()

# this approach will not waste memory but keeps generating the numbers
# print(next(values))
# print(next(values))
# print(next(values))


for x in range(500):
    print(next(values))
