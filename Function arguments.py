#There are 4 types of arguments 1. Default arguments 
# 2. Keyword arguments 3. Variable arguments 4. required arguments
#defalut arguments
def average(a=9,b=1):
    print("The average is",(a+b)/2)
#average (4,6)
average(5)

# Default argument

def name(fname, mname= "Mourya",lname="Halder"):
    print("Hello",fname,mname,lname)
name("Sumit","Tuban","Anderson") #Overwrite hoi jacche in output

#Required arg - arguments have to give numbers have to be taken

# Finding average
def average(*numbers):  # numbers is iterable(Object which can be looped)
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("The Average is:",sum/len(numbers))
average(5,6,7,1)

#(**)mane  dictionary  function