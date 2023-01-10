######### TRY INDIVIDUALES
try:
    print(0/0)
except ZeroDivisionError as e:
    print(e)

print('Hello')


try:
    # assert (hace verificaciones), Exception
    assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as e:
    print(e)

print('Hello2')


try:
    age = 10
    if age < 18:
        raise Exception("Es menor de edad")
except Exception as e:
    print(e)
print('Hello3')



######### TRY GRUPAL
# try:
#     print(0/0)

#     # assert (hace verificaciones), Exception
#     assert 1 != 1, 'Uno no es igual que uno'

#     age = 10
#     if age < 18:
#         raise Exception("Es menor de edad")
# except ZeroDivisionError as e:
#     print(e)
# except AssertionError as e:
#     print(e)
# except Exception as e:
#     print(e)


# print('Hello')
# print('Hello2')
# print('Hello3')