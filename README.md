# Python_Topics
<h1>Introduccion a Python</h1>

# Input
    n = int(input("valor1\n"))

# Control Flow

## Sentencia if

    if x<0:
        print("valor de x menor a cero: ",x)
    elif x == 0:
        print("valor de x es igual a ",x," (cero)")
    else:
        print("valore mayor a cero:",x) 

## Sentencia for

    animales = ["gato", "perro", "tortuga"]
    for animal in animales:
        print(animal, len(animal))

## Sentencia range

    for y in range(10):
        print(y)
    # 1,2,3,4,5,6,7,8,9

    # start, end, jump
    for y in range(0,10,2):
        print(y, end="\n")

## Sentencia While
    
    while a<n:
        print (a,end=",")
        a, b = b, b+a

# Function

    def fib(n):
        a, b = 0,1
        while a<n:
            print (a,end=",")
            a, b = b, b+a
        print()

    # call Function
    fib(200)


# lambda

    # lambda arguments : expression
    x = lambda a: a + 10
    print(x(5))  # 15

    # 
    def myfunc(n):
        return lambda a : a * n
    double = myfunc(n) # Function return lambda
