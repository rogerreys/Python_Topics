# Function
def increment(x):
    return x+1

res = increment(10)
print(res)
# LAMBDA
increment_v2 = lambda x : x + 1

res2 = increment_v2(20)
print(res2)

full_name = lambda name, last_name: f'Your name is {name.title()} {last_name.title()}'
print(full_name("roger", "reyes"))
print(full_name("steven", "medina"))