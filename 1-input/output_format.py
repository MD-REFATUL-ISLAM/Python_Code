
name = "Md Refatul Islam"
age = 30
salary = 4903.89

print(" Name:%s \n Age:%d \n Salary:%f" %(name,age,salary))
# Name:Md Refatul Islam 
# Age:30 
# Salary:4903.890000
print("Name:{} \nAge:{} \nSalary:{}".format(name,age,salary))
# Name:Md Refatul Islam 
# Age:30 
# Salary:4903.89

print("Name:{0} Age:{1} Salary:{2}".format(name,age,salary))
print("Name:{0} Age:{0} Salary:{0}".format(name,age,salary))
print("Name:{1} Age:{1} Salary:{1}".format(name,age,salary))
print("Name:{2} Age:{2} Salary:{2}".format(name,age,salary))

"""
Name:Md Refatul Islam Age:30 Salary:4903.89
Name:Md Refatul Islam Age:Md Refatul Islam Salary:Md Refatul Islam
Name:30 Age:30 Salary:30
Name:4903.89 Age:4903.89 Salary:4903.89
"""