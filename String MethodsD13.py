#Strings are immutable
a="Sumit!!..Sumit"
print(len(a))
print("This is original string:",a)
print(a.upper())
print(a.lower())
print(a.rstrip("!."))
print(a.replace("Sumit","Zex")) # Change Sumit to zex
print(a.split(" ")) #Creates list
blogHeading="introduction to python"
print(blogHeading.capitalize()) # this methoda turns 1st letter to capital
print(blogHeading.center(50))
print(blogHeading.upper())
print(a.count("Sumit"))

str1="Welcome to the console !!!"
print(str1.endswith("!")) #This will check if the ending is '!' or not if yes then boolean data type will return
print(str1.endswith("%")) # check if the ending is '%' if no then boolean data type
print(str1.endswith("to",4,10)) #this will start checking from 4 to 10 if 10no is ending correct then true
str1="He's name is Dan. He is an honest man"
print (str1.find("is")) #finding 1st  occurance and that number will print
str1="WelcomeToTheConsole"
print(str1.isalnum()) #if string only contains A-Z,a-z or 0-9 then true spaces not included
str1="Welcome00"
print(str1.isalpha())#will check only contains A-Z,a-z 
str1="hello world"
print(str1.islower()) #checks is all the value is in LOWER CASe or not
str1="World Health Prganization"
print(str1.istitle()) #check title ar 1st letter ta capital na ki
str1="Mocking bird"
print(str1.istitle()) #check 1st letter of every word is capital or not
str1="His name is dan. Dan is an honest man"
print(str1.title())#changes all the words 1st letter to capital
str1="Python"
print(str1.swapcase()) #change upper to lower and viceversa
