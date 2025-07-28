# Arbitrary Keyword Arguments, **args
# If the number of keyword arguments is unknown, 
# add a double ** before the parameter name
def my_function(**player):
    print('His last name is: '+player['lname'])
my_function(fname='Sachin',lname='Tendulkar')