import time
import random

def busqueda_binaria(lista, inicio, final, objetivo):
    global count
    print(f"Buscar {objetivo} entre {inicio} y {final}")
    count+=1
    if inicio > final:
        return False
    
    medio = (inicio + final)//2
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo)
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, inicio, medio-1, objetivo)

    

if __name__ == '__main__':
    count = 0
    tamaño_lista = int(input("De que tamaño es la lista?\n"))
    objetivo = int(input('Que numero quieres encontrar? \n'))
    lista = sorted([random.randint(0, 100) for i in range(0, tamaño_lista)])
    print("lista: ", lista)

    comienzo_time = time.time()
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    final_time = time.time()
    print(f'El elemento {objetivo} {"esta" if encontrado else "No Esta"} en la lista')
    print("Tiempo Exc: ",final_time - comienzo_time, "  Steps: ", count)