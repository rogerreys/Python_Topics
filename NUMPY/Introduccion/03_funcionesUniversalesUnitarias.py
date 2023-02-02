# FUNCIONES UNIVERSALES UNITARIAS
# Son funciones que realizan operaciones elemento a elemento sobre datos en un ndarray.
# Las funciones unarias comprenden todas las operaciones que reciben un solo array como argumento.
# 
# Funciones                 Descripcion
# abs, fabs --------------- Calcular el valor absoluto
# sqrt  ------------------- Calcular la raíz cuadrada
# square ------------------ Calcular el cuadrado
# exp  -------------------- Calcular la exponencial 𝑒𝑥
# log, log10, log2, log1p-- Calcula el Logaritmo natural, en base a 10, 2, y 𝑙𝑜𝑔(𝑥+1)
# isnan ------------------- Devuelve un array booleano indicando si cada elemento es NaN (Not a Number)
# sin, cos, tan ----------- Devuelve un array con el resultado de aplicar la función seno, coseno, y tangente en los valores
# mean, median, std, var -- Calcula la media aritmética, la mediana, la desviación estándard y la varianza en un array
import numpy as np

separ = "---------------\n"
tab = "\t" 
arr = np.array([2, 4, 9],float)
arrneg = np.array([-2, 4, -9],float)

# abs, fabs
print("\nAbs, fabs:",separ)
ab = np.abs(arrneg)
print(tab,ab)

# sqrt
print("\nsqrt:",separ)
sqr = np.sqrt(arr)
print(tab,sqr)

# square
print("\nsqrt:",separ)
sq = np.square(arr)
print(tab,sq)

# exp
print("\nexp:",separ)
ex = np.exp(arr)
print(tab,ex)

# log, log10, log2, log(x+1)
print("\nlog, log10, log2, log(x+1):",separ)
lg, lg10, lg2,lg1x = np.log(arr), np.log10(arr), np.log2(arr), np.log1p(arr)
print(tab,f"log: {lg},\n\t log10: {lg10},\n\t log2: {lg2},\n\t log(x+1): {lg1x}")

# isnan
print("\nisnan:",separ)
isNaN = np.isnan(arr)
print(tab,isNaN)

# sin, cos, tan
print("\nsin, cos, tan:",separ)
sin, cos, tan = np.sin(arr), np.cos(arr), np.tan(arr)
print(tab,f"sen: {sin},\n\t cos: {cos},\n\t tang: {tan}")

# mean, median, std, var
print("\nmean, median, std, var:",separ)
mean, median, std, var = np.mean(arr), np.median(arr), np.std(arr), np.var(arr)
print(tab,f"mean: {mean},\n\t median: {median},\n\t std: {std},\n\t var: {var}")