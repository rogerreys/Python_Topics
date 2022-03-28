print("Mutation".upper()+"\n")
print("""
Ingresar un string y luego ingresar
un caracter y index a ser reempazados en el
string
""")
s, i, c = input("Ingresar string, index y un char\n").split()
#FIRS METHODE
print("\nfirst Methode")
spliting = list(s)
spliting[int(i)] = c
print("".join(spliting))

#SECOND METHODE
print("\nSecond Methode")
string = s[:(int(i))]+c+s[(int(i)+1):]
print(string)

