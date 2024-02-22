# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest, middle, and smallest numbers
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

# Calculate the middle number by excluding the largest and smallest
middle = (num1 + num2 + num3) - largest - smallest

# Display the results
print(f"Largest number: {largest}")
print(f"Middle number: {middle}")
print(f"Smallest number: {smallest}")
