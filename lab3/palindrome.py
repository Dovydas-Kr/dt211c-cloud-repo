import string

# Program that checks if a string is palindrome.
word = raw_input("Enter a string: ")

word1 = word.lower()
word2 = reversed(word1)

if list(word1) == list(word2):
   print("True")
else:
   print("False")