# Built-in Functions

# Built-in Python Functions are always available on command
# As of python 3.6 there are a total of 68 Built-in Functions.

# print(help(print))      # find help about any function

import random as rd

numbers = rd.sample(range(10, 100), k=10)
print(numbers)

print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(round(10.12345, 3))
print(abs(-15.5))
print(eval("10.22"))
print(pow(5, 2))
print()

new_numbers = sorted(numbers)
print(new_numbers)
print([pow(x, 2) for x in new_numbers])