def calculate_statistics(int_list):
    maximum = max(int_list)
    minimum = min(int_list)
    total_sum = sum(int_list)
    return maximum, minimum, total_sum

def main():
    # Taking input from the user
    user_input = input("Enter a list of integers separated by spaces: ")

    # Converting the input string into a list of integers
    int_list = [int(x) for x in user_input.split()]

    # Calculating the maximum, minimum, and sum
    maximum, minimum, total_sum = calculate_statistics(int_list)

    # Displaying the results
    print("Maximum element:", maximum)
    print("Minimum element:", minimum)
    print("Sum of all elements:", total_sum)

if __name__ == "__main__":
    main()
