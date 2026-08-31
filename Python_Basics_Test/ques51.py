#Write a Python program to create Boolean variables for payment_success, stock_available, and address_valid, then calculate whether an order can be placed.
payment_success=False
stock_available=True
address_valid=True

if payment_success and stock_available and address_valid:
    print("The order can be Placed")
else:
    print("The order cannot be placed\nInvalid payment/stock/address details. Try Again")
