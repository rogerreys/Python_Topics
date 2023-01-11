# file = open('./text.txt')
# for line in file:
#     print(line)
# file.close()

# READ
with open('./text.txt') as file:
    for f in file:
        print(f)

# WRITE
# with open('./text.txt', 'w') as file:
#     file.write('Test') 

# READ & WRITE
with open('./text.txt', 'r+') as file:
    for f in file:
        print(f)
    file.write('\nA11 B22 C33 D44') 
