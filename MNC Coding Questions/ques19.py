#Reverse a list without reverse().
lst=[10,20,30,40]
rev=[]
i=len(lst)-1
while i>=0:
    rev.append(lst[i])
    i=i-1
print(rev)
