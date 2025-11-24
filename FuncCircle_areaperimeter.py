#Area and Circumference of Circle
import math
def area_of_circle(radius):
    return math.pi * radius * radius
def circumference_of_circle(radius):
    return 2 * math.pi * radius
radius = float(input("Enter the radius of the circle: "))
print("Area of circle:", area_of_circle(radius))
print("Circumference of circle:", circumference_of_circle(radius))