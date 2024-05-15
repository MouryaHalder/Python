#WAPP to check whether a year is leapyear or not
yr=int(input("Enter any year:"))
if((yr%400==0)or(yr%4==0 and yr%100!=0)):
    print(yr,"is a leap year")
else:
    print(yr,"is not a leap year")