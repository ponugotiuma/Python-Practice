#CRUD Operations
##Update/modify operation
lst=[1,2,3,4,5]
lst[0]=99 #replacing the element by index
lst[1:3]=[20,30,40] #slicing the elements by index
print(lst)


##Delete Operation
lst1=[10,20,30,20,40]
lst1.remove(20)
x=lst1.pop()
y=lst1.pop(0)
del lst1[0]
lst1.clear()
print(lst1)
print(x)
print(y)
