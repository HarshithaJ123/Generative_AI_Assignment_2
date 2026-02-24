#personal bio card program
#Storing personal details in variables
name = "Harshitha J"
age = 23 
course = "Master Of Computer Applications"
college = "Vidya Vikas Institute Of Engineering And Technology"
email = "harshithaj615@gmail.com"

#creating border line using repeated = symbols
border = "=" * 71

#print top border
print(border)

#print the title of Bio card at middle
print(f"|{'STUDENT BIO CARD':^69}|")

#print border again
print(border)

#displaying personal details already stored in variables
print(f"|  Name   :    {name:<55}|")
print(f"|  Age   :     {age:<55}|")
print(f"|  Course   :  {course:<55}|")
print(f"|  College   : {college:<55}|")
print(f"|  Email   :   {email:<55}|")

#print bottom border to complete box
print(border)
