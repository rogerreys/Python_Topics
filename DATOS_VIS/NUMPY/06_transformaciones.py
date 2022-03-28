# Transformaciones
# As Type
# Este tipo nos permite modificar el dato con valores de array
sepa="------------------\n"
import numpy as np

arr = np.random.randint(90,size=(3,4))
print(arr)

# As Type
print("\nAs Type",sepa)
print(arr.astype(float))

# Sort
print("\nSort",sepa)
arr.sort()
print(arr,"\n")
# 0 -- Columna
arr.sort(axis=0)
print(arr,"\n")

# Reshape
# Modifica dimensiones del array, debe mantener relacion del mismo numero de elementos
print("\nReshape",sepa)
arr_modi = arr.reshape(2,6)
print(arr_modi)

# Flatten (aplanar)
# Crea metodo unidimensional
print("\nFlatten",sepa)
arr_plano = arr_modi.flatten()
print(arr_plano)

# To List
# Crea una lista apartir del array
print("\nTo list",sepa)
lista_arr = arr.tolist()
print(lista_arr,type(lista_arr))


# Split & Concatenate
print("\nSplit & Concatenate",sepa)
print("Split")
split_arr = np.split(arr,3)
print(split_arr)

print("\nConcatenate")
# 0 -- Columnas
# 1 -- fila
concat_arr = np.concatenate((split_arr[0],split_arr[2]),axis=0)
print(concat_arr)

# Matriz Transpuesta
print("\nMatriz Transpuesta",sepa)
print("Origin \n",arr,"\n")

trans_mat = arr.T
print("Transpuesta\n",trans_mat)
