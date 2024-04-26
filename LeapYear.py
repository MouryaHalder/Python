def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    # Taking input from the user
    year = int(input("Enter a year: "))

    # Checking if the year is a leap year
    if is_leap_year(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

if __name__ == "__main__":
    main()
