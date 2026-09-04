#Write a Python program to create a service quotation that accepts customer name, service name, hours, hourly rate, discount, and tax, then prints the final quotation.
customer_name = input("Enter customer name: ")
service_name = input("Enter service name: ")
hours = float(input("Enter number of hours: "))
hourly_rate = float(input("Enter hourly rate: "))
discount = float(input("Enter discount percentage: "))
tax = float(input("Enter tax percentage: "))

subtotal = hours * hourly_rate

discount_amount = subtotal * discount / 100
after_discount = subtotal - discount_amount

tax_amount = after_discount * tax / 100

final_amount = after_discount + tax_amount

print("\n--- SERVICE QUOTATION ---")
print("Customer Name:", customer_name)
print("Service:", service_name)
print("Hours:", hours)
print("Hourly Rate:", hourly_rate)
print("Subtotal:", subtotal)
print("Discount:", discount_amount)
print("Tax:", tax_amount)
print("Final Amount:", final_amount)
