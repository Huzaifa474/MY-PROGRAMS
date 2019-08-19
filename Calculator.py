print("\tSIMPLE CALCULATOR PROGRAM\t")
print("_____________________________")
a=int(input("Enter any number"))
b=int(input("Enter second number"))
print("\n")
print("_________________________________________________________________")
print("Press 1 for Addition\n","Press2 for Subraction\n","Press 3 for multiplication\n","Press 4 for division\n")
print("\n")
c=int(input("Enter option\n"))
if (c==1):
    d=a+b
    print("_______________")
    print(a,"+",b,"=",d)
    print("_______________")
elif (c==2):
    d=a-b
    print("_______________")
    print(a,"-",b,"=",d)
    print("_______________")
elif (c==3):
    d=a*b
    print("_______________")
    print(a,"*",b,"=",d)
    print("_______________")
elif (c==4):
    d=a/b
    print("_______________")
    print(a,"/",b,"=",d)
    print("_______________")
else:
    print("WRONG OPERATOR")
