# While Loops

# Similar to a for loop, while loops outputs each element, but based on a while statement being true.
# Once the while statement is no longer true, the while loop ends.

print('Numbers from 0 to 9:')
x = 0
while x < 10:
    print(x, end=' ')       # Prints 0 to 9
    x += 1
print()

num = int( input("Enter number for multiplication table: ") )
print('The multiplication table of %d:' % (num))
x = 1
while x <= 10:
    print('{} x {} = {}'.format(num, x, num*x))       # Prints multiplication of num
    x += 1

print('Even numbers from 0 to 10:')
x = 0
while x <= 10:
    if x % 2 == 0:
        print(x, end=' ')      # Prints even numbers from 0 to 10
    x += 1
print()

print('Inverted half pyramid using nested while loop:')
a = 1; b = 1
while a < 5:
    while b < 5:
        print('*', end=' ')
        b += 1
    print()    
    a += 1
    b = a

print('Half pyramid using while loop:')
x = 1
while x < 5:
    print('* ' * x, end=' ')
    print()
    x += 1