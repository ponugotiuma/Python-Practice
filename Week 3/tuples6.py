#Named Tuples
## 1,Student Names
from collections import namedtuple
'''Student = namedtuple("Student", ["name", "id", "branch"])
s1 = Student("Rahul", 101, "CSE")
s2 = Student("Priya", 102, "ECE")
s3 = Student("Arjun", 103, "EEE")
print(s1.name)
print(s2.name)
print(s3.name)'''

## 2,Employee Salary
'''Employee = namedtuple("Employee", ["name", "id", "salary"])
e1 = Employee("Rahul", 101, 50000)
print(e1.salary)'''

## 3,Products With Low Stock
'''Product = namedtuple("Product", ["name", "price", "stock"])
products = [
    Product("Laptop", 50000, 5),
    Product("Mouse", 800, 25),
    Product("Keyboard", 1500, 7),
    Product("Monitor", 12000, 15),
    Product("Headphones", 2000, 4)
]
for product in products:
    if product.stock < 10:
        print(product.name, product.stock)'''

## 4,Student Total Marks
'''Student = namedtuple("Student", ["name", "maths", "python", "sql"])
students = [
    Student("Rahul", 80, 85, 90),
    Student("Priya", 90, 92, 88),
    Student("Arjun", 75, 80, 85)
]
for student in students:
    total = student.maths + student.python + student.sql
    print(student.name, total)'''

## 5,Employee With Highest Salary
Employee = namedtuple("Employee", ["name", "department", "salary"])
employees = [
    Employee("Rahul", "IT", 50000),
    Employee("Priya", "HR", 45000),
    Employee("Arjun", "Finance", 60000),
    Employee("Sneha", "IT", 55000)
]
highest = max(employees, key=lambda employee: employee.salary)
print("Highest Salary:", highest.name)
print("Salary:", highest.salary)
