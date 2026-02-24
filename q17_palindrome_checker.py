#program to check palindrome checker
#accepts word or number
# shows step-by-step verification
text = input("Enter word/number: ")

# original value
original_text = text

# convert to lower case for checking
lower_text = text.lower()

# reverse the value
reversed_text = lower_text[::-1]

# display steps
print("\nOriginal:", original_text)
print("Reversed:", reversed_text)

# checking palindrome
if lower_text == reversed_text:
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")