# python program showing
# how to take multiple program 
# at a time


# taking three input at a time 
x,y,z = [int(x) for x in input("enter three value : ").split(",")]

print("first number is : ", x)
print("second number is : ", y)
print("third number is : ", z)

# taking multiple input at a time 
x = [int(x) for x in input("enter multiple value : ").split()]
print("the list of value is : ", x)
