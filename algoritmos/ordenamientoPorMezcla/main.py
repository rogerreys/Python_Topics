import random

def ord_mezcla(lista):
    if len(lista)>1:
        medio = len(lista)//2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*'*5, derecha)

        # Llamada recursiva en cada mitad
        ord_mezcla(izquierda)
        ord_mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iteradores para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i+=1
            else:
                lista[k] = derecha[j]
                j+=1
            k+=1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-'*30)

    return lista



if __name__ == '__main__':
    tamaño_lista = int(input("De que tamaño es la lista?: "))
    lista = [random.randint(0, 100) for i in range(0, tamaño_lista)]
    print(lista)
    list_ord = ord_mezcla(lista)
    print("/"*30)
    print(list_ord)