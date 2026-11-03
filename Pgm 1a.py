# Read two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display menu
print("\nChoose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter your choice (1-4): "))
# Perform operation based on choice
if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
       print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice! Please enter a number between 1 and 4.")
