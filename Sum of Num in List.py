# Function to calculate the sum of numbers in a list
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Main function
def main():
    # Ask the user for input
    num_str = input("Enter a list of numbers separated by spaces: ")

    # Convert the input string into a list of integers
    numbers = [int(x) for x in num_str.split()]

    # Calculate the sum using the calculate_sum function
    total_sum = calculate_sum(numbers)

    # Print the result
    print("The sum of the numbers is:", total_sum)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
