import csv
import functools as func

def read_csv(path):
  # Tu código aquí
  with open(path, 'r') as file:
    text = list(csv.reader(file, delimiter=','))
    total = func.reduce(lambda count, x: count+int(x[1]), text, 0)
    print('total ', total)
  return total

response = read_csv('./data.csv')
print(response)