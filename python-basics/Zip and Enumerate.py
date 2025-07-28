# Zip and Enumerate

# zip can combine elements from two or more lists into nested tuples
# enumerate can generate a integer number next to each output


for count, i in enumerate(range(10, 40, 5)):
    print(count, i)
print()

tup1 = (10, 20, 30, 40)
list1 = [1, 2, 3, 4]
z = zip(tup1, list1)
print(dict(z))
print()


z = zip(tup1, list1)

for i, j in z:
    print(i+j)
print()

# Unzip example:

z = zip(tup1, list1)

i, j = zip(*z)

print(i, j, sep='\n')
print()

a = ['a', 'b', 'c', 'd']
b = [1, 2, 3, 4]

for i, j in zip(a, b):
    print(i + '=' + j)

