toys = {'robot': '$40.0', 'car': '$25', 'ironman': '$12'}
sum = 0

for i in list(toys.values()):
    sum += eval(i[1:])

print(toys)
print('Sum of values of dict ->', int(sum))