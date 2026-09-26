## 1,Create & Access a Dictionary : Create a dictionary containing a student's name, age, and marks. Print the name and marks.
student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}
print("Name:", student["name"])
print("Marks:", student["marks"])

## 2,Add & Update Dictionary Values : Add a city key and update the student's marks to 90.
student = {
    "name": "Anil",
    "age": 21,
    "marks": 75
}
student["city"] = "Hyderabad"
student["marks"] = 90
print(student)

## 3,Check Whether a Key Exists : Check whether "phone" exists in the dictionary.
student = {
    "name": "Priya",
    "age": 20,
    "course": "CSE",
    "email": "priya@gmail.com"
}
if "phone" in student:
    print("Phone number exists")
else:
    print("Phone number does not exist")

## 4,Print All Keys and Values : Print all the keys and all the values separately.
product = {
    "name": "Laptop",
    "price": 55000,
    "brand": "Dell",
    "stock": 10
}
print("Keys:")
for key in product.keys():
    print(key)
print("\nValues:")
for value in product.values():
    print(value)

## 5,Calculate Total Marks : Calculate and print the total marks from the dictionary.
marks = {
    "Python": 85,
    "SQL": 90,
    "Excel": 80,
    "Power BI": 75
}
total = 0
for mark in marks.values():
    total = total + mark

print("Total Marks:", total)
