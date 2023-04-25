items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalon',
        'price': 200
    },
    {
        'product': 'gorro',
        'price': 50
    },
    {
        'product': 'sueter',
        'price': 150
    }
]

prices = list(map(lambda x: x['price'], items))
print(prices)

def calcu_taxes(item):
    item['taxes'] = item['price']*0.19
    return item

# new_items = list(map(calcu_taxes, items))
#print("Array orig: ", items)
#print("New array: ", new_items)
# RECOMENDACION: No deberia modificar el array original

# SOLUCION
def calcu_taxes_v2(item):
    new_items = item.copy()
    new_items['taxes'] = new_items['price']*0.19
    return new_items

new_items_v2 = list(map(calcu_taxes_v2, items))
print("Array orig 2: ", items)
print("New array 2: ", new_items_v2)