print("String Validators\n".upper())
string = "qA2"
alnum, alpha, digit, lower, upper = False, False,False,False,False 
for x in string:
    alnum += x.isalnum()
    alpha += x.isalpha()
    digit += x.isdigit()
    lower += x.islower()
    upper += x.isupper()
print(bool(alnum))
print(bool(alpha))
print(bool(digit))
print(bool(lower))
print(bool(upper))

#METHOD SHORT
print("\n\nMethod Short")
print(any(c.isalnum() for c in string))
print(any(c.isalpha() for c in string))
print(any(c.isdigit() for c in string))
print(any(c.islower() for c in string))
print(any(c.isupper() for c in string))
