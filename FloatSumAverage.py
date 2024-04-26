def main():
    # Taking input from the user as comma-separated floats and converting to list of floats
    numbers = [float(x) for x in input("Enter multiple float values separated by commas: ").split(',')]

    # Calculating sum and average
    total_sum = sum(numbers)
    average = total_sum / len(numbers)

    # Displaying the sum and average
    print("Sum:", total_sum)
    print("Average:", average)

if __name__ == "__main__":
    main()
