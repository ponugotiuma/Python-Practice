#Write a Python program that checks whether a service booking is valid based on available slots and customer payment status.
available_slots=3
cus_pay_status=True

if available_slots>0 and cus_pay_status:
    print("The Service booking is valid.")
elif available_slots==0:
    print('The slots are empty . Please visit again')
else:
    print("Please check your payment status.")
