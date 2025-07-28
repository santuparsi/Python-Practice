# List Comprehension

# List Comprehension is an elegant way to define and create a list in python
# relies heavily on for loops
# significantly reduces lines of code


v1 = []
for i in 'hello':
    v1.append(i)
print(v1)

v2 = [i for i in 'world']
print(v2)

print([i for i in v2].values)
