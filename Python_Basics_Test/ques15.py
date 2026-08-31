#Write a Python program to calculate profit or loss from cost price and selling price.
cost_price=200
selling_price=190

if selling_price>cost_price:
    profit=selling_price-cost_price
    print(f"The Profit is : {profit}")
else :
    loss=cost_price-selling_price
    print(f"The Loss is : {loss}")
