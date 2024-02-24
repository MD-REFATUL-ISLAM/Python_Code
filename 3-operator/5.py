# Python Program to perform addition 
# of two complex numbers using binary 
# + operator overloading.
class complex:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    # adding two objects
    def __add__(self,other):
        return self.a + other.a, self.b + other.b, self.c + other.c

ob1 = complex(1,2,4)
ob2 = complex(5,8,5)

ob5 = ob1 + ob2

print(ob5)

