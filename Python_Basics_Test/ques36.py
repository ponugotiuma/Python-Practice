#Write a Python program to format a customer invoice using an f-string with customer name, product, quantity, and total.
cus_name='Uma'
product='Battery'
quantity=1
total=1399.99

print(f"Customer Name\tProduct\tQuantity\tTotal")
print(f"{cus_name}\t\t{product}\t{quantity}\t{total}")
