#Write a Python program to count the number of words in a service description.
ser_desc="This service is only provided for the students, not for professionals"

words=ser_desc.split()
count=len(words)
print(words)
print("The total words are :", count)
