# Author: SMR (AMDG) 11/14/21
word=(input("Enter your first word: "))
word2=(input("Enter your second word: "))
word3=list(word)
word4=list(word2)
word3.sort()
word4.sort()

if word3 == word4:
    print("These words are anagrams.")
else:
    print("These words are not anagrams.")