
# Get user input
while True:
    try:
        num1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        num2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Determine maximum and minimum
if num1 > num2:
    max_num = num1
    min_num = num2
else:
    max_num = num2
    min_num = num1

# Display maximum and minimum
print(f"The maximum number is {max_num}")
print(f"The minimum number is {min_num}")