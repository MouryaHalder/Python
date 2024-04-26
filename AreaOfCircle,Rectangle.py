import math

def circle_area(radius):
    return math.pi * radius**2

def rectangle_area(length, width):
    return length * width

def square_area(side):
    return side**2

def main():
    print("Choose a shape to calculate its area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    
    choice = int(input("Enter your choice (1, 2, or 3): "))
    
    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius)
        print("The area of the circle is:", area)
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(length, width)
        print("The area of the rectangle is:", area)
    elif choice == 3:
        side = float(input("Enter the side length of the square: "))
        area = square_area(side)
        print("The area of the square is:", area)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
