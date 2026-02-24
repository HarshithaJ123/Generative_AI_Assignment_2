#temperature converter program
#menu based temperature conversion

while True:
  print("\n=== Temperature Converter ===")
  print("1. Celsius to Fahrenheit")
  print("2. Fahrenheit to Celsius")
  print("3. Celsius to kelvin")
  print("4. kelvin to Celsius")
  print("5. Fahrenheit to kelvin")
  print("6. kelvin to Fahrenheit")
  print("7. exit")

  choice = int(input("Enter your choice (1-7): "))
  if choice == 1:
    c = float(input("Enter temperature in celsius: "))
    f = (c * 9/5) + 32
    print("Result:", f, "F")

  elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Result:", c, "C")

  elif choice == 3:
    c = float(input("Enter temperature in celsius: "))
    k = c + 273.15
    print("Result:", k, "K")

  elif choice == 4:
    k = float(input("Enter temperature in kelvin: "))
    c = k - 273.15
    print("Result:", c, "C")

  elif choice == 5:
    f = float(input("Enter temperature in Fahrenheit: "))
    k = (f - 32) * 5/9 + 273.15
    print("Result:", k, "K")

  elif choice == 6:
    k = float(input("Enter temperature in kelvin: "))
    f = (k - 273.15) * 9/5 + 32
    print("Result:", f, "F")

  elif choice == 7:
    print("Exiting program")
    break
  else:
    print("invalid choice. please try again.")





  



  

   

