import random as rd


print(rd.random())
print(rd.randint(1, 6))
print(rd.randrange(10, 100, 10))
print(rd.uniform(2, 3))
print()

animals = ["\N{cat}", "\N{dog}", "\N{snake}", "\N{horse}"]      # Prints emojis / works in web
rd.shuffle(animals)
print(animals)
print()

heroes = ['Batman', 'Captain America', 'Spiderman', 'Ironman']
villians = ['Joker', 'Red Skull', 'Venom', 'Thanos']

rd.shuffle(heroes)
rd.shuffle(villians)

for i in range(4):
    print(heroes[i], 'VS', villians[i])
print()


students = ['a', 'b', 'c', 'd', 'e']
probability = [0.3, 0.3, 0.1, 0.1, 0.2]         # chances of appearance
print(rd.choices(students, probability, k=3))   # k mean how many values, can be more than len of list
print()

print(rd.sample(range(10), k=3))