# BMI (BODY MASS INDEX) CALCULATE IN PYTHON
height=float(input("Enter your height in Centimeter : ="))
weight=float(input("Enter your weight in Kilograms="))
height=height/100
bmi=weight/(height*height)
print("your body mass index is:",bmi)
if(bmi>0):
    if(bmi<=16):
        print("you are extremely underweight")
    elif(bmi<=18.5):
        print("you are underweight")
    elif(bmi<=25):
        print("you are healthy")
    elif(bmi<=30):
        print("you are overweight")
    else:
        print("you are extremely overweight")
else:
    print("enter the valid details")