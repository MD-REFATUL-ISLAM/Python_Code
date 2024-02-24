# define a function
def add( num1: int, num2: int) ->int:
# This line defines a function named add 
# that takes two parameters (num1 and num2) of type int 
# specifies that the function will return an integer (-> int).
    num3 = num1 + num2
    return num3
# return num3: The return statement in a function sends back a value

# driver code
num1 = int(input("enter first value : "))
num2 = int(input("enter the second value : "))
ans = add(num1,num2)
print(f"the sum of {num1} and {num2} is {ans}")

