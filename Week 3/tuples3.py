# Baisc Tuple Problems
## 1, Create a Tuple : Create a tuple containing 5 numbers and print the tuple.
'''tup1=(2,4,6,8,10,12)
print(type(tup1))
print(tup1)'''

## 2,Different Data Types : Create a tuple containing an integer, float, string, and Boolean value. Print the tuple.
'''tup2=(15,15.5,"Uma",True)
print(tup2)'''

## 3,Access Elements : Print the first and last elements of the tuple.
'''fruits = ("apple", "banana", "mango", "orange")
print(fruits[::3])'''

## 4,Indexing : Print the element at index 2 and index -2 from the tuple.
'''numbers = (10, 20, 30, 40, 50)
print(numbers[2], numbers[-2])'''

## 5,Slicing : Print , First 3 elements,Last 3 elements,Elements from index 2 to 4.
'''numbers = (10, 20, 30, 40, 50, 60)
print(numbers[:3])
print(numbers[3:])
print(numbers[2:5])'''

## 6,Length of Tuple: Create a tuple of 7 student names and find its length using len().
'''students=("Uma","Vyshnavi","Akshara","Srujana","Swarupa","Suguna","June")
print(len(students))'''

## 7,Check Membership : Check whether "SQL" and "Java" are present in the tuple.
'''subjects = ("Python", "SQL", "Excel", "Power BI")
print("SQL" in subjects)
print("Java" in subjects)'''

## 8,Count an Element : Find how many times 10 occurs.
'''numbers = (10, 20, 10, 30, 10, 40)
result = numbers.count(10)
print(result)'''

## 9,Find Index : Find the index position of "Mumbai".
'''cities = ("Hyderabad", "Delhi", "Mumbai", "Chennai")
print(cities.index("Mumbai"))'''

## 10,Tuple Concatenation : Combine both tuples into a single tuple and print the result.
'''t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)'''

#Tuple Packing & Unpacking
## 11,Tuple Packing : Pack the following values into a single tuple, Print the resulting tuple.
'''name = "Rahul"
age = 21
city = "Hyderabad"
student = name, age, city
print(student)'''

## 12,Basic Unpacking : Unpack the tuple into three variables, name,age,branch.Then print each variable separately.
'''student = ("Rahul", 21, "CSE")
print(student[0])
print(student[1])
print(student[2])'''

## 13,Unpacking with Multiple Values : Unpack all five values into five separate variables and print them.
'''numbers = (10, 20, 30, 40, 50)
num1=numbers[0]
num2=numbers[1]
num3=numbers[2]
num4=numbers[3]
num5=numbers[4]
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)'''
