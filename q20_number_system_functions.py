#Number System Functions Program
#1.factorial
def factorial(n):
  fact = 1
  for i in range(1, n + 1):
    fact *= i
  return fact

#prime check
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

#fibonacci
def fibonacci(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a + b
  return a

#sum of digits
def sum_of_digits(n):
  return sum(int(digit) for digit in str(n))

#reverse number
def reverse_number(n):
  return int(str(n)[::-1])

#armstrong number
def is_armstrong(n):
  digits = str(n)
  power = len(digits)
  total = sum(int(digit) ** power for digit in digits)
  return total == n

#gcd
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

#lcm
def lcm(a, b):
  return (a * b) // gcd(a, b)

#perfect number
def is_perfect_number(n):
  total = 0
  for i in range(1, n):
    if n % i == 0:
      total += i
  return total == n

#menu
def math_menu():
  while True:
    print("\n==== NUMBER SYSTEM MENU ====")
    print("1. Factorial")
    print("2. Prime Check")
    print("3. Fibonacci")
    print("4. Sum of Digits")
    print("5. Reverse Number")
    print("6. Armstrong Number")
    print("7. GCD")
    print("8. LCM")
    print("9. Perfect Number")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      n = int(input("Enter number: "))
      print("Factorial =", factorial(n))
    elif choice == 2:
      n = int(input("Enter number: "))
      if is_prime(n):
        print("Prime number")
      else:
        print("Not a prime number")

    elif choice == 3:
      n = int(input("Enter n: "))
      print("Fibonacci =", fibonacci(n))

    elif choice == 4:
      n = int(input("Enter number: "))
      print("Sum of digits =", sum_of_digits(n))

    elif choice == 5:
      n = int(input("Enter number: "))
      print("Reversed number =", reverse_number(n))

    elif choice == 6:
      n = int(input("Enter number: "))
      if is_armstrong(n):
        print("Armstrong number")
      else:
        print("Not an Armstrong number")

    elif choice == 7:
      a = int(input("Enter first number: "))
      b = int(input("Enter second number: "))
      print("GCD =", gcd(a, b))

    elif choice == 8:
      a = int(input("Enter first number: "))
      b = int(input("Enter second number: "))
      print("LCM =", lcm(a, b))

    elif choice == 9:
      n = int(input("Enter number: "))
      if is_perfect_number(n):
        print("Perfect number")
      else:
        print("Not a perfect number")

    elif choice == 10:
      print("Exiting program...")
      break

    else:
      print("Invalid choice!")

# run program
math_menu()




  