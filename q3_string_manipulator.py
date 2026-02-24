#string manipulator program
#this program performs different operations on a sentence

#takes a sentence input from user
sentence = input("Enter a sentence: ")

#displaying original sentence
print("\nOriginal:", sentence)

#calculating total characters with spaces
total_chars = len(sentence)
print("characters(with spaces):",total_chars)

#calculating total characters without spaces
no_space = sentence.replace(" ", "")
print("characters(without spaces):",len(no_space))

#counting total words in sentence
words = sentence.split()
print("words:", len(words))

#converting sentence to uppercase
upper_text = sentence.upper()
print("UPPERCASE:",upper_text)

#converting sentence to lowercase
lower_text = sentence.lower()
print("lowercase:",lower_text)

#converting sentence to title case
title_text = sentence.title()
print("Tittle Case:",title_text)

#getting first word from sentence
first_word = words[0]
print("First Word:", first_word)

#getting last word from sentence
last_word = words[-1]
print("Last Word:", last_word)

#reversing the sentence
reversed_text = sentence[::-1]
print("Reversed:",reversed_text)