# Lambda Expressions

# Lambda is called an anonymous function, meaning it does not require a def name.
# Does not require a return.
# Lambdas are single line Expressions.
# Can only be used as a substitute for basic functions.
# Cannot add a doc string.


def add(v1, v2):
    return v1 + v2
print(add(10, 20))


sum = lambda v1, v2: v1 + v2
print(sum(10, 20))


def check(num):
    return num % 2 == 0 or num > 8
print(check(5))


chk = lambda num: num % 2 == 0 or num > 8
print(chk(13))


def compare(v1, v2):
    if v1 > v2:
        return  v1
    else:
        return v2
print(compare(10, 20))


comp = lambda v1, v2: v1 if v1 > v2 else v2
print(comp(10, 20))

