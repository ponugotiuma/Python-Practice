#Write a Python program to compare two product names after converting them to lowercase and removing extra spaces.
product1 = input("Enter first product name: ")
product2 = input("Enter second product name: ")

product1 = " ".join(product1.lower().split())
product2 = " ".join(product2.lower().split())

if product1 == product2:
    print("The product names are the same.")
else:
    print("The product names are different.")
