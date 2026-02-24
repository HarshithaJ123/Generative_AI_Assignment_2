#sum and average calculator program
#program to find sum,average,maximum,minimum of numbers

# ask how many numbers user wants to enter
n = int(input("How many numbers"))
total = 0
nums = []

# taking numbers using loop
for i in range(1, n + 1):
  value = int(input(f"Enter number: "))
  nums.append(value)
  total += value

# calculations
average = total / n
maximum = max(nums)
minimum = min(nums)

# displaying results
print("\nResults:")
print("total Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)