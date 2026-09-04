#Write a Python program to determine whether a user qualifies for a premium plan using multiple conditions with and/or.
age = 25
monthly_spend = 150.0
has_referral_code = True
account_age_months = 8

if age >= 18 and (monthly_spend > 100 or has_referral_code) and account_age_months >= 6:
    print("User qualifies for the premium plan.")
else:
    print("User does not qualify for the premium plan.")
