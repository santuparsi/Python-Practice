# Dictionaries

# Consists of keys and key values seperated by a colon.
# Dictionaries called dict can contain:

#     Strings and numbers
#     tuples
#     lists
#     sets
#     series
#     dataframes
#     nested dictionaries

d1 = {}
d2 = {1: 'A', 2: 'B'}
toys = {'cars': '$500', 'bike': '$300.5'}

print("type(d1) ->", type(d1))
print()

d1['A'] = 1
d1['B'] = 2

print('d1 ->', d1)
print('d2 ->', d2)
print('toys ->', toys)
print()

d1.update(toys)
print('d1.update(toys) ->', d1, '# Merge two dictionaries')

toys.clear()
print('toys.clear() ->', toys, '# Remove all items')

d1.pop('A')
print("d1.pop('A') ->", d1, '# Remove item with matching key')
print()

print('d1.values() ->', d1.values(), '# Returs the values in a list')
print('# Convert the values into list or tuple for indexing')
print('list(d1.values()) ->', list(d1.values()), '# Show all values in list')
print('list(d1.values())[1] ->', list(d1.values())[1], '# Show only value at index 1')
print()

print('d1.keys() ->', d1.keys(), '# Returs the keys in a list')
print('# Convert the keys into list or tuple for indexing')
print('list(d1.keys()) ->', list(d1.keys()), '# Show all keys in list')
print('list(d1.keys())[1] ->', list(d1.keys())[1], '# Show only key at index 1')
print()

print('d1.items() ->', d1.items(), '# Returns all items in list of tuples')
print()

menu = [('chips', 2.4), ('soup', 5.0)]
print("menu = [('chips', 2.4), ('soup', 5.0)]")
print('type(menu) ->', type(menu))
print('type(menu[0]) ->', type(menu[0]))
print('dict(menu) ->', dict(menu))
print('type(dict(menu)) ->', type(dict(menu)))
print()

maze = {'k1': {'cars': '$500', 'bike': '$300.5'},
        'k2': [10, 20, 30],
        'k3': ('tuple', [1, 2, {'k4': ['a', 'b', 'catch me!']}])}
print('type(maze) ->', type(maze))
print('maze ->', maze)
print("maze['k3'][1][2]['k4'][2] ->", maze['k3'][1][2]['k4'][2])