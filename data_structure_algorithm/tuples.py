# Tuples
""" 
Tuples are: 
# Immutable (can't add / change)
# Useful for fixed data
# Faster than lists
# Sequence type
"""

# constructors - creating new tuples
x = ()
x = (1, 2, 3)
x = 1, 2, 3
x = 2, 
print(x, type(x))

# converting list to tuple
list1 = [2, 4, 6]
x = tuple(list1)
print(x, type(x))

# tuples are immutable, but member objects may be mutable
x = (1, 2, 3)
# del(x[1]) # fails
# x[1] = 8  # fails
print(x)

y = ([1, 2], 3) # a tuple where the first item is a list
del(y[0][1])    # delete the 2  # this will be work
print(y)
y += (4, )      # concatenating two tuples work
print(y)