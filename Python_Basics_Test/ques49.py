#Write a Python program to determine whether a service request can be accepted when the customer is active and payment is completed.
customer_active=False
payment_status=True

if customer_active and payment_status:
    print("Service request can be accepted")
else:
    print("Service cannot be accepted, cause of customer/payment status is pending...")
