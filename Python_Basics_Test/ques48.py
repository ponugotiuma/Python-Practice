#Write a Python program to check whether a user qualifies for a product warranty based on purchase amount and warranty status.
purchase_amount=1000
warranty_status=True

if warranty_status and purchase_amount>=1000:
    print("User qualifies for warranty")
else:
    print("User won't qualifies for warranty.Better luck next time")
