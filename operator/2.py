
a, b =[int(a) for a in input("enter two value : ").split(",")]

if a != b:

    if a < b:
         print(f"{a} is less than {b}")
         print(True)

    else:
        print(f"{a} is greater than {b}")
        print(False)

else : 

    print("both are equal")
    





