# lambda arguments : expression
x = lambda a: a + 10
print(x(5))

# lambda arguments1, arguments2 : expression
y = lambda a, b : a + b
print(y(5,4))

# Use
def myfunc(n):
    return lambda a : a * n

n = int(input("valor1\n"))
m = int(input("valor2\n"))

double = myfunc(n)
print(double(m))