#age calculator program
#this program calculates age in different units

#taking birth year from user
birth_year = int(input("Enter your birth year: "))

#setting current year manually
current_year = 2026

#calculating current age
age = current_year - birth_year

#calculating age in different units
months = age*12
days = age*365
hours = days*24

minutes = hours*60

#calculating years untill age 100
years_to_100 = 100 - age

#displaying results
print("current age:", age, "years")
print("age in months:", months)
print("age in days:", days)
print("age in hours:", hours)
print("age in minutes:", minutes)
print("years left to reach 100:", years_to_100)