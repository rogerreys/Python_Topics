import sys
print(sys.path)

# EXPRESIONES REGULARES
import re 
text = 'Mi numero celular es 0998765431, y el codigo de pais es 6435, el numero de la suerte es 72'
res = re.findall('[0-9]+', text)
print("res: ", res)


# HORAS Y FECHAS
import time
timestamp = time.time()
local = time.localtime()
res_time = time.asctime(local)
print("timestamp=> ", timestamp)
print("res_time=> ", res_time)


# COLLECTIONS
import collections
num = [1,1,2,3,4,4,5,3,6,4,7]
couter = collections.Counter(num)
print("couter:: ", couter)
