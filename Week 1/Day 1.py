#Write an if-block with two indented lines and one line outside it
'''age=20
if age>18:
    print("U are Major")
    print("Eligible for vote")'''

#Spot the bug: an if with the body not indented
'''if age>21:
print("U may completed ur degree")'''

#Spot the bug: mixed 2-space and 4-space indentation
'''if age>18:
    print("U are MAjor")
  print("Eligible for Vote")'''

#Show that Python is case-sensitive using two variables
'''age=18
Age=20
print(age)
print(Age)'''

#Write a multi-line list using implicit continuation
'''Skills=[
    "python","Sql",
    "Excel","PowerBI",
    ]
print(Skills)'''

#Printing multiple values
'''print("Name:", "Asha", " ", "Age:", 25)'''

# Sep(separator) Parameter
'''print("2024", "01", "15", sep="-")
print("a", "b", "c", sep="")
print("x", "y", "z", sep=" | ")'''

#Combining Text&Variables
'''name = "Asha"
age = 25'''
## 1) f-string (Formatted String Literal)
'''print(f"{name} is {age} years old")'''
## 2) comma-separated values 
'''print(name, "is", age, "years old")'''
## 3) concatenation 
'''print(name + " is " + str(age) + " years old")'''

#Formatting numbers inside f-strings
'''pi = 3.14159265
print(f"{pi:.2f}")'''#returns 2 decimal places
'''print(f"{pi:.4f}")'''#returns 4 decimal places
'''price = 1250
print(f"{price:,}")'''#a separator according to the given value
'''ratio = 0.256
print(f"{ratio:.1%}")''' # returns the percentage under 100%  

#Docstrings
'''def greet(name):
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"
print(greet.__doc__)
help(greet)'''

#Print your name, age, and city on three separate lines
'''print("Name:","Uma" ,"\n" ,"Age:", 25, "\n", "city:" , "Kodad" )'''

#Print three values separated by hyphens using sep
'''print("a","b","c", sep="+")'''

#Print 'Loading...' then 'done' on the same line using end
'''print("Loading...","done", end="")'''

#Print a date as 2024/01/15 using sep
'''print("2024","01","15", sep="/")'''

#Build a sentence from name and age using an f-string
'''name="uma"
age=20
print(f"{name} is {age} years old")'''

#Print an empty line between two messages
'''print("Hello world")
print()
print("Welcome!!")'''
#Predict output
'''print('a','b',sep='',end='!')
print('c')'''

#Print a 3x3 box of stars using \n in one string
'''print("***\n***\n***")'''
