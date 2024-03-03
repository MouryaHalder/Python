# Converting touple to a list & then again converting that list to touple
countries=("Spain","Germany","India","America")
temp=list(countries)
temp.append("Germany") #Add item
temp.pop(3)      #remove item
temp[2]="Italy" #Change item
countries=tuple(temp)
print(countries)

# Merging touples and creating a new touple 
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)


tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
#res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)