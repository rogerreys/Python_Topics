#EJEMPLO 1
#output: For each command of type print, print the list on a new line.
#Sample Input 0
#   12
#   insert 0 5
#   insert 1 10
#   insert 0 6
#   print
#   remove 6
#   append 9
#   append 1
#   sort
#   print
#   pop
#   reverse
#   print
print("\n\nEjercicio1: Escribir comandos")
num = int(input("numero de veces: "))
while num<=4:
    L = []    
    for x in range(0,num+1):
        s = str(input())
        s = s.split()
        comand = s[0]
        kw = s[1:]
            
        if comand != "print":
            comand+="("+",".join(kw)+")"
            eval("L."+comand);     
        else:
            print(L)
