#program to find factorial of a number
#calculates factorial using loop and shows step by step
num = int(input("Enter a number: "))

# handle negative numbers
if num < 0:
  print("Factorial not possible for negative numbers")

# factorial of 0
elif num == 0:
  print("0! = 1")
else:
  fact = 1
  steps = ""
  for i in range(num, 0, -1):
    fact = fact * i
    steps += str(i)
    if i != 1:
     steps += " x "

# display step-by-step result
print(f"{num}! = {steps} = {fact}")