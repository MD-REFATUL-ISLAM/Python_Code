
string = "Learn programming."

print("Center align : ")
print(string.center(50,"#")) 


print("left align : ")
print(string.ljust(60,'-'))

print("Right align : ")
print(string.rjust(70,"*"))

"""
Center align : 
################Learn programming.################
left align : 
Learn programming.------------------------------------------
Right align : 
****************************************************Learn programming.
"""

