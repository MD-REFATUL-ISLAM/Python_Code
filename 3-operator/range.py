# Python range() function doesn’t support float numbers
# range(start,stop,step)

for i in range(4):
    print(i)

for i in range(2,9):
    print(i,end="-")

for i in range(0,30,4):
    print(i)

for i in range(25,3,-4):
    print(i,end="+")


# Concatenation of two range() functions using itertools chain() method
# concatenated by using the chain() method of itertools module. 
from itertools import chain

print("concatening the result : ")
result = chain(range(5),range(3,12,3))

for i in result:
    print(i)



