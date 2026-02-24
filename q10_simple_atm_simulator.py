#simple atm simulator program
#inintial balance = 10000
balance = 10000
while True:
  print("\n=== ATM MENU ===")
  print("1. check balance")
  print("2. deposit money")
  print("3. withdraw money")
  print("4. exit")

  choice = int(input("Enter ypur choice: "))

  #check balance
  if choice == 1:
    print("current balance:", balance)

  #deposit money
  elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("deposit successful!")
    print("updated balance:", balance)

  #withdraw money
  elif choice == 3:
    amount = float(input("Enter amount to withdraw: " ))

    if amount > balance:
      print("insufficient balance!")
    elif balance - amount < 500:
      print("minimum balance of 500 must remain!")
    else:
      balance -= amount
      print("withdrawal successful!")
      print("updated balance:", balance)

  #exit
  elif choice == 4:
    print("thank you for using atm")
    break
  else:
    print("invalid choice!")
