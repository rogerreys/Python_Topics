import time
import random

def busqueda_lineal(lista, objetivo):
    global cont
    match = False
    for i in lista:     # O(n)
        cont+=1
        if i == objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    cont = 0
    tamaño_lista = int(input("De que tamaño es la lista?\n"))
    objetivo = int(input('Que numero quieres encontrar? \n'))
    lista = [random.randint(0, 100) for i in range(0, tamaño_lista)]
    print("lista: ", lista)

    comienzo_time = time.time()
    encontrado = busqueda_lineal(lista, objetivo)
    final_time = time.time()
    print(f'El elemento {objetivo} {"esta" if encontrado else "No Esta"} en la lista')

    print("Tiempo Exc: ",final_time - comienzo_time, " Steps: ", cont)