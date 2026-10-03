#Find maximum and minimum in a list without max()/min().
lst=[9,7,5,3,2,4,6,8]
min_val=lst[0]
max_val=lst[0]
for num in lst:
    if num<min_val:
        min_val=num
    if num>max_val:
        max_val=num
print(min_val)
print(max_val)
