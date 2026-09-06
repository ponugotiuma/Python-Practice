#Generate a formatted receipt for three products
product1 = "Laptop"
price1 = 50000

product2 = "Mouse"
price2 = 800

product3 = "Keyboard"
price3 = 1500

total = price1 + price2 + price3

print("========== RECEIPT ==========")
print(f"{product1:<15} ${price1:>8.2f}")
print(f"{product2:<15} ${price2:>8.2f}")
print(f"{product3:<15} ${price3:>8.2f}")
print("-----------------------------")
print(f"{'Total':<15} ${total:>8.2f}")
print("=============================")
