#1,Arithmetic Calculator
##Take two numbers from the user and print their sum, difference, product, quotient, floor quotient, remainder, and power.
'''a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print("Floor Quotient:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)'''

#2,Even or Odd Without %
##Determine whether a number is even or odd without using the modulo operator. Use a bitwise operator.
'''n = int(input("Enter a number: "))
print("Even" if (n & 1) == 0 else "Odd")'''

#3,Largest of Three
##Take three integers and find the largest using only comparison operators and a ternary expression. Don't use max().
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
largest = a if a > b and a > c else (b if b > c else c)
print("Largest:", largest)'''

#4,Divisibility Checker
##Take a number and print whether it is divisible by both 3 and 5, divisible by only one of them, or divisible by neither.
'''n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
elif n % 3 == 0 or n % 5 == 0:
    print("Divisible by only one of them")
else:
    print("Divisible by neither")'''
    
#5,Bit Manipulation--Given an integer n, write a program that:
##sets the 2nd bit
###clears the 3rd bit
####toggles the 4th bit
#####checks whether the 5th bit is set
######Assume bit positions start from 0.
'''n = int(input("Enter an integer: "))
n = n | (1 << 1)
n = n & ~(1 << 2)
n = n ^ (1 << 3)
fifth_bit = (n & (1 << 4)) != 0

print("Final number:", n)
print("5th bit is set:", fifth_bit)'''

#6,Power of Two--Write a program that checks whether a positive integer is a power of 2 using bitwise operators, without loops.
'''n = int(input("Enter a positive integer: "))
result = n > 0 and (n & (n - 1)) == 0
print("Power of 2:", result)'''

#7,Swap Without Temporary Variable
###Take two integers and swap them without using a third variable.
####Restriction: don't use tuple unpacking.
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a,b=b,a

print("After swapping:")
print("a =", a)
print("b =", b)'''

#8,Simple Grade Evaluator -- Input marks from 0–100 and produce:
##A → 90–100 | B → 75–89 | C → 60–74 | D → 40–59 | F → below 40
###Use a nested ternary expression rather than if/elif/else.
'''marks = int(input("Enter marks: "))
grade = "A" if marks >= 90 else ("B" if marks >= 75 else ("C" if marks >= 60 else ("D" if marks >= 40 else "F")))

print("Grade:", grade)'''

#9,Bitwise Number Transformation--Given n, calculate: result = ((n << 2) | (n >> 1)) ^ 7
##Print n, its binary representation, and the final result with its binary representation.
###Don't use any library for the bitwise calculation.
'''n = int(input("Enter an integer: "))
result = ((n << 2) | (n >> 1)) ^ 7

print("n =", n)
print("Binary of n =", bin(n))
print("Result =", result)
print("Binary of result =", bin(result))'''

#10,Operator Master Challenge --Take three integers a, b, and c.
##Create one Boolean expression that is True only when:
##a is greater than b,b is not equal to c,a is even,c is either negative or greater than 100.
###Restrictions:
##One Boolean expression only.Must use comparison + logical + bitwise operators.No if, elif, else.No abs(), max(), or min()
'''a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
result = (a > b) and (b != c) and ((a & 1) == 0) and ((c < 0) or (c > 100))

print(result)'''
