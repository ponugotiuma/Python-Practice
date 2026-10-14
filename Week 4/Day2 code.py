#FOR LOOPS
##1,Print each character
'''for ch in "abc":
    print(ch)'''

##2,Loop through a list
'''nums = [10, 20, 30]
for num in nums:
    print(num)'''

##3,enumerate() — get the index too
'''names = ["Ravi", "Sita", "Ram"]
for i, name in enumerate(names, start=1):
    print(i, name)'''

##4,zip() — loop through two lists together
'''names = ["Ravi", "Sita", "Ram"]
marks = [80, 90, 75]
for name, mark in zip(names, marks):
    print(name, mark)'''

#NESTED FOR LOOP
## "*" Pattern
'''for i in range(3):
    for j in range(4):
        print("*", end=" ")
    print()'''

#RANGE() — generating numbers
##1,numbers
'''for i in range(1, 6):
    print(i)'''

##2,Even numbers
'''for i in range(2, 11, 2):
    print(i)'''

##3, Countdown
'''for i in range(5, 0, -1):
    print(i)'''

##4, Reverse a sequence of indices
'''for i in range(4, -1, -1):
    print(i)'''

#FUNCTIONs
##1,Basic - "Hello!"
'''def greet():
    print("Hello!")
greet()'''
##2,Parameters and return values
'''def add(a, b):
    return a + b
result = add(10, 20)
print(result)'''
##3,Default arguments
'''def greet(name, greeting="Hello"):
    print(greeting, name)
greet("Ravi")
greet("Sita", "Welcome")'''
##4,Multiple return values
'''def min_max(nums):
    return min(nums), max(nums)
smallest, largest = min_max([3, 1, 9, 5])
print(smallest)
print(largest)'''

