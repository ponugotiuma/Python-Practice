#DICTIONARIES
##Creation
'''student = {
    "name": "Asha",
    "age": 21,
    "branch": "CSE"
}
print(student)'''

##Accessing Dictionary
'''print(student["name"])
print(student.get("salary"))'''
##Adding / Updating
'''student["city"] = "Hyderabad"
print(student["city"])
student["age"] = 22
print(student["age"])'''
##Deleting
'''student.pop("age")
print(student)'''

##Dictionary Loop
'''marks = {
    "Asha": 90,
    "Ravi": 85,
    "Kiran": 95
}'''
##Keys
'''for name in marks:
    print(name)'''
##Values
'''for score in marks.values():
    print(score)'''    
##Both
'''for name, score in marks.items():
    print(name, score)'''

##Count something / frequency problem
'''word = "hello"
count = {}
for ch in word:
    if ch not in count:
        count[ch] = 0
    count[ch] += 1
print(count)'''

## frequency using "counter" module
'''from collections import Counter
count = Counter("hello")
print(count)'''

##Problem — Grouping
'''from collections import defaultdict
words = ["apple", "banana", "avocado", "cherry", "blueberry"]
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
print(by_letter)'''
