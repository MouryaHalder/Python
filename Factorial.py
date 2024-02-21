# wap to find factorial of a number

def calculate_factorial(n):
    """
    Function to calculate the factorial of a given number.
    """
    if n < 0:
        return "Factorial is undefined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        factorial_result = 1
        for i in range(2, n + 1):
            factorial_result *= i
        return factorial_result

# Example usage:
number = int(input("Enter a number: "))
result = calculate_factorial(number)
print(f"The factorial of {number} is: {result}")

print("******Adjustments*******")
name = "Mourya"
print(name.ljust(20))  # Left justify
print(name.rjust(20))  # Right justify
print(name.center(20))  # Center justify

#4

# String data type
name = "John Doe"
print(f"String: {name}")

# Integer data type
age = 30
print(f"Integer: {age}")

# Float data type
height = 5.9
print(f"Float: {height}")

# Boolean data type
is_student = True
print(f"Boolean: {is_student}")

# Complex data type
complex_num = 1j
print(f"Complex: {complex_num}")

# List data type
fruits = ["apple", "banana", "cherry"]
print(f"List: {fruits}")

# Tuple data type
colors = ("red", "green", "blue")
print(f"Tuple: {colors}")

# Set data type
numbers = {1, 2, 3, 4, 5}
print(f"Set: {numbers}")

# Dictionary data type
person = {"name": "Jane Doe", "age": 25}
print(f"Dictionary: {person}")

# # 5
# # Get user input
# input_data = input("Enter some data: ")

# # Determine data type
# data_type = type(input_data)

# # Display data type
# print(f"The data type of the input is {data_type}")

# # Convert input to appropriate data type
# try:
#     integer_data = int(input_data)
#     print(f"The integer value is {integer_data}")
# except ValueError:
#     pass

# try:
#     float_data = float(input_data)
#     print(f"The float value is {float_data}")
# except ValueError:
#     pass

# try:
#     bool_data = bool(input_data)
#     print(f"The boolean value is {bool_data}")
# except ValueError:
#     pass

# # Display input as string
# print(f"The string value is {input_data}")

#6
# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Display message
print(f"Hello, {name}! You are {age} years old.")