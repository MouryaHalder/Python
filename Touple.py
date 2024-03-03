#tup=(1,5)
tup=[1,2,3,4,5,6,7,8,9,'RED',True]
#tup[0]=90
print(type(tup),tup)
print("length is",len(tup))
print(tup[0])
print(tup[-2])
print(tup[2])
if 99 in tup:
    print("Yes 99 is present in touple")
tup2=tup[:5]
print(tup2)