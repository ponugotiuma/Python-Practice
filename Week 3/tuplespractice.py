#Tuples Practice
##Creating
'''student = ("Rahul", 21, "CSE")
print(student[0])'''

##Tuple Unpacking
'''point = (3, 4)
x, y = point
print(point)
print(x,y)'''

##swap variables:
'''a = 10
b = 20
a, b = b, a
print(a,b)'''

##Problem 1 — Return 3 Values (minimum,maximum,average)
'''def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

lo, hi, avg = stats([4,8,15,16,23,42])
print(lo, hi, avg)'''

##Problem 2 — Unique Coordinates
'''def unique_points(points):
    return len(set(points))
points=unique_points([
    (1,2),
    (3,4),
    (1,2),
    (5,6),
    (3,4)
])
print(points)'''
