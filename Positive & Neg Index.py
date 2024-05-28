def display_elements_with_indices(lst):
    for i in range(len(lst)):
        print(f"Element: {lst[i]}, Positive Index: {i}, Negative Index: {-len(lst) + i}")

def main():
    # Taking input from the user
    user_input = input("Enter the elements of the list separated by spaces: ")

    # Converting the input string into a list
    lst = user_input.split()

    # Displaying elements with their positive and negative indices
    display_elements_with_indices(lst)

if __name__ == "__main__":
    main()
