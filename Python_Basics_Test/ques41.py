#Write a Python program to check whether a given string is a palindrome using slicing.
s='madam'
if s==s[::-1]:
    print(s ,"is palindrome")
else :
    print(s ,"is not a palindrome")
