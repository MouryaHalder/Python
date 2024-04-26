def user(name):
    print("Characters in the name:")
    for char in name:
        print(char)

def main():
    # Taking input from the user
    name = input("Enter your name: ")

    # Displaying each character of the name
    user(name)

if __name__ == "__main__":
    main()
