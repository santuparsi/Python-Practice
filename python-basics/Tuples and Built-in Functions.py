# Tuples

# Similar to a list in that it contains a collection of elements in ()
# Elements in a Tuple are immutable
# Only has two functions index and count

# Built-in functions:
# max
# min
# sum
# sorted


tup1 = 20, 30, 10, 40
print("tup1 -> ", tup1)
print("typeof -> ", type(tup1))
print()

mylist = [10, 20, 30, 40]
print("mylist -> ", mylist)
print("typeof -> ", type(mylist))
print()

tup2 = tuple(mylist)
print("tup2 = tuple(mylist)")
print("tup2 -> ", tup2)
print("typeof -> ", type(tup2))
print()

tup3 = tup1 + tup2
print("tup3 = tup1 + tup2")
print("tup3 -> ", tup3)
print()

tup4 = "cat", "cat", "cat", "dog", "dog", 1, 1, 2, 3, False
print("tup4 -> ", tup4)
print('tup4.count("cat") -> ', tup4.count("cat"))
print('tup4.count(1) -> ', tup4.count(1))
print('tup4.count(False) -> ', tup4.count(False))
print()

print("tup1.index(10) -> ", tup1.index(10))
print("sum(tup1) ->", sum(tup1))
print("max(tup1) ->", max(tup1))
print("min(tup1) ->", min(tup1))
print("sorted(tup1) ->", sorted(tup1))