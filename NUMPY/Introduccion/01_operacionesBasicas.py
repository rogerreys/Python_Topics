separ="--------------\n"

import numpy as np

arr = np.arange(1,9)

lista=[1,2,3,4,5]

# Shape para convertir en Array
print("\nShape para convertir en Array",end=separ)
arr.shape = (2,4)
print(arr)

# Sumar arrays
print("\nSumar arrays",end=separ)
print("array: ",arr+arr)    # Suma de arrays
print("list: ",lista+lista) # Union de arrays

# Sustraccion
print("\nSustraccion arrays",end=separ)
print(arr-arr)

# Producto
print("\nProducto arrays",end=separ)
print(arr*arr)

# Exponenciacion
print("\nExponenciacion arrays",end=separ)
print(arr**arr)

# Division
print("\nDivision arrays",end=separ)
print(arr/arr)
