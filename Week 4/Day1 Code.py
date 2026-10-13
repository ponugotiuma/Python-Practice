#IF/ELIF and ELSE
##1,Condition
'''age = 20
print(age >= 18)
print(age < 18)
print(age == 20)'''

##2, IF-ELSE Statement
'''age = 20
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")'''

##3,IF-ELSE-ELIF statement
'''marks = 82
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"
print(grade)'''

##4,Chained comparisons
'''score=75
if 0 <= score <= 100:
    print("Valid Score")
else:
    print("Invalid score")'''

##5,ternary condition
'''age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)'''

##6,Truthiness
'''name = " "
if name:
    print("Name exists")
else:
    print("Name is empty")'''

##7,While Loops
###Numbers 1-5
'''i = 1
while i <= 5:
    print(i)
    i += 1'''
###Find the sum of numbers from 1 to N.
'''n = int(input("Enter N: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum:", total)'''

##8,Check whether a number is positive, negative or zero.
'''n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")'''
