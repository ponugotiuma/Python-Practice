#Remove duplicates from a list.
lst=[1,2,3,4,1,2,3,1,5]
lst1=[]
for item in lst:
    if item not in lst1:
        lst1.append(item)
print(lst1)
