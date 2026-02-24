#program to generate multiplication table generator program
#this program asks the user for a number and range, then prints multiplication table

# taking number input from user
num = int(input("Enter the number: "))

# taking range input
end_range = int(input("Enter range (end):"))
print("\nmultiplication table of", num)

# loop to generate multiplication table
for i in range(1, end_range + 1):
    print(num, "x", i, "=", num * i)

#bonus part full 1–10 table grid
print("\ncomplete table from 1 to 10:\n")
for i in range(1, 11):
  for j in range(1, 11):
      print(i * j, end="\t")  
  print()   