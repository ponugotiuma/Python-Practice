#Write a Python program to compare two service plans by price and display which one is cheaper.
plan1 = "Basic"
price1 = 499

plan2 = "Premium"
price2 = 699

if price1 < price2:
    print(plan1, "is cheaper.")
elif price2 < price1:
    print(plan2, "is cheaper.")
else:
    print("Both plans have the same price.")
