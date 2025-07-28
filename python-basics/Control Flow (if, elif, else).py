# IF, ELSE, ELIF

# Adds logic to our code
# The if statement performs the task if the condition is true.
# The else statement performs a default when the if statement's condition is false.
# Else statements cannot exist on their own.
# The elif statement (short for else if) works in between if and else statements.
# Elif only performs a task when true, and the if statement is False.

a = 10; b = 25; c = 100; d = ("cat", "dog", "bird")

# if statement
if a == 10:
    print('IF statement with one condition')

# if statement with 2 conditions
if a == 10 and b < 40:
    print('IF with two conditions')

# nested if statement
if a == 10:
    if b < 40:
        print('Nested IF statement')

# if/else statement
if a == 20 and b < 40:
    print('This statement will not be printed')
else:
    print('IF/ELSE statement')

# nested if/else statement
if a ==10:
    print('a is true')
    if b < 40:
        print('b is true')
    else:
        print('b is false')
else:
    print('a is false')

if 'cat' in d:
    print('cat is in tuple')
else:
    print('cat is not in tuple')

# elif statements
print()
num = int(input('Enter a Number:- '))

if num >= 3:
    print('Keep Looking !')
else:
    print('Found a {}'.format(d[num]))