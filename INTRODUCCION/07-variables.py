final= "-"*70+"\n"
# Local Scope
print('Local Scope',final)
def myfunc():
  x = 300
  print(x)

myfunc()


# Global Scope
print('Global Scope', end=final)
y = 300

def myfunc2():
  print(y)

myfunc2()
print(y)


# Naming Variables
print('Naming Variables', end=final)
z = 300

def myfunc3():
  z = 200
  print(z)

myfunc3()
print(z)


# Global Keyword
# If you need to create a global variable, but are stuck in the local scope
print('Global Keyword', end=final)

def myfunc4():
  global ab
  ab = 300

myfunc4()

print(ab)