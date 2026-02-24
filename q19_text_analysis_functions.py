#text analysis using functions
#count words
def count_words(text):
  words = text.split()
  return len(words)

#count vowels
def count_vowels(text):
  vowels = "aeiouAEIOU"
  count = 0
  for ch in text:
    if ch in vowels:
      count += 1
  return count

#count consonants
def count_consonants(text):
  vowels = "aeiouAEIOU"
  count = 0
  for ch in text:
    if ch.isalpha() and ch not in vowels:
      count += 1
  return count

#reverse text
def reverse_text(text):
  return text[::-1]

#check palindrome
def is_palindrome(text):
  clean = text.replace(" ", "").lower()
  return clean == clean[::-1]

#remove vowels
def remove_vowels(text):
  vowels = "aeiouAEIOU"
  result = ""
  for ch in text:
    if ch not in vowels:
      result += ch
  return result

#word frequency
def word_frequency(text):
  words = text.lower().split()
  freq = {}
  for word in words:
    freq[word] = freq.get(word, 0) + 1
  return freq

#longest word
def longest_word(text):
  words = text.split()
  longest = max(words, key=len)
  return longest, len(longest)

#analyze text (main function)
def analyze_text(text):
  print("\n=== TEXT ANALYSIS ===")
  print("Words:", count_words(text))
  print("Vowels:", count_vowels(text))
  print("Consonants:", count_consonants(text))
  print("Reversed:", reverse_text(text))

  if is_palindrome(text):
    print("Palindrome: Yes")
  else:
    print("Palindrome: No")
    print("Without vowels:", remove_vowels(text))
    word, length = longest_word(text)
    print("Longest word:", word, f"({length} letters)")
    freq = word_frequency(text)
    print("Word Frequency:", freq)

# user input
text = input("Enter text: ")
analyze_text(text)

