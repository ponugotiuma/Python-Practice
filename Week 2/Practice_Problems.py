#Check if 'racecar' is a palindrome
'''s = "racecar"

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")'''

#Build a table row with aligned columns
'''name = "Asha"
age = 25
score = 95

print(f"{name:<10}{age:>5}{score:>8}")'''

#Check if 'asha_99' is alphanumeric
'''s = "asha_99"

print(s.isalnum())'''

#FizzBuzz for a single number using ternary chaining
'''n = 15

result = "FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else str(n)

print(result)'''

#Convert 37 to binary, octal, and hexadecimal
'''n = 37
print(bin(n))
print(oct(n))
print(hex(n))'''

#Predict round(7.5) and round(8.5)
'''print(round(7.5))
print(round(8.5))'''

#Compute 5 to the power 0.5
'''result = 5 ** 0.5
print(result)'''

#Reverse each word but keep word order
'''s = "Hello World"
result = " ".join(word[::-1] for word in s.split())
print(result)'''

#Count vowels in 'Consistency AI'
'''s = "Consistency AI"
count = sum(1 for c in s.lower() if c in "aeiou")
print(count)'''

#Remove punctuation and split into words
'''s = "Hello, World!"
s = s.replace(",", "").replace("!", "")
words = s.split()
print(words)'''

#Label temperature as hot/mild/cold using ternary
'''temp = 25
result = "hot" if temp >= 30 else "mild" if temp >= 20 else "cold"
print(result)'''
