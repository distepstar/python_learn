# List
# creating new list
x = list()
y = ['a', 25, 'dog', 8.43]
tuple1 = (10, 20)
# converting tuple to list
z = list(tuple1)

# list comprehension
# create a list filled with 0 to 7
a = [m for m in range(8)]
print(a)
# n**n -> sqrt -> 5**2 -> 5 * 5 = 25
b = [i**2 for i in range(10) if i > 4]
print(b)

# delete -> delete item from list
x1 = [5, 3, 8, 6]
del(x1[1])
print(x1)
# delete entire list
del(x1)

# append -> add item to list
x2 = [5, 3, 8, 6]
x2.append(7)
print(x2)

# extend -> append a sequence to a list -> merge list
x3 = [5, 3, 8, 6]
y3 = [12, 13]
x3.extend(y3)
print(x3)

# insert -> insert an item at a given index
x4 = [5, 3, 8, 6]
x4.insert(1, 7)
print(x4)

# pop -> pops last item off list and returns item
x5 = [5, 3, 8, 6]
x5.pop()
print(x5)

# remove -> remove first instance of an item
x6 = [5, 3, 8, 6, 3]
x6.remove(3)
print(x6)

# sort - sort the list in place
# Note:
# sorted() returns a new sorted list without changing the original list.
# x.sort() pust the items of x in sorted order (sorts in place)
x7 = [5, 3, 8, 6]
x7.sort()
print(x7)


# reverse sort - just like the name -> sort and reverse
x8 = [5, 3, 8, 6]
x8.sort(reverse=True)
print(x8)