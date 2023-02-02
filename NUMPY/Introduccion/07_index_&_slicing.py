# Indexacion & Slicing
# Slicing (Filtrado) sigue [i:j:k]
# i = indice inicial,  j = indice final,  k = incremento (step) no nulo
sepa = "---------\n"
import numpy as np

# arr = np.random.randint(80,size=(4,5))
arr = np.array(range(64)).reshape((8,8))
print(arr)

# Indexar
print("\nIndexar",sepa)
print(arr[1,6],"\n")
print(arr[0:6:3],"\n")
print(arr[0:6:3,0:5:2],"\n")
print(arr[1,1:],"\n")
print(arr[[1,3,5],[3,5,7]],"\n")
print(arr[[1,3,5],::3],"\n") # :: conteo



# Indexacion Booleana
# >  <
print("\n\nIndexacion Booleana",sepa)
data = np.array(range(20))
print(data,"\n")
print(data < 8,"\n")
print(data[data<8],"\n")

amigos = np.array(['Julia','Ana','Sandra','Pepe','Juan','Sandra'])
print('Ana' in amigos)
print(amigos[amigos != 'Ana'])# Evaluacion logica
 