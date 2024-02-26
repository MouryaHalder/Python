#Type Casting

#EXPLICIT TYPE CASTING
a="1"#Taking this as a String 
b="2"#Taking this as a String
print(int(a)+int(b))  #Converting this to intiger if int is USED (This is type casting)

string ="15"
number= 5
string_number = int(string)#throws an error if the string is not a valid integer
sum=number+string_number
print("THe Sum of both the numbers is", sum)


#Implicit TypeCasting
print("Implicit TypeCasting:") #automatically converts one data type to another data type without any user's need.
c=1.9
d=8
print(c+d)

#Examples
#Python automatically converts 
#a to int
a=7
print(type(a))
#Python automatically converts b to float
b=3.0
print(type(b))
#python automatically converts c to float as it is a float addition
c=a+b
print (c)
print(type(c))

