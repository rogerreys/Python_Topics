print("Find a string".upper())
string = input("Ingresar String\n").strip()
subString  = input("Ingre sub string\n").strip()

cont = 0

if subString in string:
    for x in range(0,len(string)):
        if subString in string[x:(len(subString)+x)]:
            cont+=1

print(cont)


           
        
    
    

