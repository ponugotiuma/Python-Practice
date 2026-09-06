#Write a Python program to split a full customer name into first name and last name and create a username from them.
full_name = "John Smith"

name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[1]

username = first_name.lower() + last_name.lower()

print("First Name:", first_name)
print("Last Name:", last_name)
print("Username:", username)
