import datetime

x = datetime.datetime.now()
print("\n","Print information",end="\n")
# Year
print(x.year)
# Name Day
print(x.strftime("%A")) 


# Creating Date Objects
print("\n","Creating Date Objects",end="\n")
y = datetime.datetime(2020, 3, 23)
print("yyyy-MM-dd", y)
z = datetime.datetime(x.year, x.month, 23, 10,30)
print("yyyy-MM-dd hh:mm", z)

# The strftime() Method
# ref: https://www.w3schools.com/python/python_datetime.asp
print("\n","The strftime() Method",end="\n")
print(y.strftime("%A"))
print(y.strftime("%B"))
print(y.strftime("%x"))