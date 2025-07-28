##    Lists and Range

##    A list contains sequence of values in []
##    Each value can be float, int, or string
##    Each value in list is called an element
##    List can contain:
##        Nested lists
##        Tuples
##        Dictionaries
##        And much more
##
##    Mutable
##
##    Elements in a list and dictionaries are mutable
##    Elements in a tuple or string aren't mutable
##
##    Range generated a specefied list of numbers
##    Used with loops

print(list(range(11)))
print(list(range(5, 11)))
print(list(range(0, 22, 2)))

num = [2, 5, 3, 7, 4, 10]
print(type(num))
print(num)
num.sort()
print(num)
num.reverse()
print(num)

items = ["cars", "bike", "plane"]
print(items)
items.append(num)
print(items)
items[3].insert(2, ["hello"])
print(items)
print(items[0])
print(items[3])
print(items[3][2])
print(items[3][2][0])
