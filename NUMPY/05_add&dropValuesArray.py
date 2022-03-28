# Agregar y quitar valores a un array
import numpy as np
separ = "----------\n"

# Range
print("\nrange",separ)
arr = np.arange(2,24,4)
print(arr)

# random
print("\nrandom",separ)
arran = np.random.rand(2,3)
print(arran)

# randint
print("\nRandom",separ)
arranin = np.random.randint(100, size=(4,8))
print(arranin)

# full
print("\nfull",separ)
ar_full = np.full((4,4),6)
print(ar_full)

# append
print("\nappend",separ)
apd = np.append(arr,[1,2,3])
print(apd)

# Insert
print("\ninsert",separ)
ins = np.insert(arr,2,[9,8,7])
print(ins)

# delete
print("\ndelete",separ)
# 0 -- Filas
# 1 -- Columnas
print(arran,"\n")
ins = np.delete(arran,0,axis=1)
print(ins)