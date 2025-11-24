#Area and Perimeter of Rectangle
def area_of_rectangle(length, width):
    return length * width
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("Area of rectangle:", area_of_rectangle(length, width))
print("Perimeter of rectangle:", perimeter_of_rectangle(length, width))
