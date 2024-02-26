marks=[3,5,6,"Mourya",True,8,9,11,12,13,14,15,16,17,18]
# print(marks)
# print(type(marks))
# print(marks[0]) #index 0  i.e 3
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# print(marks[-3])  # negative index
# print(marks[len(marks)-3])  #  positive index
# print(marks[5-3]) #positive index
# print(marks[2]) #positive index

# if 'Mourya' in  marks:
#     print("YES")
# else:
#     print('NO')

# # Same thing applies for string as well
# if "rya" in "Mourya":
#     print("Yes")
# else:
#     print("NO")

# print(marks)
# print(marks[1:15])
# print(marks[1:15:2]) # 2 is jump index
# print(marks[1:15:3])

# LIST COMPREHENSION
lst=[i for i in range(5)] #range always take length not index
print(lst)
lst=[i*i  for i in range(10)]
print(lst)
lst=[i*i for i in range(10)  if i % 2 == 0]
print(lst)
