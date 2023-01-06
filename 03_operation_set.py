set_a = {'col', 'mex', 'ec'}
set_b = {'pe', 'ec'}
print("a ", set_a)
print("b ", set_b)
# Union (.union o |)
set_c = set_a.union(set_b)
print("Union ",set_c)
print("Union ",set_a | set_b)

# Intersection  (.intersection o &)
set_c = set_a.intersection(set_b)
print("Intersection: ", set_c)
print("Intersection: ", set_a & set_b)

# Diferencia
set_c = set_a.difference(set_b)
print("Diferencia ",set_c)
print("Diferencia ",set_a - set_b)

# Symmetric Diferencia 
set_c = set_a.symmetric_difference(set_b)
print("Symme Dif ", set_a ^set_b)
print("Symme Dif ", set_c)