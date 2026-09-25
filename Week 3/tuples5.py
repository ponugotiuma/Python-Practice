#Tuples as Dictionary Keys & Hashability
##1,Student ID + Subject as Tuple Key
'''marks = {
    (101, "Python"): 85,
    (101, "SQL"): 90,
    (102, "Python"): 92
}
print(marks[(101, "SQL")])'''

## 2,Count Points
'''points = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
count = {}
for point in points:
    if point in count:
        count[point] += 1
    else:
        count[point] = 1
print(count)'''

## 3,Product + Month Sales
'''sales = {
    ("Laptop", "Jan"): 50000,
    ("Laptop", "Feb"): 55000,
    ("Phone", "Jan"): 30000
}
print(sales[("Laptop", "Feb")])'''

## 4,Which Objects Are Hashable?
'''items = [
    (1, 2),
    [1, 2],
    "hello",
    {1, 2},
    ((1, 2), (3, 4)),
    (1, [2, 3])
]
for item in items:
    try:
        hash(item)
        print(item, "-> Hashable")
    except TypeError:
        print(item, "-> Not Hashable")'''

## 5,Fix the Unhashable Tuple
'''data = {
    (101, (10, 20)): "Rahul" #old --> data = {(101, [10, 20]): "Rahul"}
}
print(data[(101, (10, 20))])'''

## 6,City + Pincode
'''cities = {
    ("Hyderabad", 500001): 1000000,
    ("Delhi", 110001): 2000000,
    ("Mumbai", 400001): 1500000,
    ("Chennai", 600001): 1200000,
    ("Bengaluru", 560001): 1800000
}
print(cities[("Hyderabad", 500001)])'''

## 7,Count Payment Method + Month
'''transactions = [
    ("UPI", "January"),
    ("Cash", "January"),
    ("UPI", "January"),
    ("Card", "February"),
    ("UPI", "January")
]
count = {}
for transaction in transactions:
    if transaction in count:
        count[transaction] += 1
    else:
        count[transaction] = 1
print(count)'''

## 8,Check Hashability
'''a = (1, 2, 3)
b = (1, [2, 3])
c = ((1, 2), (3, 4))
d = (1, {2, 3})
items = [a, b, c, d]
for item in items:
    try:
        hash(item)
        print(item, "-> Hashable")
    except TypeError:
        print(item, "-> Not Hashable")'''

## 9,Attendance System
'''attendance = {
    (101, "Python"): 85,
    (101, "SQL"): 72,
    (102, "Python"): 68,
    (102, "SQL"): 90,
    (103, "Python"): 74
}
for key, percentage in attendance.items():
    if percentage < 75:
        print(key, percentage)'''

## 10,User Input Marks System
'''marks = {
    (101, "Python"): 85,
    (101, "SQL"): 90,
    (102, "Python"): 92,
    (102, "SQL"): 88
}
student_id = int(input("Enter student ID: "))
subject = input("Enter subject: ")
key = (student_id, subject)
if key in marks:
    print("Marks:", marks[key])
else:
    print("Record not found")'''
