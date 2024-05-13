# Write a Python Program (WAPP) to check smallest between three numbers ( A!=B!=C)
a=int(input("Enter 1st number="))
b=int(input("Enter 2nd number="))
c=int(input("Enter 3rd number="))
if(a<b and a<c):
    small=a
elif(b<c):
    small=b
else:
    small=c
print("Smallest Number will be:",small)