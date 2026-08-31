#Write a Python program to calculate the final bill amount after applying a percentage discount to a product price.
product_price=150.99
discount=15
dis_apply=product_price*discount/100
final_price=product_price-dis_apply

print(f"The final Bill of the product is: {final_price}")
