# Dict (Hashmap)
"""
# Key/Values pairs
# Associative array, like Java HashMap
# Dicts are Unordered
"""
# Constructor
x = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
print(x)
# Converting list to dict
x = dict([('pork', 25.3), ('beef', 33.8) , ('chicken', 22.7)])
print(x)
# Converting tuple to dict
x = dict(pork=25.3, beef=33.8, chicken=22.7)
print(x)

# dict operations
x['shrimp'] = 38.2  # add or update
print(x)

# delete an item
del(x['shrimp'])
print(x)

# get length of dict x
print(len(x))

# delete all items from dict x
x.clear()
print(x)

# delete dict x
del(x)

# accessing keys and values in a dict
y = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
print(y.keys())
print(y.values())
print(y.items())    # key-value pairs

# check membership in y_keys (only looks in keys, not values)
print('beef' in y)

# check membership in y_values
print('clams' in y.values())    # False
print(22.7 in y.values())       # True


# iterating a dict
for key in y:
    print(key, y[key])

for k, v in y.items():
    print(k, v)