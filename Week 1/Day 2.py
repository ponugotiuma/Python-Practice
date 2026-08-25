#AUGMENTED ASSIGNMENT OPERATORS
#Start at 0 and use += to reach 10 in two steps
'''x=0
x+=6
x+=4
print(x)'''

#Use -= to subtract from a score
'''x-=5
print(x)'''

#Double a value with *=
'''x=2
x*=2
print(x)'''

#Build a string 'Python' using += from 'Py'
'''x="Py"
x+="thon"
print(x)'''

#Predict:
'''x=10;
x//=3;
print(x)'''
#Predict:
'''x=10;
x%=4;
print(x)'''
#Predict:
'''x=2;
x**=4;
print(x)'''

#Create variables for your name, age, height, and student status
'''name="Uma"
age=20
height=5.4
student_status=True'''

#Assign 1, 2, 3 to x, y, z in one line
'''x,y,z=1,2,3
print(x,y,z)'''

#Assign the value 0 to three variables in one line
'''a=b=c=0
print(a,b,c)'''

#Swap three variables in a cycle (a->b->c->a)
'''a=5
b=6
c=7
a,b,c=c,a,b
print(a,b,c)'''

#Print 'Age: 25' by concatenating with str()
'''name="Uma"
age=20
print(f"{name} " + "is" +  " " + str(age)  + "years old")'''

#Create an int, a float, and a complex number; print each type
'''x=3
y=10.5
z=2+4j
print(type(x))
print(type(y))
print(type(z))'''

#Check if a number is even using %
'''num=4
if num%2==0:
    print("even: ", num)'''

#Concatenate and repeat strings
'''name="Uma"
city="Kodad"
print("Uma"+ " " +"from"+" "+"Kodad")
print(name*3)'''

#Split 'a,b,c' on commas
'''print("a,b,c".split(","))'''

#Predict
'''print(bool(0))
print(bool('hi'))
print(bool([]))
print(bool(None))'''

#Count Trues in a list using sum()
'''my_list=[True,False,True,False]
count=sum(my_list)
print(count)'''
