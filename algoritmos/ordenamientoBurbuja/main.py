import random

def orden_burbuja(lista):
    n = len(lista)
    
    for i in range(n):  # O(n) * O(n-i-1) = O(n²)
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

if __name__ == '__main__':
    cont = 0
    tamaño_lista = int(input("De que tamaño es la lista?\n"))
    lista = [random.randint(0, 100) for i in range(0, tamaño_lista)]
    print(lista)
    list_sort = orden_burbuja(lista)
    print(list_sort)