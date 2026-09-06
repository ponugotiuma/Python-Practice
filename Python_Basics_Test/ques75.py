#Normalize customer input and compare with category
stored_category = "electronics"

customer_input = "  ELECTRONICS  "

normalized_input = customer_input.strip().lower()

if normalized_input == stored_category:
    print("Category matched.")
else:
    print("Category does not match.")
