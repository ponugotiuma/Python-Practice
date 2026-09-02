#Write a Python program that checks whether a user is eligible for a free trial based on account status and previous trial usage.
account_status = "active"   
previous_trial_used = False 

if account_status == "active" and previous_trial_used == False:
    is_eligible = True
else:
    is_eligible = False

if is_eligible:
    print("User is ELIGIBLE for a free trial.")
else:
    print("User is NOT eligible for a free trial.")
