# Funciones Universales Binarias
# Son funciones que realizan operaciones elemento-a-elemento sobre datos en una ndarray.
# Las funciones binarias toman dos arrays y devuelven uno o más arrays.


# Función 	              Descripción
# add ------------------- Suma entre elementos correspondientes entre arrays
# subtract -------------- Resta entre elementos de arrays
# multiply -------------- Multiplica arrays
# divide, floor_divide -- Divide o división truncada
# array_equal ----------- Devuelve True si los elementos del array son iguales entre sí
# power ----------------- Eleva cada elemento del primer array a la potencia indicada en el segundo array
# fmin ------------------ Devuelve el mínimo entre cada elemento. fmin ignora los NaN
# fmax ------------------ Devuelve el máximo entre cada elemento. fmax ignora los NaN

import numpy as np

separ = "------------\n"
tab = "\t"
arr1 = np.array([5,36,17,18,9])
arr2 = np.array([8,24,17,19,9])

print(tab, arr1,"\n")
print(tab, arr2,"\n")

# add
print("\nadd",separ)
sum = np.add(arr1, arr2)
print(tab, sum)

# subtract
print("\nsubtract",separ)
rest = np.subtract(arr1, arr2)
print(tab, rest)

# multiply
print("\nmultiply",separ)
mult = np.multiply(arr1, arr2)
print(tab, mult)

# divide, floor_divide
print("\ndivide, floor_divide",separ)
div = np.divide(arr1, arr2)
floDiv = np.floor_divide(arr1, arr2)
print(tab, "div:\n", tab,div)
print(tab, "FloDiv:\n", tab,div)

# array_equal
print("\narray_equal",separ)
arr_equal = np.array_equal(arr1, arr2)
print(tab, arr_equal)

# power
print("\npower",separ)
pow = np.power(arr1, arr2)
print(tab, pow)

# fmin
print("\nfmin",separ)
min = np.fmin(arr1, arr2)
print(tab, min)

# fmax
print("\nfmax",separ)
max = np.fmax(arr1, arr2)
print(tab, max)