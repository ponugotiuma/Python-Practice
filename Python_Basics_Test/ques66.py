#Write a Python program to calculate the final subscription amount after converting a monthly price entered as text into a number and applying a discount.
monthly_price = input("Enter monthly subscription price: ")
discount = float(input("Enter discount percentage: "))

monthly_price = float(monthly_price)

discount_amount = monthly_price * discount / 100

final_amount = monthly_price - discount_amount

print("\n--- SUBSCRIPTION ---")
print("Monthly Price:", monthly_price)
print("Discount:", discount_amount)
print("Final Subscription Amount:", final_amount)
