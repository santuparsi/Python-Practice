# Try, Except, and Finally

# Python will output different types of error notifications. These include:
#     - TypeError
#     - NameError
#     - AttributeError
#     - IndentationError
#     - SyntaxError
# Python allows us to manage the output error instead of relying on python itself.
# This is where Try, Except, and Finally comes in.
# These clauses can prevent errors from being fatal to our code.



def sum():
    try:
        v1, v2 = input("Enter two numbers: ").split()
        print(int(v1) + int(v2))
    except ValueError:
        print("Please enter valid numbers as input...!!!")
        sum()

sum()

def friends():
    animals = ('bird', 'cat', 'dog', 'cow', 'pig', 'horse')
    try:
        num = int(input('Please select a friend: '))
        try:
            print(animals[num])
        except:
            print('You did not choose a friend !!!')
        finally:
            print('_______________________________')
            for pet in animals:
                print(pet)
            print('_______________________________')
    except:
        print('You did not enter a valid index !!!')

friends()
