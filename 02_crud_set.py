set_countries = {'col', 'mex', 'ec'}
size = len(set_countries)
print(size)
print('col' in set_countries)

# add
set_countries.add('pe')
set_countries.add('pe')
print(set_countries)

# update
set_countries.update({'ar', 'bol', 'pe'})
print(set_countries)

# remove
set_countries.remove('pe')
# set_countries.remove('arg')  # Da error si no existe
print(set_countries)

# discard es similar a remove, pero si no encuentra no lanza fallo
set_countries.discard('ar')
set_countries.add('arg')

# clear
set_countries.clear()
print(set_countries, "len: ",len(set_countries))

