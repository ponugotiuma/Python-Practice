#Check if two variables point to the same list
a = [1, 2, 3]
b = a

print(a is b)
print(a == b)

#Validate a 4-digit PIN
p = "1234"

if len(p) == 4 and p.isdigit():
    print("Valid PIN")
else:
    print("Invalid PIN")
    
#Build 'Name: Asha | Age: 25' using f-string
name = "Asha"
age = 25
print(f"Name: {name} | Age: {age}")

#Compute 2**10 and 10**2
a = 2 ** 10
b = 10 ** 2

print(a)
print(b)
print(a > b)

#Check if a number is even using bitwise AND
n = 24

if n & 1 == 0:
    print("Even")
else:
    print("Odd")

#Slice the year from '15-01-2024'
s = "15-01-2024"
year = s[-4:]
print(year)

#Validate age range with permit override
age = 16
has_permit = True

if (18 <= age <= 60) or has_permit:
    print("Allowed")
else:
    print("Not allowed")

#Title-case a sentence from input()
s = input("Enter a sentence: ")
print(s.title())

#Zero-pad a number to 5 digits
n = 42
print(str(n).zfill(5))

#Build a hyphen-separated date using join()
y = 2024
m = 1
d = 15
date = "-".join(map(str, [y, m, d]))
print(date)

#Check whether a string is entirely uppercase
s = "HELLO"
print(s.isupper())

#Use a raw string for a Windows path
path = r"C:\Users\Asha"
print(path)

#Average of digits in '13579'
s = "13579"
average = sum(int(c) for c in s) / len(s)
print(average)
