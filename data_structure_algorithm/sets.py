# Sets
"""
Sets are:
# Store non-duplicate items
# Very fast access vs List
# Math Set ops (union, intersect)
# Sets are Unordered -> you cannot sort a set
"""

# constructors - creating a new sets
x = {3, 5, 3, 5}
print(x)

# create an empty set
y = set()
print(y)

list1 = [2, 3, 4]
z = set(list1)
print(z)

# set operations
x = {3, 8, 5}
print(x)
# add item to set
x.add(7)
print(x)


# remove item
x.remove(5)
print(x)

# get length of set x
print(len(x))

# check membership in x
print(5 in x)

# pop random item from set x
print(x.pop(), x)

# delete all items from set x
x.clear()
print(x)

print("\n")
print("Mathematical set operations")
# Mathematical set operations
"""
# Intersection (AND): set1 & set2
# Union (OR): set1 | set2
# Symmetric Difference (XOR): set1 ^ set2 difference (in set1 but not in set2): set1 - set2
# Subset (set2 contains set1): set1 <= set2
# Superset (set1 contains set2): set1 >= set2
"""
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
print(s1 - s2)
print(s1 <= s2)
print(s1 >= s2)