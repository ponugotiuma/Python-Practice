#Write a Python program to generate a customer-facing message containing customer name, product name, quantity, total amount, and payment status.
name = input("Enter customer name: ")
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
total_amount = float(input("Enter total amount: "))
payment_status = input("Enter payment status (Paid/Pending): ")

message = f"""
Hello {name},
Your order for {quantity} x {product} is confirmed.
Total: Rs. {total_amount} - Status: {payment_status}
Thank you for shopping with us!
"""

print(message)
