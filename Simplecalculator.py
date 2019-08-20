import math
print("")
a=int(input(""))
b=input("")
if b == "+":
    c=int(input(""))
    d=input("")
    if d == "=":
        e=a+c
        print(a,"+",c,"=",e)
    else:
        print("INVALID")
elif b == "-":
    c=int(input(""))
    d=input("")
    if d == "=":
        e=a-c
        print(a,"-",c,"=",e)
    else:
         print("INVALID")
elif b == "*":
    c=int(input(""))
    d=input("")
    if d == "=":
        e=a*c
        print(a,"*",c,"=",e)
    else:
        print("INVALID")
elif b == "/":
    c=int(input(""))
    d=input("")
    if d == "=":
        e=a/c
        print(a,"/",c,"=",e)
    else:
        print("INVALID")
elif b == "^":
    d=input("")
    if d == "=":
        e=a*a
        print(a,"*",a,"=",e)
elif b == "&":
       d=input("")
       if d == "=":
          print(math.sqrt(a))
       else:
           print("INVALID")
elif b == "!":
           d=input("")
           if d == "=":
               print(math.factorial(a))
           else:
               print("INVALID")
        


