# HOF con funciones
## FUNCION
def increment(x):
    return x+1

## HOF
def high_ord_funct(x, func):
    return x + func(x)

res = high_ord_funct(2, increment)
print("res:: ", res)

# HOF con lambda
decrement = lambda x:x-1

high_ord_funct_v2 = lambda x, func: x+func(x)
res_v2 = high_ord_funct_v2(10, decrement)
print("res_v2:: ", res_v2)
res_v2 = high_ord_funct_v2(10, lambda x: x*2)
print("res_v2:: ", res_v2)
res_v2 = high_ord_funct_v2(10, lambda x: x/2)
print("res_v2:: ", res_v2)