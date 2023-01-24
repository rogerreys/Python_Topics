import random

def ord_insercion(lista):
    lista_ref = []
    i_act = 0
    for i, x in enumerate(lista):
        i_act = i
        while i_act>0 and lista[i_act]<lista[i_act-1]:
            lista[i_act],lista[i_act-1] = lista[i_act-1],lista[i_act]
            i_act-=1
    return lista

  

if __name__ == '__main__':
    tamaño_lista = int(input("De que tamaño es la lista?\n"))
    lista = [random.randint(0, 100) for i in range(0, tamaño_lista)]
    print(lista)
    list_ret = ord_insercion(lista)
    print(list_ret)