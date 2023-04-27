import functools as func
num = [2,3,4,5,6]
def accum(count, item):
    print("count=> ",count)
    print("item=> ",item)
    return count + item

# res = func.reduce(lambda count, item: count+item, num)
res = func.reduce(accum, num)
print("res: ", res)
