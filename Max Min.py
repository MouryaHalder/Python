def find_max_min(num1, num2, num3):
    # Finding the maximum
    maximum = max(num1, num2, num3)
    
    # Finding the minimum
    minimum = min(num1, num2, num3)
    
    return maximum, minimum

def main():
    # Taking input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Calling the function to find maximum and minimum
    max_num, min_num = find_max_min(num1, num2, num3)

    # Displaying the results
    print("Maximum number:", max_num)
    print("Minimum number:", min_num)

if __name__ == "__main__":
    main()
