# first, import the module sys
# use of the stdout.write() method

import sys

# It only works with string 
# If you pass a number or a list
# you will get a TypeError.

sys.stdout.write("GeeksforGeeks ")
sys.stdout.write("is best website for coding!\n")


# print value in same line  
print("geeks", end= " ")
print("for", end=" ")
print("geeks")

# print something between
print("geeks", end= "@")
print("for", end="@")
print("geeks")

# print without space
print("geeks", end="")
print("for", end="")
print("geeks")
