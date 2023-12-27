
# initialize a string
var1 = "improvization"
print("initial string : ")
print(var1)

# Updating a character of the String 
# As python strings are immutable, they don't support item updation directly 
# there are following two ways 

#1
list1 = list(var1)
list1[3] = "X"
var2 = "".join(list1)

print("\nunderstanding the 3rd index: ")
print(var2)

#2

var3 = var1[0:3] + "X" + var1[4:]
print(var3)
