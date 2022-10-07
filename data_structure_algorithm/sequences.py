# ---------------------------------------------------

# Sequences can be access in String, List Tuple
# String


print('\n')
print("Sequences")
x = "frog"
print(x[3])

# list
x = ["pig", "cow", "horse"]
print(x[2])

# tuple -> immutable, can only access only
x = ("Kevin", "Niklas", "Jenny", "Craig")
print(x[0])

# ---------------------------------------------------

# adding / concatenating - combine 2 sequences of the same type by using +
# string
print('\n')
print("Adding / Concatenating")
x = 'horse' + 'shoe'
print(x)

# list
y = ['pig', 'cow'] + ['horse']
print(y)

# tuple
z = ('Kevin', 'Niklas', 'Jenny') + ('Craug',)
print(z)

# ---------------------------------------------------

# Multiply - multiply a sequence using *
print('\n')
print("Multiplying")
x = 'bug' * 3
print(x)

# list
y = [8, 5] * 3
print(y)


# tuple
z = (2, 4) * 3
print(z)

# ---------------------------------------------------

# slicing - slice out substrings, sublists, subtuples using indexes
# [start: end+1: step]
print('\n')
print("Slicing")


x = 'computer'
print(x[1:4])
print(x[1:6:2])
print(x[3:])
print(x[:5])
print(x[-1])
print(x[-3:])
print(x[:-2])

# ---------------------------------------------------

# checking membership - test whether an item is or is not in a sequence
print('\n')
print("Checking Membership")

x = 'bug'
print('u' in x)

# list
y = ["pig", "cow", "horse"]
print('cow' not in y)

# tuple
z = ("Kevin", "Niklas", "Jenny", "Craig")
print('Niklas' in z)

# ---------------------------------------------------

# iterating - iterating through the items in a sequence
print('\n')
print("Iterating")

x = [7, 8, 3]
for item in x:
    print (item)

# index & item
y = [7, 8, 3]
for index, item in enumerate(y):
    print(index, item)


# ---------------------------------------------------

# number of items
print('\n')
print("Length of items")

# string
x = 'bug'
print(len(x))

# list
y = ['pig', 'cow', 'horse']
print(len(y))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craug')
print(len(z))