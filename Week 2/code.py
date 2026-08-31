#Number bases
'''print(bin(10), oct(15), hex(255))'''

'''b = 0b1010 
o = 0o17
h = 0xFF
print(b,o,h)'''

#Floating-point precision
'''a = 0.1 + 0.2
print(a == 0.3)
print(abs(a - 0.3) < 1e-9) '''

#Convert 0b1111 to decimal by hand, then check with bin()
'''b=0b1111
print(b)
print(bin(15))'''

#Write 200 in binary, octal, and hex using bin/oct/hex
'''print(bin(200),oct(200),hex(200))'''

#Rounding
'''print(round(4.5) , round(5.5))''' #4,6

#Round 3.14159 to 3 decimal places
'''print(round((3.14159), 3))'''

#Round 2500 to the nearest thousand using round()
'''print(round(2500, -3))'''

#Sum the numbers 1 to 100 using sum(range(...))
'''print(sum(range(1,101)))'''

# A program should read an age and double it, but must not crash on bad input.
'''nrml=input("Enter Age:")
try:
    age=int(nrml)
    print(f"Double your age by '{age * 2}' ")
except ValueError:
    print(f"please enter a valid number. '{nrml}' is not a whole number!")'''

#Check if 'Consistency' is a palindrome using slicing
'''s='mam'
if s==s[::-1]:
    print(f" '{s}' is palindrome.")
else:
    print(f" '{s}' is not a palindrome.")'''

#Print every 3rd character of 'abcdefghij'
'''s='abcdefghij'
print(s[::3])'''

#Get the domain from 'user@email.com' using slicing
'''s='user@email.com'
print(s[-9:])'''

#Extract the file extension from 'report.pdf'
'''s='report.pdf'
print(s[-4:])'''

#Write a slice that extracts every character except the first and last
'''s='Python'
print(s[1:-1])'''

#Modification of a string
'''s = "  hello world  "
s = s.strip()
s = s.upper()              
s = s.replace("WORLD" , "PYTHON")
print(s)'''

# str.format()
'''name, age = "Asha", 25
print("{} is {}".format(name, age))'''

# % formatting (the old, printf-style way)
'''name, age = "Asha", 25
print("%s is %d" % (name, age))'''

#Strip whitespace then uppercase a padded string in one chain
'''s="       Hello        "
print(s.strip().upper())'''

#Concatenate first and last name with a space
'''first,last='Uma','Ponugoti'
print(first + ' '  + last)'''

#Build a 30-character divider line of hyphens
'''print('-'*30)'''

#Join ['red','green','blue'] with commas
'''colors=['red','green','blue']
print(','.join(colors))'''

#Use += to build 'Python' from 'Py' and 'thon'
'''msg="Py"
msg += "thon"
print(msg)'''

#Pad the number 7 to 4 digits with leading zeros
'''x=7
print(f"{x:04d}")'''

#Format 0.5 as a percentage with no decimals
'''x=0.5
print(f"{x:.0%}")'''

#Right-align 'hi' in a field of width 10
'''s='hi'
print(f"{s:>10}")'''

#Print a string containing an escaped tab and newline
'''print("My name is Uma\nI'm 20 years old\tHow old areyou?")'''

#Print a string containing both single and double quotes
'''print("Hi i'm Uma" + ' ' + 'and you?')'''

#Build a formatted receipt line: item, qty, price aligned
'''print("Item\tqty\tprice")
print("Soap\t2\t200")'''

#Format -5 with a forced + or - sign using :+d
'''x=-10
print(f"{x:+d}")'''

#Print a raw string that intentionally keeps \n literal
'''print(r'line1\nline2')'''

#Combine an f-string with a nested format spec variable
'''x=3.14295982
width=0
print(f'{x:{width}.2f}')'''
