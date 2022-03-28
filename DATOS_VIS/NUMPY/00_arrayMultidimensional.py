# Numerical Python
import numpy as np
# Indicar dimensiones de array
import ndim

separ="--------------\n"

# Arreglo
print("Arreglo",end=separ)
arreglo = np.array([0,1,2,3,4,5])
print("\t",arreglo,type(arreglo))

print("Arreglo Float",end=separ)
notas = np.array([16,17,19,15,18],dtype=float)
print("\t",notas,type(notas[0]))

print("Array",end=separ)
ar_notas_todas = np.array(([0,1,2,3,4],notas))
print("\t",ar_notas_todas)

# Dimensiones
print("Dimensiones Arreglo",end=separ)
print("\tarreglo: ",arreglo.ndim)
print("\tnotas: ",notas.ndim)
print("\tar_notas",ar_notas_todas.ndim)

# Shape
print("Shape Arreglo",end=separ)
print("\tarreglo: ",arreglo.shape)
print("\tnotas: ",notas.shape)
print("\tar_notas: ",ar_notas_todas.shape)

# Arrays especiales
print("\nArrays especiales",end=separ)
# Zero
print("Zeros",end=separ)
arrZero = np.zeros((2,3), dtype=float)
print(arrZero)

# Ones
print("Ones",end=separ)
arrOnes = np.ones((3,5), dtype=float)
print(arrOnes)

# Identity
print("Identity",end=separ)
arrIdentity = np.identity((5), dtype=float)
print(arrIdentity)

# Eyes or Identity
print("Eye or Identity",end=separ)
arrEyes = np.eye((8), dtype=float)
print(arrEyes)

# Arange
print("Arange",end=separ)
arrArange = np.arange(1,9)
print(arrArange)