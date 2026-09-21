#TUPLES
##1, Comma trap of tuples Creation
'''a=(5)
b=(5,)
c=5,
print(type(a),type(b),type(c))
print(len(b))'''

##2,Immutable Nature, append 3 to the inner list!
'''t=([1,2],3)
t[0].append(3)
print(t)'''

##3,Hashable Test
'''k1=(1,2,3)
k2=(1,[2,3])
k3=([1,2],3)
k4=((1,2),3)
print(type(k1),type(k2),type(k3),type(k4))''' #all are tuples

## 4, swapping for tuples
'''a=(1,2,3)
b=(4,5,6)
a,b=b,a
print("a:",a)
print("b:",b)'''

## 5,Star Unpacking
'''first , *middle, last=[1,2,3,4,5,6]
print(first, middle ,last)

x,*y=[1]
print(x,y)

a, *b,c="abc"
print(a,b,c)'''

##6, ignore with_
'''data =[("Asha",95,"A"),("Ravi",88,"B")]
for name,score,_ in data:
    print(f"{name}:{score}")'''

