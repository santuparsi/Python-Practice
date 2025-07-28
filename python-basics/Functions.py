# Functions

# Reduces the amount of code
# Can be called anywhere
# Functions must be given a name
# Can contain multiple parameters or none at all
# A parameter can have default values

def addWithArgs(num1, num2):
    print(num1+num2)

addWithArgs(5, 3)

def addWithReturn(num1, num2):
    return num1 + num2

result = addWithReturn(5, 3)
print(result)

def addWithDefaultArgs(num1, num2=3):
    return num1 + num2

result = addWithDefaultArgs(5)
print(result)

def funcWithMultipleReturs(num1, num2):
    """This function returns sum and product of parameters"""       # This line documents the function, describes its purpose...
    return  num1 + num2, num1 * num2

result = funcWithMultipleReturs(5, 3)       # Doc string is visible in parameter section
print(result)