#Complex String Methods
#Q1
'''text = "  Python is Powerful  "
result = text.strip().lower().replace("powerful", "awesome")
print(result)'''

#Q2
'''text = "apple,banana,orange,grape"
items = text.split(",")
result = "-".join(items[::-1])
print(result)'''

#Q3
'''text = "PythonProgramming"
print(text.find("Pro"))
print(text.rfind("m"))
print(text.count("o"))
print(text.startswith("Py"))
print(text.endswith("ing"))'''

#Q4
'''text = "Hello-Python-World"
a = text.partition("-")
b = a[2].rpartition("-")
print(a)
print(b)
print(b[0].upper())'''

#Q5 
'''text = "  Data Science Python  "
result = (
    text.strip()
        .swapcase()
        .replace(" ", "_")
)

print(result)
print(result.count("_"))
print(result.startswith("dATA"))
print(result.endswith("pYTHON"))'''
