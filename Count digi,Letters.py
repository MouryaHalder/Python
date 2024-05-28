def count_characters(s):
    letters = 0
    digits = 0
    symbols = 0

    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1

    return letters, digits, symbols

def main():
    # Taking input from the user
    user_string = input("Enter a string: ")

    # Counting letters, digits, and symbols
    letters, digits, symbols = count_characters(user_string)

    # Displaying the counts
    print("Letters:", letters)
    print("Digits:", digits)
    print("Symbols:", symbols)

if __name__ == "__main__":
    main()
