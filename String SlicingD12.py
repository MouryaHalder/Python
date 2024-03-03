name="Sumit,Mourya"
print(name[0:3]) #0 to n-1 Here the value of n is 3
print(len(name)) #length function

fruit = "Apple" 
len=len(fruit) #len function ta len variable ar bhetor dhukiachi
print("Mango is a ",len,"letter word")
print(fruit[0:3]) #for slicing '[]' square bractets is used
print(fruit[:3]) #Python will put automatically put 0
print(fruit[1:3])  #Starts from 1
print(fruit[:]) #len of fruit
#print(fruit[0:len(fruit)-2]) #including 0 but not 4
print(fruit[0:-3]) #index -3 refers to the last character
#In this case, it takes characters at indices 0 and 1, forming the substring 'Ap'.
print(fruit[-3:-1]) # Ap|pl|e -3 Extracts p,l(-3 i.e Ap excluded from ple as ending is -1 e is Sliced)
