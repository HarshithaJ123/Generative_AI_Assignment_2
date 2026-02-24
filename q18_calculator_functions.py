#calculator using functions program
#addition
def add(a, b):
  return a + b
#subtraction
def subtract(a, b):
  return a - b
#multiplication
def multiply(a, b):
  return a * b
#division (handle division by zero)
def divide(a, b):
  if b == 0:
      return "Cannot divide by zero"
  return a / b
#modulus
def modulus(a, b):
  return a % b
#power
def power(a, b):
  return a ** b

#main calculator menu function
def calculator():
  while True:
    print("\n--- CALCULATOR MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "7":
      print("Exiting calculator...")
      break
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
      print("Result:", add(a, b))

    elif choice == "2":
      print("Result:", subtract(a, b))

    elif choice == "3":
      print("Result:", multiply(a, b))

    elif choice == "4":
      print("Result:", divide(a, b))

    elif choice == "5":
      print("Result:", modulus(a, b))

    elif choice == "6":
      print("Result:", power(a, b))

    else:
      print("Invalid choice")

#call main function
calculator()