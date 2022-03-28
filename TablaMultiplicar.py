import os

x = input("Ingresar 1° numero:\n")

os.system('clear')

print("--TABLA DE MULTIPLICAR--", end="\n\n")


for fact in range(0, 10):
    res = str(int(x)*fact)
    imp = x +" * "+ str(fact) +" = " + res
    print(imp)