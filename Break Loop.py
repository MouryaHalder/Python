# Break loop alteration
for i in range (12):
    if(i==10):
        break
    print("5 X", i+1,"=",5*(i+1))
print('Loop has been exitted')


# {Continue} meaning skipping the alteration mane oii part ta exit korabe naa
for i in range(12):
    if(i==10):
        print('Skip the iteration(this step has been skipped)')
        continue
    print('5 X',i,'=',5*i)


#while loop this will execute once whether the condition is true or not
i=0
while True:
    print(i)
    i=i+1
    if(i%100 == 0):
        break
