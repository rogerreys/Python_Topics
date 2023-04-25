num = [1, 2, 3, 4]
num_2 = [i*2 for i in num]
print(num)
print(num_2)

# Con MAP 
num_3 = list(map(lambda x: x*2, num))
print(num_3)

number_1 = [1,2,3,4,5,6]
number_2 = [8,9,10]
res = list(map(lambda x, y: x+y, number_1, number_2))
print(number_1, number_2,res)