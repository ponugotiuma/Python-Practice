#LIST METHODS
##1, The None Bug
'''nums=[3,1,2]
nums=nums.sort(nums) #sorts but doesn't print new list
#for new list --> nums = sorted(nums)
print(nums)''' 

##2, Complexity of list
'''lst=[1,2,3,4,5]
for i in range(5):
    lst.insert(0, i) #inserts the 4 elements at the 0th index
print(lst)'''

## 3, append() vs extend()
'''a=[1,2]
a.append([3,4]) #prints with []
print(a)
b=[1,2]
b.extend([3,4]) #just adds the numbers
print(b)'''

## 4, pop() trick
'''lst=list(range(1000))
lst.pop() #by default pops the last element in list
lst.pop(0) #pops the 0th index element
print(lst)'''

## 5,remove() vs pop() vs del()
'''lst=[1,2,3,2,4]
lst.remove(2) #removes the 1st occurance of the given element
lst.pop(2) #pops up by given index
del lst[0] #deletes by index with keyword 'del'
print(lst)'''

## 6,sort by 2nd element , but stable
'''details=[("Asha",30),("Ravi",25),("Asha",22)]
details.sort(key=lambda t: t[0])
print(details)'''

