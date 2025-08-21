# Task 1: Basic Mathematical Operations

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero not allowed)"

# Displaying results
print(f"\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
