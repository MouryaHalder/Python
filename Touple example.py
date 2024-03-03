tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3, 4, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
res=tuple1.index(3,4,8) #4-8 slicing then finding 3 in the sliced then printing the index number of 3
#res=len(tuple1) #shows length of the full tuple
print("Count of 3 in touple is:",res)


myTuple=([1,2],[3])
myTuple[1].append(4)
#we can modifi list and there adress stays the same here 1 space is left like the 1st list so 4 entered
print(myTuple)