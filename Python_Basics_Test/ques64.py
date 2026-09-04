#Write a Python program to parse an order string such as 'Laptop,2,55000' and calculate the order value.
order = "Laptop,2,55000"

parts = order.split(",")

product_name = parts[0]
quantity = int(parts[1])
price = float(parts[2])

order_value = quantity * price

print("Product:", product_name)
print("Quantity:", quantity)
print("Price:", price)
print("Order Value:", order_value)
