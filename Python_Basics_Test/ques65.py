#Write a Python program to validate a product code with a required prefix, length, and numeric suffix.
code = input("Enter product code: ")

prefix = "PROD"

if len(code) == 8 and code.startswith(prefix) and code[4:].isdigit():
    print("Valid product code.")
else:
    print("Invalid product code.")
