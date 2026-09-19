#LIST COMPREHENSIONS
## 1, Squares of Evens
'''nums=[1,2,3,4,5,6]
result=[x*x for x in nums if x % 2 == 0]
print(result)'''

##2, Pass/Fail - Ternary at FRONT
'''marks=[35,78,55,90,33]
result=['Pass' if m>=40 else 'Fail' for m in marks]
print(result)'''

##3, Flatten + Even filter
'''data = [[1,2,3],[4,5],[6,7,8,9]]
flat = [v for row in data for v in row]
print(flat)
even_flat=[v for row in data for v in row if v % 2 == 0]
print(even_flat)'''

##4, 3X3 Matrix
'''matrix = [[r+c for c in range(3)] for r in range(0,9,3)]
print(matrix)'''

## 5, Alias Bag
'''a=[10,20,30]
b=a
b.append(40)
print(a)
print(b is a)'''

## 6, Shallow vs Deep
###Shallow
'''import copy
grid=[[1,2],[3,4]]
shallow=grid.copy()
shallow[0][0]=99
print(grid)'''
###Deep
'''deep=copy.deepcopy(grid)
deep[0][0]=100
print(grid)'''
