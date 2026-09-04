#Write a Python program to build a simple product bill calculator using only variables, numbers, strings, casting, and operators.
product_name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\n--- PRODUCT BILL ---")
print("Product:", product_name)
print("Price:", price)
print("Quantity:", quantity)
print("Total Bill:", total)
