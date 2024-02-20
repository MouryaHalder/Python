my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} #Each key-value pair is separated by a colon (:)
#Keys and values can be of any data type.
print(my_dict['key1'])  # Output: 'value1'
my_dict['key1'] = 'new_value' #Modifying Values:
my_dict['new_key'] = 'new_value' #Adding New Key-Value Pairs:
del my_dict['key2'] #Removing Key-Value Pairs:
if 'key1' in my_dict: #Checking for Key Existence:
    print("Key 'key1' exists!")
#Dictionary Methods:
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()


#Example 

# Creating a dictionary
student_info = {
    'name': 'Sumit',
    'age': 19,
    'grade': 'A'
}

# Accessing values
print(student_info['name'])  # Output: 'Sumit'

# Modifying values
student_info['age'] = 20

# Adding a new key-value pair
student_info['gender'] = 'Male'

# Removing a key-value pair
del student_info['grade']

# Checking for key existence
if 'grade' in student_info:
    print("Grade exists.")
else:
    print("Grade does not exist.")

# Using dictionary methods
keys = student_info.keys() # keys () mane sob keys print hobe
values = student_info.values() #values() mane sob values print hobe
items = student_info.items() #items() mane total Keys and values is called items

print(keys)    
print(values)  
print(items)   

