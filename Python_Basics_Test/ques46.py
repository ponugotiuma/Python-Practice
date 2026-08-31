#Write a Python program to check whether a coupon is valid when the coupon code matches and the order value meets the minimum amount.
coupon_code='17182505'
order_value=799
min_value=699

if coupon_code and order_value>=min_value:
    print("Coupon is valid")
else:
    print("Please try again")
