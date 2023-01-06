# SIN List comprehension
number = []
for el in range(1, 11):
    number.append(el*2)
print(number)

# CON List comprehension
x = [i for i in range(1, 11)]
y = [i*2 for i in range(1, 11)]
z = [i for i in range(1, 11) if i%2==0]
print(x,y,z)