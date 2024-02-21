import time
timestamp =  time.strftime('%H:%M:%S')
print (timestamp)
timestamp =  int(time.strftime('%H'))
print (timestamp)
timestamp =  int(time.strftime('%M'))
print (timestamp)
timestamp =  int(time.strftime('%S'))
print (timestamp)


import time
timestamp =  time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
hour=int(input("Enter Hour:"))
print(hour)

if (hour>=0 and hour<=12):
    print('Good morning sir G')
elif(hour>12 and hour<17):
    print("Good afternoon sir g")
if(hour>=17  and hour>0):
    print("Good night sir g")    