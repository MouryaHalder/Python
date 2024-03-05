dict = {

    543:"Arindom",
    135:"Mourya",
    127:"Diya",
    432:"Tusher",
    567:"Baccha"
}
print(dict[135])

info = {'name':'Mourya','age':19,'Eligible':True}
print(info)
print(info['name'])
print(info.get('age'))
print(info.values())

print(info.items())
for key,value in info.items():
    print("The value corresponding to the key{key}is {value}")
    