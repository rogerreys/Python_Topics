# Create class
class myClass:
    x = 3
# Create a Objetc
c = myClass()
print(c.x)

# __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Roger",23)
print(p1.name, p1.age, sep=" - ")

# Object Methods
class Car: 
    def __init__(self, nombre, marca):
        self.nombre = nombre
        self.marca = marca
    def myMethod(self):
        print(self.marca, self.nombre, sep=" -- ")

c = Car("Metro", "Susuki")
c.myMethod()

# Delete Object Properties
#del c.nombre
#c.myMethod() 

# Inheritance
class Moto(Car):
    def __init__(self, motor, nombre, marca):
        super().__init__(nombre, marca)
        self.motor = motor

    def getMoto(self):
        print(self.motor)

m = Moto("3000M","Tuxton","BMW")
m.myMethod()
m.getMoto()

