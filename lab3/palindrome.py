# Program that checks if a string is palindrome.
import string
#Asks for input
word = raw_input("Enter a string: ")

#changes string to lover case
word1 = word.lower()
#reverses string
word2 = reversed(word1)

#Checks if strings are the same
if list(word1) == list(word2):
   print("True")
else:
   print("False")