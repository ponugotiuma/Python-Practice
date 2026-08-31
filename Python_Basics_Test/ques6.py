#Write a Python program that calculates the total price of a product using price and quantity entered by the user.
product=input("Enter product:")
price=float(input("Enter price:"))
quantity=float(input("Enter quantity:"))
total_price=round(quantity*price,2)

print(f"The Total Price of the '{product}' is {total_price}")
