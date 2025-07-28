##   Strings and Len
##
##  Strings
##  Letters and numbers in a string are called elements
##  String are immutable
##
##  Len
##  Built-in Python function or method
##  Counts the number of elements in a string, list, set or dictionary


a = 'hello'
b = 'world'

print("Example of 'sep' and 'end':-")
print(a, b, sep=", ", end=" !!")
print()
print("Quote inside quote: ", "'",a,"' '",b,"'", sep="")
print()

print("Length of variable a is",len(a))
print("Capitalize -", a.capitalize(), b.capitalize())
print("Uppercase -", a.upper(), b.upper())
print("Lowercase -", a.lower(), b.lower())
print()

print("Example of 'eval':-")
num = 10
print("Number is " + str(num))
print(str(num)+' + "10" = ', num + eval("10") )
print()

print("Example of 'count':-")
print("letter 'o' occours in 'hello' ", a.count('o'), "times")
print("letter 'H' occours in 'hello' ", a.count('H'), "times")
print("letter 'l' occours in 'hello' ", a.count('l'), "times")
print()

print("Example of 'replace':-")
messy = """HELLO @THERE,
THIS IS A#
#STRING WITH#
MU@LTI LINES """
print()
print(messy)
print()
print(messy.replace("#", "").replace("@", "").replace("\n", " ").capitalize())
print()

pet = 'cat'
print("The 0 index of 'pet' is", pet[0])

