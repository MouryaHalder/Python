# Elementory operation on set
a=set([1,2,3,4,5,6])
b=set([4,5,6,7,8,9])
print('a=',a)
print('b=',b)
print('Union=',a.union(b))
print('Intersection=',a.intersection(b))
print('a-b=',a.difference(b))
print('b-a=',b.difference(a))
print(a.symmetric_difference(b))

