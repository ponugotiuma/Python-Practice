#SETS — New Problems
##1. Find Missing Numbers
'''numbers = [1, 2, 3, 5, 6, 8, 10]
all_numbers = set(range(1, 11))
given_numbers = set(numbers)
missing = all_numbers - given_numbers
print(missing)'''

##2. Check Whether a Set Is a Subset
'''a = {2, 4}
b = {1, 2, 3, 4, 5}
result = a.issubset(b)
print(result)'''

##3.Check Whether Sets Are Disjoint
'''a = {1, 2, 3}
b = {4, 5, 6}
result = a.isdisjoint(b)
print(result)'''

##4.Find Elements Present in All 3 Lists
'''a = [1, 2, 3, 4, 5]
b = [2, 3, 5, 6]
c = [2, 5, 7, 8]
set_a = set(a)
set_b = set(b)
set_c = set(c)
common = set_a & set_b & set_c
print(common)'''

##5. Find Unique Words
'''sentence = "python is easy and python is powerful"
words = sentence.split()
unique_words = set(words)
print(unique_words)'''

#DICTIONARIES — New Problems
##6. Find the Student With Highest Marks
'''marks = {
    "Ravi": 85,
    "Anu": 92,
    "Kiran": 78,
    "Priya": 95
}
highest_student = max(marks, key=marks.get)
print(highest_student)'''

##7. Find All Students With 90 Marks
'''marks = {
    "Ravi": 90,
    "Anu": 80,
    "Kiran": 90,
    "Priya": 70
}
students = []
for name, mark in marks.items():
    if mark == 90:
        students.append(name)
print(students)'''

##8. Invert a Dictionary
'''data = {
    "a": 1,
    "b": 2,
    "c": 3
}
inverted = {}
for key, value in data.items():
    inverted[value] = key
print(inverted)'''

##9. Merge Two Dictionaries
'''a = {
    "name": "Ravi",
    "age": 21
}
b = {
    "branch": "CSE",
    "year": 4
}
a.update(b)
print(a)'''

##10. Find Common Keys
'''a = {
    "name": "Ravi",
    "age": 21,
    "city": "Hyderabad"
}
b = {
    "age": 22,
    "city": "Vijayawada",
    "branch": "CSE"
}
common_keys = a.keys() & b.keys()
print(common_keys)'''
