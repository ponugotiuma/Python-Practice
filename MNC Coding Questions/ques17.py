#Find common elements between two lists.
lst1=[1,2,3,4]
lst2=[2,1,3,4,5]
common=[]
for item in lst1:
    if item in lst2:
        common.append(item)
print(common)
