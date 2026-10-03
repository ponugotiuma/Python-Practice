# Find the sum of digits of a number.
num=123456789
add=0
while num>0:
    digit=num%10
    add=add+digit
    num=num//10
print(add)
