s1={1,2,5,6}
s2={4,6,7,3}
print(s1.union(s2))
print(s1,s2)

# Intersection and update
cities={"Tokyo","Delhi","Kolkata","Goa"}
cities2={"Amritsar","Odisa","Kolkata","Chennai","Goa"}
#cities3=cities.intersection(cities2)
cities.intersection_update(cities2) #here cities 2 ar value cities a dhuke jabe and rest values will be omitted
print(cities)

# Symetric difference i.e all the values which is not common
cities={"Tokyo","Delhi","Kolkata","Goa"}
cities2={"Amritsar","Odisa","Kolkata","Chennai","Goa"}
cities3=cities.symmetric_difference(cities2)
print(cities.isdisjoint(cities2))# Disjoint Set when 2 sets have nothing in common
print(cities3) # uncommon values gulo print hobe

# Super set
cities={"Tokyo","Delhi","Madrid","Berlin","Seoul","Kabul"}
cities2={"Seoul","Kabul"}
print(cities.issuperset(cities2))
cities3  = {"seoul","Madrid","Kabul"}
print(cities.issuperset(cities3))

# Delete and discard()
cities={"Tokyo","Delhi","Madrid","Berlin","Seoul","Kabul"}
cities.remove("Kabul")
cities.discard("Delhi")
cities.clear()
print(cities)