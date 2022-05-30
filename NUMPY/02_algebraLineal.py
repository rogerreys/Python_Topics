separ="--------------\n"

import numpy as np

a = np.array([1,2,3], float)
b = np.array([0,1,1], float)

# Producto de matrices
# [a11,a12,a13]   [b11,b12,b13]   [(a11*b11 + a12*b21 + a13*b31), (a11*b12 + a12*b22 + a13*b32), (a11*b13 + a12*b23 + a13*b33)]
# [a21,a22,a23] * [b21,b22,b23] = [(a21*b11 + a22*b21 + a23*b31), (a21*b12 + a22*b22 + a23*b32), (a21*b13 + a22*b23 + a23*b33)]
# [a31,a32,a33]   [b31,b32,b33]   [(a31*b11 + a32*b21 + a33*b31), (a31*b12 + a32*b22 + a33*b32), (a31*b13 + a32*b23 + a33*b33)]


# dot - Producto de matrices, da resultado escalar
print("\ndot - Producto de matrices",end=separ)
res = np.dot(a,b)
print(res)

# Producto de matrices
a = np.array([[5, 2], [4, 8]], float) 
b = np.array([[2, 4], [5, 3]], float) 

# Metodo dot
print("\nMetodo dot",end=separ)
print(a,"\n-----")
print(b,"\nResultado")
res = np.dot(a,b)
print(res)

# Metodo @ "ad"
print("\nMetodo @",end=separ)
print(a,"\n-----")
print(b,"\nResultado")
res = a @ b
print(res)

# Metodo matmul "ad"
print("\nMetodo matmul",end=separ)
print(a,"\n-----")
print(b,"\nResultado")
res = np.matmul(a,b)
print(res)

# Otros Array
print("\nOtros Array",end=separ)
a = np.array([[0, 1, 4], [5, 2, 3], [1, 4, 8]], float) 
b = np.array([2, 3, 5], float) 
print("a\n",a,"\n-----")
print("b\n",b,"\nResultado")
res = a @ b
print("a@b\n",res)
res = b @ a
print("b@a\n",res)


# Algebra lineal
print("\nAlgebra lineal",end=separ)
a = np.array([[8, 5], [3, 4]])

print(a, "\n ---------------")
# Determinante
# [a11,a12] determinante= (a11*a22)-(a12*a21)
# [a21,a22]
res = np.linalg.det(a)
print(res)

# Auto-valores y auto-vectores 
print("\nAuto-valores y auto-vectores",end=separ)
val, vec = np.linalg.eig(a)
print("val:",val,separ)
print("vec:",vec,separ)