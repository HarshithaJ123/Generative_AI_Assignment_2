#leap year checker program
#this program checks whether a year is a leap year

year = int(input("Enter a year: "))

#checking leap year condition
if year % 4 == 0:
  if year % 100 != 0 or year % 400 == 0:
    print(year,"is a leap year.")
    print("Reason: Divisible by 4 and not divisible by 100 unless divisible by 400.")
  else:
    print(year, "is not a leap year.")
    print("Reason: Divisible by 100 but not divisible by 400.")
else:
  print(year, "is not a leap year.")
  print("Reason: not divisible by 4.")
  
  

