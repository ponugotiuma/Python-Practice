#SETS
##Creation
'''numbers = [1,2,2,3,3,3,4]
print(set(numbers))'''

##METHODS
#s = {1,2,3}
###Adding elements
'''s.add(4)
print(s)'''
###Adding Multiple elements 
'''s.update([5,6])
print(s)'''
###Remove
'''s.remove(6)
print(s)'''
###Safer remove
'''s.discard(100)
print(s)'''

##OPERATIONS
A = {1,2,3,4}
B = {3,4,5,6}
###Union (|)
'''print(A | B)'''
###Intersection (&)
'''print(A & B)'''
###Difference(-)
'''print(A-B)'''
###Symmetric Difference (^)
'''print(A ^ B)'''

##Problem 1 — Remove Duplicates but Keep Order
'''def dedup_ordered(nums):
    seen = set()
    out = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
nums=dedup_ordered([3,1,3,2,1,4])
print(nums)'''

##Problem 2 — Intersection and Union
'''def intersect_union(a, b):
    sa = set(a)
    sb = set(b)
    return sorted(sa & sb), sorted(sa | sb)
a = [1,2,2,3]
b = [2,3,4]
print(a,b)'''

##Problem 3 — Detect Duplicate
'''def first_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return x
        seen.add(x)
    return None
nums=first_duplicate([1,2,3,4,2])
print(nums)'''
