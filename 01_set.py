# SET - NO SE PUEDE REPETIR
set_countries = {'col', 'mex', 'ec'}
print(set_countries)
set_num = {1,2,3,6,8,1}
set_val = {1,"Hi",False,12.21}
print(set_val)

set_from_str = set("hola mundo")
print(set_from_str)

# Tupla en set
set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

# lista en set
list_num = [1,5,8,6,4,2,1,3,2,4]
set_num = set(list_num)
print(set_num)
unique_num = list(set_num)
print(unique_num)