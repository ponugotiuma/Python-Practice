#Write a Python program to determine whether a support ticket should be marked urgent using priority and customer plan.
priority = "high"          
customer_plan = "basic"    

is_urgent = False

if priority == "high" or priority == "critical":
    is_urgent = True
elif customer_plan == "enterprise" and priority == "medium":
    is_urgent = True
else:
    is_urgent = False

if is_urgent:
    print("Ticket Status: URGENT")
else:
    print("Ticket Status: Normal")
