#Write a Python program to check whether a customer is eligible for a service based on age and a minimum score.
age = 22
score = 750

min_age = 18
min_score = 700

if age >= min_age and score >= min_score:
    print("Customer is eligible for the service.")
else:
    print("Customer is not eligible for the service.")
