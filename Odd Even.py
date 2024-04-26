def check_odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    # Taking input from the user
    num = int(input("Enter a number: "))

    # Calling the function to check if the number is odd or even
    result = check_odd_even(num)

    # Displaying the result
    print("The number is", result)

if __name__ == "__main__":
    main()
