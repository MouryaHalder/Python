# WAPP to generate result depending upon following condition:
# ---------------------------------------
# marks Grade
# 75-100 Star
# 60-75 First Class
# 45-60 Second Class
# 30-45 Pass Division
# Otherwise FAIL
#-----------------------------------------
m=int(input("Enter the marks(Within 100)="))
if(m>=75):
    result="Star marks"
elif(m>=60):
    result="First Class"
elif(m>=45):
    result="Second Class"
elif(m>=30):
    result="Pass Division"
else:
    result="FAIL"
print("Your have obtained",result)