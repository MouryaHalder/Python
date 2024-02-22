# Format is a string method //fstring = formating string
letter="Hey my name is {1} and I am from {0}"
country="India"
name="Sumit"
print(letter.format(country,name)) #sequence
print(f"Hey my name is {name} and I am from {country}") 

print(type(f"{2*30}")) #this curverts to string 
print(f"{2*30}")