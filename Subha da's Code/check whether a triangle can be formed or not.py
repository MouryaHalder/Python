# WAPP to check whether a triangle can be formed or not
a=int(input("Enter 1st side of the triangle="))
b=int(input("Enter 2nd side of the triangle="))
c=int(input("Enter 3rd side of the triangle="))
if((a+b>c)and(b+c>a)and(c+a>b)):
    print("Triangle can be formed")
else:
    print("Triangle can not be formed")