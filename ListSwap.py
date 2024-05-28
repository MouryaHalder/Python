def swap_first_elements(list1, list2):
    # Swapping the first elements of the lists
    list1[0], list2[0] = list2[0], list1[0]
    return list1, list2

def main():
    # Taking input from the user for the first list
    list1 = input("Enter the first list of elements separated by spaces: ").split()
    
    # Taking input from the user for the second list
    list2 = input("Enter the second list of elements separated by spaces: ").split()

    # Swapping the first elements
    list1, list2 = swap_first_elements(list1, list2)

    # Displaying the second element of the first list after the swap
    if len(list1) > 1:
        print("The second element in the first list after swapping is:", list1[1])
    else:
        print("The first list does not have a second element.")

if __name__ == "__main__":
    main()
