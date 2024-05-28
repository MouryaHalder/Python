

from prettytable import PrettyTable

def convert_list_to_table(data):
    # Create a PrettyTable object
    table = PrettyTable()

    # Adding columns to the table
    table.field_names = ["Index", "Value"]

    # Adding rows to the table
    for index, value in enumerate(data):
        table.add_row([index, value])

    return table

def main():
    # Taking input from the user
    user_input = input("Enter the elements of the list separated by spaces: ")

    # Converting the input string into a list
    data_list = user_input.split()

    # Converting the list to a table
    table = convert_list_to_table(data_list)

    # Displaying the table
    print(table)

if __name__ == "__main__":
    main()
