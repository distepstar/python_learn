# List
from types import new_class


x = [4, True, 'hi']
x.append('world')
x.extend([4,5,5,5,5,5])

# copy list
print("\nCopy List")
y = x[:]
print(x)
print(y)
print(len(x), len(y))


# tuple (immutable list -> cannot be changed after defined)
print("\nTuple and loops")
z = (0, 0, 2, 2)
# range function -> range(stop) / range(start, stop) / range(start, stop, step)
for i in range(len(z) - 1, 0, -1):
    print(z[i])

# list obj loop
for i, element in enumerate(z):
    print(f"Index: {i} Variables: {element}")

# slice
print("\nSlice")
values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# parameters same as range func [start:stop:step]
# arr[::stop] -> start at the beginning and stop
sliced = values[0:4:2]
print(sliced)


# Set
print("\nSet")
# empty set create
mySet = set()
# set literal
newSet = {4, 32, 2, 2}
newSet2 = [4, 32, 2, 2]

# dictionary
dict = {}
# add
newSet.add(2)
print(newSet)
# remove
newSet.remove(2)
print(newSet)
# check if exist (arr or set)
print(2 in newSet2)
print(32 in newSet)
# union, diff, intersect
set1 = {1, 2, 4, 16, 32}
set2 = {2, 6, 12, 32, 36}
# merge two sets
print(f"Merge: {set1.union(set2)}")
# intersect (find commons)
print(f"Common: {set1.intersection(set2)}")
# diff (find differences)
print(f"Diff: {set1.difference(set2)}")

print("\nDictionary")
# key value (hashmap)
dict1 = {'key': 4}
dict1['key2'] = 5
dict1[2] = 8
print(dict1)
# print values (convert dict_values to list)
print(list(dict1.values()))
# remove key
del dict1[2]
print(dict1)
# loop through dict
for k, v in dict1.items():
    print(k, v)


print("\nComprehensions")
# polyfill array
newArr = [i for i in range(5)]
print(newArr)

# polyfill array with even numbers
newArr2 = [i for i in range(100) if i % 2 == 0]
print(newArr2)


print("\nagrs & **kwargs")
def func(x):
    def func2():
        print(x)
    return func2

x = func(4)
x()

def func3(x, y):
    print(x, y)
pairs = [(1,2), (3,4)]

for pair in pairs:
    # two asterix for dict **
    func3(**{'x': 2, 'y': 5})

x = [1, 23, 236363 ,2727]
# * unpack operators -> separate elements
print(x)
print(*x)

# args = arguments that passe to the func, kwargs = keyword arguments
def func4(*args, **kwargs):
    # unpack
    print(*args, *kwargs)

func4(1, 2, 3, 4, 5, one=0, two=1)


print("\nScope & Globals")
x = 'tims'

def func5(name):
    # use global variables
    global x
    x = name

func5("Louis")
print(x)
print("\nExceptions")
# raise Exception("Bad")
# try except(try catch)
try:
    x = 7/0
except Exception as e:
    print(e)
finally:
    # no matter what's the result -> run this
    print("final")

print("\nLambda expression")

# lambda function
# lambda parameter: action
x = lambda x: x + 5
print(x(2))

print("\nMap and filter")
x = [x for x in range(10) if x % 2 == 0]
# map(function, parameter)
mp = map(lambda i: i + 2, x)
print(list(mp))
fil = filter(lambda i: i % 3 == 0, x)
print(list(fil))

