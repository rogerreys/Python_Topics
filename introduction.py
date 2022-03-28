#Comando
print('hello word')



#TIPOS DE DATOS
print('\n\nTIPOS DE DATOS')

    #numero
print(type(3))

    #float
print(type(5.6))

    #boolean
print(type(True))

    #list->si pueden cambiar
print(type([10,34,12]))
print(type(['php','js','python']))
print(type([10,'euros',True]))

    #Tuples->para datos que no cambian
tuples = (10,20,30,35) #Inmutable
print(type(tuples))

    #Dictorionies
dicto = {
    #key : value
    "nombre": "Roger",
    "lastname": "Reyes",
    "nickname":"Ryes",
    "age":23
    }
print(type(dicto))
    
    #None
print(type(None))


#VARIABLES
print('\n\nVARIABLES')
string_one = "valor de string"
num = 43
flo = 432.12
print('\n'+string_one, num, flo)

     #Case sensitive
valor = "variables"
Valor = "diferentes"
    #Asignar variables 1er metodo
x = 100
book = "I am robot"
    #Asignar variables 2er metodo
x, book = 100, 'I am robot'
print(x,book)

    #Conventiones
book_name = "I Robot" #Snake Case
bookName = "Digital fortres" #Camel case
BookName = "Interestellar" #Pascal Case
    #En python se recomienda usa mas Snake Case

    #Valor constante (TODO EN MAYUSCULAS), es otra Convention
PI = 3.141516
MY_NAME = 'Roberto'



#STRING
print('\n\nSTRING')
myStr = "Hello word, everyone"
print(dir(myStr))
print(myStr.upper())
print("title: ",myStr.title())
print("lower: ",myStr.lower())
print("swapcase: ",myStr.swapcase())
print("capitalize: ",myStr.capitalize())
print("replace: ", myStr.replace('Hello','bye' ).upper())
print("count: ",myStr.count('l'))
print("startswith ",myStr.startswith('hello'))
print("startswith: ",myStr.startswith('He'))
print("endswith: ",myStr.endswith('word'))
print("endswith: ",myStr.endswith('rd'))
#Dividir
print(myStr.split(','))
print(myStr.split('o'))
#Buscar
print("find: ",myStr.find('o'))
#Len
print("len: ",len(myStr))
#indice
print("index: ",myStr.index('H'))
#identificar
print("Is numeric: ",myStr.isnumeric())
print("Is alfanum: ",myStr.isalnum())
#caracter
print(myStr[7])
print(myStr[-4])
#concatenar
name = "Ryes"
print(f"hello {name}")
print("hello {}".format(name))
#Concatenar list o tutle
print("Concatenar list o tutle".upper())
lista = list(("Concatenar","list","a","string"))
print("#".join(lista))


#NUMBERS
print('\n\nNumber')
num_int = 10
print(type(num_int))
num_float = 14.2    
print(type(num_float))

    #suma
print(4+1)
print(5+19.2)

    #resta
print(4-1)
print(5-19.2)

    #multiplicacion
print(4*1)
print(5*19.2)

    #division
print(4/1)
print(5/19.2)

    #exponencial
print(4**2)

    #modulo
print(3/2)
print(3//2, "o", 3%2)

    #table de presendenca
print(20-10/2*3**2)
print((20-10)/(2*3**2))

    #Insertar
age = input("Ingresar edad:")
print(type(age))
age = int(age)

new_age = age **2
print(new_age)



#CONVERSION
print('\n\nCONVERSION')
print(type(int("10")))
print(type(float("10.10")))
print(type(str(10)))



#LIST
print('\n\nLIST')
demo_list = [1,'hello',1.23,True,[1,2,3]]
colors = ['red','blue','green']
print('colors is: ',type(colors))
print('posicion de colors 1: ',colors[1])
    #constructor
number_list = list((1,2,3,4)) #Utilizo tupla para crar list
print(number_list)

    #range
rango = list(range(1,100,5))
print(len(rango))
    #Si existe un elemento de una lista
colors = ['red','blue','green']
print('Existe:','green' in colors) #Existe green en colors
print('Existe:','black' in colors) #Existe black en colors
    #Agregar
colors[2] = 'black'
print('Existe: ','black' in colors)
print(colors)
    #metodos en list
print(dir(colors))
#colors.extend(('white','violet')) #ó colors.extend(['white','violet'])
    #Agregar en indice
colors.insert(1,'brown')#indica la posicion
colors.insert(len(colors),'lightblue')#indica la posicion
print(colors)
    #eliminar por indice o ultimo
colors.pop() 
colors.pop(3)
print("pop: ",colors)
    #eliminar por nombre
colors.remove('red') #por nombre
print("remove: ",colors)
    #eliminar todo
#colors.clear();
print(colors)
    #Ordenar
colors.extend(["yellow",'lightred','black'])
print('extend: ',colors);
colors.sort()
print('sort:',colors)
colors.reverse()
print('reverse: ',colors)
    #Obtener indice
print(colors.index('yellow'))
    #contar
print(colors.count('black'))

#List Comprehensions
print("\n\nList Comprehensions".upper())
#[expression-involving-loop-variable "for" loop-variable in sequence ]
print("With for")
ListOfNumbers = [ x for x in range(10) ] # List of integers from 0 to 9
print(ListOfNumbers)

#[ expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ]
print("With in")
print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])

#[ expression-involving-loop-variable for loop-variable in sequence if boolean-expression-involving-loop-variable ]
print("With for, in and if")
ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples
print(ListOfThreeMultiples)


#NESTED LISTS
print('\n\nNESTED LISTS')
#A nested list is a list that contains another list
nested_list = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]
print(nested_list)
print(nested_list[1])
print(nested_list[0][1])




#TUPLES
print('\n\nTUPLES')
tup = (1,2,3)
print(tuple((4,5,6)))
print(dir(tup))
print(tup[0])
print(tup)
    #Eliminar 
#del tup
#print(tup)
    #Ejemplo de uso
location = {
        "tokyo": (12.43,123.12),
        "paris": (0,0)        
    }



#SET #Conjunto de datos desordena sin indice
print('\n\nSET')

colors = {"red","green","blue"}
print(dir(colors),'\n')
print(type(colors))
print('red' in colors)
#Agregar
print(colors)
colors.add('violet')
print('add: ',colors)
#Remover
colors.remove('green')
print('remove:',colors)
#clear
colors.clear() #o del colors
print('clear: ',colors)




#DICTIONARIES
print("\n\nDICTIONARIES")
product = {
        'name': 'book',
        'quatity':3,
        'price':4.99
        }
person = {
    'name': 'Ryan',
    'lastname': 'Ray'
    }
print(type(product))
print(dir(person),'\n\n')
print('keys: ',person.keys())
print('items: ',person.items())

#elminar
#del person # o person.clear()

print("\n")
cars = [product, person]
print('list_with_dictionaries:',cars)




#CONDICIONES
#IF
print('\n\nCONDICIONES')
print('\nIF')
x = int(input("Valor de x:"))
if x == 10:
    print(f'{x} es mayor o igual a 10')
elif x > 10:
    print(f'{x} es mayor a 20')
elif  x < 10:
    print(f'{x} es menora 10')    

#OPERADORES LOGICOS
    #and
    #or
    #not
print('\nOPERADORES LOGICOS')
if x >= 10 and x <= 20:
    print(f'10<{x}<20')
elif x > 0 and x < 10:
    print(f'0<{x}<10')
else:
    print(f'{x}<0')


#FOR and WHILE
print('\n\nFOR\n')
food = ['apples', 'bread', 'cheese','milk']
for x in food:
    if x == 'cheese':
        continue;
    print(food.index(x),x);

print('\n\n');
for x in range(0,10,2):
    print(x)

print('\n\n');

    
print('\n\nWHILE\n')
count = 0
while count <=10:
    print(count)
    count = count+1
    if(count == 5):
        break;

    
#FUNCIONES
print('\n\nFUNCIONES\n')

def operacion(x=1, y=1):
    result = ""
    result = result+'suma:'+ str(x+y)+'\n'
    result = result+'resta:'+ str(x-y)+'\n'
    result = result+'multi:'+ str(x*y)+'\n'
    if y > 0:
        result = result+'div:'+ str(x/y)+'\n'
    else:
        result = result+'div: y debe ser mayor a 0''\n'
    return result

print(operacion(3,2))
print(operacion())
print(operacion(3,0))

print('\nFunction lambda\n')
hi = lambda param1, param2: 'hello '+param1+' '+param2

print("function lambda: ",hi('roger','reyes'))




#MODULOS
print('\n\nMODULOS\n')
#3 MODULO
#own modules
#thirdy party modules (por otros)
#python modules
    #1 Metodo
import datetime
print(datetime.date.today())

    #2 Metodo
#from datetime import timedelta
#print(timedelta(minutes=100))

    #Own module
    #file1: pmath
#def add(n1,n2):
#    print(n1+n2)

#def subtract(n1,n2):
#    print(n1-n2)
    
#file2: index
    #Metodo 1
#import pmath
#pmath.add(1,2)
    #metodo 2
#from pmath import add, subtract
#add(1,2)
#subtract(1,2)

#REGULAR EXPRESSION (RegEx)
#
#
#matching.
print('\n\nREGULAR EXPRESSION (RegEx)')
text=("A regex is a sequence of characters that defines a"
      " search pattern, mainly for the use of string pattern"
      " matching")
print(text+"\n")

import re
print("re.search","""\
expression scans through a string looking for the
first location where the regex pattern produces a match.""","\n")

print("search",re.search(r"ly","similarly"),"\n")

print("re.match","""\expression only matches at the beginning
    of the string.""" "\n")
print("match",re.match(r"ly","ly should be in the beginning"))



#EVAL
print("\n\neval() FUNCTION")
x = "print('Ejecutar un string')"
eval(x)













    
        
