#SENTENCIA IF
print("____IF___")
x = int(input("Ingresar valor: "))
if x<0:
    print("valor de x menor a cero: ",x)
elif x == 0:
    print("valor de x es igual a ",x," (cero)")
elif x == 1:
    print("valor de x es igual a ",x," (uno)")
else:
    print("valore mayor a cero:",x) 

#SENTENCIA FOR
print("____FOR___")
animales = ["gato", "perro", "tortuga"]
for animal in animales:
    print(animal, len(animal))


# Strategy:  Iterate over a copy
#for user, status in users.copy().items():
#    if status == 'inactive':
#        del users[user]

# Strategy:  Create a new collection
#active_users = {}
#for user, status in users.items():
#    if status == 'active':
#        active_users[user] = status

#SETENCIA RANGE
print("____RANGE___")
for y in range(10):
    print(y)

#inicio, fin, salto
print("range parametros")
for y in range(0,10,2):
    print(y, end="\n")

#para string
valor = ["Numero","de","caracteres","recorridos","por","for y range"]
for i in range(len(valor)):
    print(i," ",valor[i])

#funcion sum con range
print("____SUM CON RANGE___")
print(sum(range(4)))
#0+1+2+3

#listar un range
print(list(range(2,4)))

#Declaracion break
print("\nDeclaracion break")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
        # loop fell through without finding a factor
            print(n, 'is a prime number')

#Declaracion continue 
print("\nDeclaracion continue")
for x in range(2,10):
    if x%2 == 0 :
        print("numero par")
        continue
    print("numero impar")

#SETENCIA PASS
print("\n____PASS___")
#while True:
#    pass

#DEFINIENDO FUNCIONES
print("\n_____FUNCTION_____")
def fib(n):
    a, b = 0,1
    while a<n:
        print (a,end=",")
        a, b = b, b+a
    print()

#llamamos la funcion
fib(200)

#asignacion de funcion a variable
f = fib
f(100)

#funcion con retorno
def multPorDos(x):
    result = []
    for i in range(1,x):
        result.append(2*i)    
    return result

print(multPorDos(10))

#funcion por omision
#EJEMPLO1
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#ask_ok('Do you really want to quit?')
#ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

#EJEMPLO2
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
