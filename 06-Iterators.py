# Lists, tuples, dictionaries, and sets are all iterable objects
# iter() method is used to get an iterator

myTuple = ("manzana","pera","sandia")
myIt = iter(myTuple)
print(next(myIt))
print(next(myIt))
print(next(myIt))

# Strings are also iterable objects,
var = "Bananas"
myItVar = iter(var)
for x in range(len(var)):
    print(next(myItVar))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)


# Create an Iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print("\nFirst iteration")
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration
print("\nSecond iteration with limit")
class StopIte():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else: raise StopIteration
        

si = StopIte()
myIterClas = iter(si)

for x in range(100):
    print(next(myIterClas))