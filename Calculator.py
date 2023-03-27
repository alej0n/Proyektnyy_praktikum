# Calculator

# Define the functions for the operations
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  # Add a condition to avoid division by zero
  if b == 0:
    print("Cannot divide by zero")
    return None
  else:
    return a / b

# Ask the user to choose an operation
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

option = input("Enter your option (1/2/3/4): ")

# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the chosen operation and display the result
if option == "1":
  print(num1, "+", num2, "=", add(num1, num2))
elif option == "2":
  print(num1, "-", num2, "=", subtract(num1, num2))
elif option == "3":
  print(num1, "*", num2, "=", multiply(num1, num2))
elif option == "4":
  # Display the result only if it is not None
  result = divide(num1, num2)
  if result is not None:
    print(num1, "/", num2, "=", result)
else:
  print("Invalid option")