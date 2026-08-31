#Write a Python program that checks whether a product is eligible for a return using purchase days and return policy status.
purchase_days=10
return_policy=True

if return_policy and purchase_days<=7:
    print("Return of product is Eligible")
else:
    print("Cannot be returned")
