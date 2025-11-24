#Area and Perimeter of Triangle
def area_of_triangle(base, height):
    return 0.5 * base * height
def perimeter_of_triangle(a, b, c):
    return a + b + c
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
side_a = float(input("Enter side a of the triangle: "))
side_b = float(input("Enter side b of the triangle: "))
side_c = float(input("Enter side c of the triangle: "))
print("Area of triangle:", area_of_triangle(base, height))
print("Perimeter of triangle:", perimeter_of_triangle(side_a, side_b, side_c))