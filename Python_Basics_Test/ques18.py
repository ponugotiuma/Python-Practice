#Write a Python program that accepts a string price such as '1499.50', converts it to a float, and calculates a 10% discount.
price=float('1499.50')
discount=10
dis_apply=price*discount/100
final_price=price-dis_apply

print(f"The discount is {dis_apply}")
print(f"The final Price is {final_price}")
