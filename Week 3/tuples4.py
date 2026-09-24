# Operations on tuples
## 1,Creating a Tuple
'''t = (10, 20, 30, 40)
print(t)'''

## 2,Accessing Tuple Elements
'''t = (10, 20, 30, 40, 50)
print(t[0])
print(t[2])
print(t[4])
print(t[-1])
print(t[-2])'''

## 3,Slicing a Tuple
'''t = (10, 20, 30, 40, 50)
print(t[1:4])'''

## 4,Tuple Concatenation +
'''a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)'''

## 5,Tuple Repetition '*'.
'''t = (1, 2, 3)
print(t * 3)'''

## 6,Checking Membership
'''t = (10, 20, 30, 40)
print(20 in t)
print(30 not in t)'''

## 7,Finding Length
'''t = (10, 20, 30, 40, 50)
print(len(t))'''

## 8,Finding Maximum and Minimum
'''t = (10, 50, 20, 5, 40)
print(max(t))
print(min(t))'''

## 9,Sum of Tuple
'''t = (10, 20, 30, 40)
print(sum(t))'''

## 10,count()
'''t = (10, 20, 10, 30, 10, 40)
print(t.count(10))'''

## 11,index()
'''t = (10, 20, 30, 40)
print(t.index(30))'''

## 12,Immutability
'''t = (10, 20, 30)
t[0] = 100''' ## Type Error

## 13,Converting List ↔ Tuple
'''numbers = [10, 20, 30]
t = tuple(numbers)
print(t)'''

## 14,Tuple → List
'''t = (10, 20, 30)
numbers = list(t)
print(numbers)'''

## 15,Print only Even Numbers
'''t = (10, 15, 20, 25, 30, 35, 40)
print(t[::2])'''
