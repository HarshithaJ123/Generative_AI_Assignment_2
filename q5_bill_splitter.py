#bill splitter program
#this program calculates restaurant bill and splits among people

#taking inputs from user
total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tax_percent = float(input("Enter tax percentage: "))
tip_percent = float(input("Enter tip percentage: "))

#calculating sub total
subtotal = total_bill

#calculating tax amount
tax_amount = (subtotal * tax_percent) / 100

#calculating bill after tax
after_tax = subtotal + tax_amount

#calculating tip amount
tip_amount = (after_tax * tip_percent)/ 100

#calculating total bill
total_amount = after_tax + tip_amount

#calculating amount per person
per_person = total_amount / people

#displaying bill breakdown
print("\n=== BILL BREAKDOWN ===")
print("subtotal: ₹", subtotal)
print("tax amount: ₹", tax_amount)
print("after tax: ₹", after_tax)
print("tip amount: ₹", tip_amount)
print("total bill: ₹", total_amount)
print("amount per person: ₹", per_person)