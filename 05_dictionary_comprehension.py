# SIN dictionary comprehension
dicc = {}
for i in range(1, 11):
    dicc[i] = i*2
print(dicc)

# CON dictionary comprehension
x = { i:i*2 for i in range(1,11) }
print(x)


# EXAMPLE 1
import random
count = ['col', 'mex', 'bol', 'pe']
population_v1 = {}
population_v2 = {}

for i in count:
    population_v1[i] = random.randint(100, 1000)
print(population_v1)

population_v2 = {i:random.randint(100, 1000) for i in count}
print(population_v2)


# EXAMPLE 2
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98 ]

firts_way = {names[i]:ages[i] for i in range(0, len(names))}
print(firts_way)

print(list(zip(names, ages)))
second_way = {name:age for (name, age) in zip(names, ages)}
print(second_way)