#Area and Perimeter of Square
def area_of_square(side):
    return side * side
def perimeter_of_square(side):
    return 4 * side
side = float(input("Enter the side length of the square: "))
print("Area of square:", area_of_square(side))
print("Perimeter of square:", perimeter_of_square(side))
