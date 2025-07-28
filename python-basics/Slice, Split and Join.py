##  Slice, Split and Join

robot = "technologically"
consoles = "ps4 is cooler than xbox!"
code = "p1y2t3h4o5n6i7c8"
words = "I saw a cat jump over the moon and into the clouds"
paid = "I recieved a total of $5000"

print("Example of Slice, Split and Join:-")
print(robot[0:6])
print(robot[6:])
print(robot[10:14])
print(code[0::2])
print(code[1::2])
print(code[1::2][::-1])
print(code[1::2][::-2])
print(consoles.endswith('!'))
print(consoles[-17:-11])

var = words.split()
print(var[3:8:2])

s1 = slice(3, 8, 2)
var2 = words.split()[s1]
print(var2)
print(var[s1])
print(" ".join(var2))
print((" ".join(var2) + ' ' + " ".join(var[s1])).split())

print(paid.split("$"))
