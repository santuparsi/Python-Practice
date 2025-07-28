# For Loops

# for loops iterate over elements in a sequence (list, tuple, dict)
# outputs all elements from sequence

print('For Loops')
for i in range(0,11,2):
    print(i, end=' ')
print()

num = list(range(5))
for i in num:
    print(i, end=' ')
print()
print()

nest = [1, 2, 3, 
        ['cat', 'dog', 'bird'],
        [1.5, 'hello', True, 5]]

for item in nest:
    if type(item) == list:
        for i in item:
            print(i, '<- inner list item')
    else:
        print(item, '<- outer list item')
print()

tup = ((1, 2, 3), ('a', 'b', 'c'), (1.5, 2.5, 3.5))
for x, y, z in tup:
    print('{} - {} - {}'.format(x, y, z))
print()

d1 = {'k1': ('chocolate', 'vanilla', 'butterscoth'), 'k2': [1, 2, 3]}

for i in d1:
    print(type(d1[i]))
    for j in d1[i]:
        print(i, ':', j)
    print()