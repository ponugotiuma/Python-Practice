#Write a Python program to validate a service registration using username, email, and password conditions.
username=input("enter the username:")
email=input("enter the email:")
password=input("enter the password:")

'''Username Validation'''
if len(username)==0:
    print("Username Error : Cannot be empty")
elif len(username)<4 and len(username)>20:
    print("Username must be 4-20 characters")
else:
    print("Invalid Username")
