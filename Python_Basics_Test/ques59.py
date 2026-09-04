#Write a Python program to create a URL-friendly product slug from a product name.
import re

product_name = input("Enter product name: ")

slug = product_name.lower()
slug = re.sub(r'[^a-z0-9\s-]', '', slug)
slug = re.sub(r'\s+', '-', slug)
slug = re.sub(r'-+', '-', slug)
slug = slug.strip('-')
print("Product Slug:", slug)
