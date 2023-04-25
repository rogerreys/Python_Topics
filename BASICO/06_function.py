def sum_range(min, max):
    num = 0
    for x in range(min, max+1):
        num+=x
    return num
    
print(sum_range(0, 10))
print(sum_range(0, 100))
print(sum_range(0, 23))
print(sum_range(0, 2**2))


# ARGS
def find_volume(lenght=1, width=1, depth=1):
    return lenght * width * depth , width, 'hi'
print(find_volume())
print(find_volume()[0])
result, width, st = find_volume(10, 20, 30)
print("res: ", result, width, st)