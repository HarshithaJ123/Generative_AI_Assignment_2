#ticket pricing system program
#calculate movie ticket price based on age and day discount

#taking inputs
age = int(input("Enter age: "))
day = input("Enter day of week: ").lower()
tickets = int(input("Enter number of tickets: "))

#deciding base price based on age
if age < 3:
  base_price = 0
elif age <= 12:
 base_price = 150
elif age <= 59:
  base_price = 300
else:
  base_price = 200

#checking day discount
if day in ["friday", "saturday", "sunday"]:
  discount = 0.20   #20% discount
else:
  discount = 0

#calculating price
price_after_discount = base_price - (base_price * discount)
total_amount = price_after_discount * tickets

#displaying output
print("\n === Ticket Details ===")
print("base price per ticket:", base_price)
print("discount applied:", discount * 100, "%")
print("price after discount:", price_after_discount)
print("total amount:", total_amount)