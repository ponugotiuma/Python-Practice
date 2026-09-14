#CRUD Operations
##1,Create Elements
lst=[10,20,30]
lst.append(40) #to add an item(append)
lst.insert(1,15) #insert(index_num, element_to_add)
lst.extend([50,60]) #to add manny items at the end(extend)
lst+=[70] #similar to extend
#print(lst)

##2,Read Elements
lst1=['a','b','c','d','e']
print(lst1[0]) #reads the 0th index element
print(lst1[-1]) #reads the -1th element i.e, last element of list
print(lst1.index('c'))
print(lst1.count('a'))
print(lst1)
