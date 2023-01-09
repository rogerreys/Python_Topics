# Scope
# Variable Global
price = 100

def increment():
    price = 0 # Variable local
    price+=10
    print(price)
    

print(price)
increment()

