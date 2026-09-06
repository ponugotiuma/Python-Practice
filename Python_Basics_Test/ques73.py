#Validate an order before payment
stock = 10
budget = 5000
customer_status = "Inactive"
payment_amount = 2500

if stock > 0 and budget >= payment_amount and customer_status == "active" and payment_amount > 0:
    print("Order is valid. Payment can be processed.")
else:
    print("Order cannot be processed.")
    
