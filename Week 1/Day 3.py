# DATATYPES & TYPE CONVERSIONS
#Create a list of three fruits and print the first
'''fruits=["mango","alphanzo","passion fruit"]
print(fruits[0])
print(type(fruits))'''

#Create a tuple of coordinates and show it can't be changed
'''coordinates=(10.5,12.7)
print(coordinates[0])
coordinates[0]=11.5
print(type(coordinates))'''

#Create a set with a duplicate and show it's removed
'''fruits1={"Yellow","Green","Yellow","Brown"}
print(fruits) #output : Brown,Green,Yellow(no duplication)
print(type(fruits1))'''

#Create a dict of name and age and look up by key
'''details={"name":"Uma", "age":"20"}
print(details['name'],details['age'])#output : Uma 20
print(type(details))'''

#Use type() to compare a value's type to int
'''x=5
print(type(x)==int)'''

#Use isinstance() to test an int against int and str
'''x=7
print(isinstance(x,int))
print(isinstance(x,str))'''

#Use isinstance() with a tuple of types (int, float)
'''my_tuple=(10,10.5,11,12.7)
print(isinstance(my_tuple, tuple))''' #output: int->False , float->False, tuple->True

#Add a new key-value pair to an existing dict
'''details={"name":"Uma", "age":"20"}
details['city']='Kodad'
print(details)'''

#Convert the string '42' to an int
'''num=int("42")
print(type(num))'''

#Convert '3.14' to a float
'''pi=float('3.14')
print(type(pi))'''

#Convert the number 100 to a string
'''num=str('100')
print(type(num))'''

#Convert 7 to a float
'''x=float('7')
print(type(x), x)'''

#Convert 'abc' to a list of characters
'''co_list=list('abc')
print(co_list)'''

#Convert a list to a tuple and to a set
'''li_tup=tuple('abc')
li_set=set('abc')
print(li_tup,"\n", li_set)'''

#Fix '5' + 3 to produce the number 8
'''x=int('5')+3
print(x)''' #output : 8

#Build an age-in-months calculator reading input
'''age=int(input("Enter age:"))
age*=12
print("The months are:", age)''' #output : age=20 , months=240

#PRACTICE PROBLEMS
#Print your name, course, and year on three lines using one print with \n
'''name,course,year="Uma","B.Tech","2023-27"
print(f"{name}\n{course}\n{year}")'''

#Swap two variables and print before/after
'''x,y=5,7
print("before swap:", x,y)
x,y=y,x
print("after swap:", x,y)'''

#Convert '2024' to int, add 1, print as a string message
'''year=int('2024')
print("Next year will be:", year+1)'''

#Check if 48 is even and if 'a' is in 'apple'
'''x=48
fruit="apple"
if x%2==0:
    print(x, "is even!")
print("a" in fruit)'''

#Print pi to 3 decimal places
'''pi=3.1415926535
print(f"{pi:.3f}")'''

#Read a number with input(), double it, and print
'''x=int(input("Enter a num:"))*2
print(x)'''

#Uppercase a name, then show the original is unchanged
'''name="uma"
print(name.upper()) #o/p : UMA
print(name)''' #o/p : uma

#Convert the list [1,1,2,3,3] to a set, then to a sorted list
'''my_list=set('11233')
print(my_list)''' # {'1', '2', '3'}
'''sorted(my_list)
print(my_list)''' # {'1', '2', '3'}

#Predict the type of 10 / 2, then convert to int
'''x=10/2
print(type(x))
x=int(10/2)
print(type(x))'''

#Slice 'Programming' to get 'gram'
'''lang="Programming"
slicer=lang[3:7]
print(lang) #o/p : Programming
print(slicer)''' # o/p: gram

#Print a receipt line: item, qty, price with aligned tabs
'''item="Soap"
qty=1
price=79
print("Item \t qty \t Price")
print(f"{item}\t{qty}\t{price}")'''

#Build a dict of 3 capitals and look one up
'''capitals={"Telangana":"Hyd", "Andhra":"Amaravati","Tamilnadu":"Chennai"}
print(capitals['Telangana'])'''

#Round 2.675 to 2 decimals
'''x=round((2.675), 2)
print(x)'''

#Show True + True + False equals 2
'''print(True+True+False)'''

#Convert 3.99 to int and round(3.99)
'''val=int(round((3.99)))
print(val)'''

#Compute a 15% tip on a bill read from input
'''amount=float(input("Enter amount:"))
tip= amount*0.15
print("The Tip is :", tip)
print("Your Total Bill is:", amount+tip)'''

#Write a mini profile: name, age, city, student(bool) via f-string
'''name,age,city,student="Uma",20,"Kodad",True
print(f"{name} is {age} years old from {city} and is a Student ({student}).")'''
