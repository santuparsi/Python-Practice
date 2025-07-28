name = "Mehul"
grade = "A+"

print("The Student's name is {} and grade is {}".format(name, grade))

animals = ["lions", "zebras", "tigers", "chetahs"]
safari = "I saw {}, {} and {} !"

for animal in animals:
    print("hello {},".format(animal))

print(safari.format(*animals))

nums = ["10", "20", "30", "40"]
oper = "{} + {} + {} + {}"

print(oper.format(*nums), end=" = ")
print(eval(oper.format(*nums)))

oper = "{0} + {1} + {1} + {1}"
print(oper.format(*nums), end=" = ")
print(eval(oper.format(*nums)))

print('%d * %d = %d' % (5, 3, (5*3)))
print('%d / %d = %.2f' % (5, 3, (5/3)))

word = "awesome"
print("The length of {} is {}".format(word, len(word)))

print("Days left are {num: .10f}".format(num = 300/9))
