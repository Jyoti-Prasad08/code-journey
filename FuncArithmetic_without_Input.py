def add(a,b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div
results = add(10, 5)
print("Sum:", results[0])
print("Subtraction:", results[1])
print("Multiplication:", results[2])
print("Division:", results[3])