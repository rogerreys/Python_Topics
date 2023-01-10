import functools as func
def get_total(orders):
  # Tu código aquí 👇
  return func.reduce(lambda count, item: count+item['total'], orders, 0)
   # return func.reduce(function, sequence, initial)


orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)