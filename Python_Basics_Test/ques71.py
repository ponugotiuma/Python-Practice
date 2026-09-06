#Create a short product identifier
product_name = "Laptop"
product_code = "PRD20257896"

first_three = product_name[:3].upper()
last_four = product_code[-4:]

product_id = first_three + last_four

print("Product Identifier:", product_id)
