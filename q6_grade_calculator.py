#grade calculator program
#this program calculates total,percentage,gradeand pass/fail result

#taking marks of 5 subjects from user
sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))
sub4 = int(input("Enter marks for subject 4: "))
sub5 = int(input("Enter marks for subject 5: "))

#calculating total marks
total = sub1 + sub2 + sub3 + sub4 + sub5

#calculating percentage
percentage = total / 5

#assigning grade based on percentage
if percentage >= 90: grade = "A+"
elif percentage >= 80: grade = "A"
elif percentage >= 70: grade = "B"
elif percentage >= 60: grade = "C"
elif percentage >= 50: grade = "D"
else:
  grade = "F"

#checking pass/fail (eacch subject >= 40)
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40: result = "pass"
else:
  result = "Fail"

#displaying results
print("\n=== RESULT===")
print("marks:" , sub1, sub2, sub3, sub4, sub5)
print("total marks:", total, "/500")
print("percentage:", percentage)
print("grade:", grade)
print("result:", result)