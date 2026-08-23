#Python Functions Practice Problems
#Problem 1 — Student Result Calculator -- Concepts: Parameters, return value, arithmetic operations
##Write a function calculate_total() that accepts 3 subject marks as parameters and returns: • Total marks • Average marks • Grade
"""python= int(input("Enter Python Marks:"))
sql=int(input("Enter SQL Marks:"))
dsa=int(input("Enter DSA Marks:"))
total=python+sql+dsa
avg = total/3 

def calculate_total(python,sql,dsa):
    if avg >= 90 :
            print("Grade:A")
    elif avg>= 75:
            print("Grade:B")
    elif avg>= 60:
            print("Grade:C")
    elif avg>=50:
            print("Grade:D")
    else :
            print("Grade:F")
       
print("Total Marks:", total)
print("Average Marks:", avg)
calculate_total(python,sql,dsa)"""

#Problem 2 — Simple Calculator -- Concepts: Multiple parameters, return value, conditional statements
##Create a function calculator() that accepts: 1. First number 2. Second number 3. Operator
"""num1=int(input("Enter 1st Num:"))
num2=int(input("Enter 2nd Num:"))
operator=input("Enter Operator:")

def calculator(num1, num2, operator):
    if operator == "+":
        print("Result:", num1+num2)
    elif operator == "-":
        print("Result:", num1-num2)
    elif operator == "*":
        print("Result:", num1*num2)
    elif operator == "/":
        print("Result:", num1/num2)
    else :
        print("Enter a valid operator")

calculator(num1,num2,operator)"""

#Problem 3 — Employee Salary Calculator -- Concepts: Default parameters, keyword arguments, return value
##Write a function calculate_salary() that accepts: • basic_salary • bonus • tax_rate

"""def calculate_salary(basic_salary, bonus=5000, tax_rate=10):
    Gross_Salary = basic_salary + bonus
    Tax = Gross_Salary * tax_rate / 100
    Net_Salary = Gross_Salary - Tax
    return Gross_Salary,Tax,Net_Salary

#Gross_Salary,Tax,Net_Salary=calculate_salary(30000)
#Gross_Salary,Tax,Net_Salary=calculate_salary(30000, 7000)
#Gross_Salary,Tax,Net_Salary=calculate_salary(30000, tax_rate=15)

print("Net Salary :" Net_Salary)"""

#Problem 4 — Find the Largest Number -- Concepts: *args, loops, return value
##Create a function find_largest() that accepts any number of numbers using *args.
###The function should return the largest number. 
"""def find_largest(*numbers):
    largest=numbers[0]
    for num in numbers:
        if num>largest:
            largest=num
    return largest

result = find_largest(10, 25, 7, 45, 18)
print(result)"""

#Problem 5 — Student Performance Analyzer -- Concepts: Multiple functions, parameters, return values, *args, function calling another function
##Create a small Student Performance Analyzer.

"""def calculate_average(*marks):
    if len(marks)==0:
        return 0
    return sum(marks)/len(marks)
    
def find_grade(average):
    if average>=90:
        return "A"
    elif average>=75:
        return "B"
    elif average>=60:
        return "C"
    elif average>=50:
        return "D"
    else :
        return "F"
    
def display_result(name, *marks):
    avg=calculate_average(*marks)
    grade=find_grade(avg)
    print("Name:", name)
    print("Marks:", marks)
    print("Average:", avg)
    print("Grade:", grade)
    
display_result("Uma", 85, 78, 92, 88)"""
