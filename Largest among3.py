print("Hi! Mourya this side")
a=int (input("enter 1st number:"))
b=int (input("enter 2nd number:"))
c=int (input("enter 3rd number:"))
if(a>b):
    if(a>c):
        print("a is the largest")
    else:
        print("c is the largest")
elif(b>a):
    if(b>c):
        print("b is the largest")
    else:
        print("c is the largest")
else:
    print("c is the largest")
