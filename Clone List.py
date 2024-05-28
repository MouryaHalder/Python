def clone_list(original_list):
    # Method 1: Using the list() constructor
    clone1 = list(original_list)

    # Method 2: Using slicing
    clone2 = original_list[:]

    # Method 3: Using the copy() method
    clone3 = original_list.copy()

    return clone1, clone2, clone3

def main():
    # Taking input from the user
    user_input = input("Enter the elements of the list separated by spaces: ")
    
    # Converting the input string into a list
    original_list = user_input.split()
    
    # Cloning the list using different methods
    clone1, clone2, clone3 = clone_list(original_list)
    
    # Displaying the original and cloned lists
    print("Original list:", original_list)
    print("Clone 1 (using list() constructor):", clone1)
    print("Clone 2 (using slicing):", clone2)
    print("Clone 3 (using copy() method):", clone3)

if __name__ == "__main__":
    main()
