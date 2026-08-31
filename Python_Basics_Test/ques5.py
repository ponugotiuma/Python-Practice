#Write a Python program to read a product name, price, and quantity from the user and display them.
pro_name=input("Enter product name:")
price=float(input("Enter price:"))
quantity=int(input("Enter Quantity:"))

print("Product\tPrice\tQuantity")
print(f"{pro_name}\t{price}\t{quantity}")
