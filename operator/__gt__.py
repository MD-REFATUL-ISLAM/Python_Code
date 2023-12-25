
class A:
    def __init__(self,a):
        self.a = a 
    
    def __gt__(self,other):
        
        if (self.a > other.a):
            return True
        else:
            return False

# call value from console        
ob1 = A(input("value : "))
ob2 = A(input("value : "))

if ob1>ob2 :
    print("ob1 is greater than ob2")
else :
    print("ob1 is less than ob2")