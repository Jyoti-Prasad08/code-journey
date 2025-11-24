def add(a,b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
results = add(a, b)
print("Sum:", results[0])
print("Subtraction:", results[1])
print("Multiplication:", results[2])
print("Division:", results[3])
