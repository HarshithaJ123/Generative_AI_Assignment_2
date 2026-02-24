# Simple calulator program
#Takes two numbers and performs arithemetic operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number "))

#performing calculations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
#checking division by zero
if num2 != 0:
  div = num1 / num2
  mod = num1 % num2
else:
  div = "not possible"
  mod = "not possible"

exp = num1 ** num2

#display results
print("\nResults:")
print(num1, "+", num2, "=", add)
print(num1, "-", num2, "=", sub)
print(num1, "*", num2, "=", mul)
print(num1, "/", num2, "=", div)
print(num1, "%", num2, "=", mod)
print(num1, "^", num2, "=", exp)