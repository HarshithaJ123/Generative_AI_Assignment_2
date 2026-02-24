#number pattern printer program
#this program prints 4 different number patterns
while True:
  print("\n=== Number Pattern Menu ===")
  print("1. Pattern 1")
  print("2. Pattern 2")
  print("3. Pattern 3")
  print("4. Pattern 4")
  print("5. Exit")

  choice = int(input("Enter pattern number(1-5): "))

  if choice == 5:
    print("Exiting program")
    break
  n = int(input("Enter height: "))

  #pattern 1
  if choice == 1:
    print("\nPattern 1:")
    for i in range(1, n + 1):
      for j in range(1, i + 1):
         print(j, end=" ")
      print()

  #pattern 2
  elif choice == 2:
    print("\nPattern 2:")
    for i in range(1, n + 1):
      for j in range(i):
        print(i, end=" ")
      print()

  #pattern3
  elif choice == 3:
    print("\nPattern 3:")
    for i in range(n, 0, -1):
      for j in range(i, 0, -1):
        print(j, end=" ")
      print()

  #pattern 4
  elif choice == 4:
    print("\nPattern 4:")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
         print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

  else:
    print("invalid choice!")
     

