import module
# Re-naming a Module
import module as mod

final= "-"*70+"\n"



# Using a function from a module, use the syntax: module_name.function_name.
print('Module',final)
module.greeting("roger")



# Call variables
print('Call variables',final)
call = ["Name","LastName","Age","City"]
for x in call:
    print(module.variableModulo[x])



# Re-naming a Module
print('Re-naming a Module',final)
calls = ["Name", "LastName", "Age", "City"]

for x in calls:
    print(mod.variableModulo2[x])



# Built-in Modules
print('Built-in Modules',final)
import platform
x = platform.system()
print(x)



# Import From Module
# import only parts from a module
print('Import From Module',final)
from module import variableModulo
print(variableModulo["Name"])