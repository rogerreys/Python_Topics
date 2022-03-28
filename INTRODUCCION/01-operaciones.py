#Division con retorno float
print(17/3)

#Division descartando parte fraccionaria
print(17//3)

#Operador resto %
print(17%3)

#Operador para potencias
print(5**2)

#La ultima variable expresa se le asigna a la variable "_"(guion bajo)
#print ( _ + 5)

#----------CADENAS
print("\n--CADENA-----------------------")
print("hola 'mundo'");
print("hola\mundo\nuevo");

    #Colocar la "r" para evitar la \
print(r"hola\mundo\nuevo");

    #Se puede agregar multiples lineas
print("""\
PRUEBA CON MULTIPLES LINEAS
---------------------------
Para esta prueba se puede utilizar
multiples lineas
""")

    #Concatenar con +  y repetir con *
print("Primera forma"+" de concatener\n"*3)
    #Concatenar con "" o ''
print('segunda forma' 'de concatenar')

text=("La segunda forma es muy util para"
     "concatenar diferentes lineas de texto")
print(text)

    #las cadenas se pueden indexar
palabra = "indexar"
print(palabra[0] + "-" +palabra[2] )
    #rebanadas
print(palabra[0] + "-" +palabra[2]+ "-" +palabra[4:6])

    #Funcion len()
print(len("Permite contar cuantos caracteres contiene una cadena"))


#----------LISTA
print("\n--LISTA-----------------------")
cuadricula = [0, 4, 1, 9, 3]
print(cuadricula)
print(cuadricula[1])
print(cuadricula[:])
    #concatenar
cuadricula + [15,16,17]
    #las listas son mutables (Cambian)
cubo = [1,8,4,6]
cubo[2] = 64
print(cubo)
    #Adjuntar al final de la lista append()
cubo.append(3**2)
print(cubo)
    #Se peude modificar por rebanadas
letras = ["a","b","c","d","e","f"]
letras[2:4] = ["C","D","E",]
print(letras)
    #Calcular la longitud

#EJERCICIO Fibonacci
print("\n--EJECICIO-----------------------")
a, b = 0, 1
print("Valores:",a,",",b)
while a<10:
    print(a, end=",")
    a,b = b, a+b




    


      
