#1,Write a Python program to take a string from the user and print it in uppercase, lowercase, and title case.
'''name=input("Enter string:")
print(name.upper())
print(name.lower())
print(name.title())'''

#2,Write a Python program to take a string from the user and count how many times a particular character appears in it.
'''s=input("Enter String:")
char=input("Enter character to count:")
count=s.count(char)
print(count)'''

#3,Write a Python program to take a sentence from the user and replace every space with -.
'''sentence = input("Enter a sentence: ")
result = sentence.replace(" ", "-")
print("Result:", result)'''

#4,Write a Python program to take a comma-separated string such as "Python,Java,C++" and convert it into a list using split().
'''text = input("Enter words separated by commas: ")
words = text.split(",")
print("List:", words)'''

#5,Write a Python program to take a list of words and combine them into a single string using join(), with - between each word.
'''words = input("Enter words separated by spaces: ").split()
result = "-".join(words)
print("Result:", result)'''

#6,Write a Python program to take a string and check whether it starts with "Python" and ends with "ing" using startswith() and endswith().
'''text = input("Enter a string: ")
starts = text.startswith("Python")
ends = text.endswith("ing")
print("Starts with Python:", starts)
print("Ends with ing:", ends)'''

#7,Write a Python program to take a string and find the position of the first occurrence of a given substring using find().
'''text = input("Enter a string: ")
substring = input("Enter the substring to find: ")
position = text.find(substring)
print("Position:", position)'''

#8,Write a Python program to take a string containing extra spaces at the beginning and end, remove those spaces, and then convert the string to uppercase.
'''text = input("Enter a string: ")
result = text.strip().upper()
print("Result:", result)'''

#9,Write a Python program to take a sentence and:remove leading/trailing spaces,convert it to lowercase,replace every occurrence of "python" with "programming".
'''sentence = input("Enter a sentence: ")
result = sentence.strip().lower()
result = result.replace("python", "programming")
print("Result:", result)'''

#10,Write a Python program to take two strings from the user and check whether they are equal using the == operator. Also check whether the first string is different from the second using !=.
'''str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Equal:", str1 == str2)
print("Different:", str1 != str2)'''

#11,Write a Python program to take two numbers and display:addition,subtraction,multiplication,floor division,modulus,exponentiation.
'''x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)'''

#12,Challenge:Write a Python program that takes a sentence from the user and:removes extra spaces from both ends,converts the sentence to lowercase,splits it into words,counts the number of words,joins the words using _,prints the final modified sentence.
sentence = input("Enter a sentence: ")
sentence = sentence.strip()
sentence = sentence.lower()
words = sentence.split()
count = len(words)
result = "_".join(words)

print("Number of words:", count)
print("Final sentence:", result)
