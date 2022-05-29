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


# Variable

## Global Keyword
If you need to create a global variable, but are stuck in the local scope

    def myfunc4():
    global ab
    ab = 300

# Date

    import datetime

    x = datetime.datetime.now()
    print(x.year)
    print(x.strftime("%A")) 

    # Creating Date Objects
    y = datetime.datetime(2020, 3, 23)
    z = datetime.datetime(x.year, x.month, 23, 10,30)

The strftime() Method
https://www.w3schools.com/python/python_datetime.asp

# Write File
Additional modes  
r+ : Reading and writing. Cannot truncate the file.
w+ : Writing and reading. Truncates the file.
    opening a file in w+ overwrites it and deletes all pre-existing data
a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab.

To work with a file on existing data, use r+ and a+

.tell() - returns the current position in bytes
.seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to beginning, relative to current position and end

    # Write
    values = ["First Line A\n", "Second Line B\n", "Third Line C\n"]
    with open(ruta+"file.txt","w") as fileWrite:
        for i in values:
            fileWrite.write(i)

    # Append
    with open(ruta+"file.txt","a") as fileAppend:
        print("Value {}".format(fileAppend.tell())) 
        fileAppend.seek(0,0)
        fileAppend.write("Line append")

    # Copy File
    with open(ruta+"file.txt","r") as fileReadable:
        with open(ruta+"file2.txt","w") as fileCopied:
            for i in fileReadable:
                fileCopied.write(i)