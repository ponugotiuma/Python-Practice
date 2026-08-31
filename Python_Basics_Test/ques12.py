#Write a Python program to calculate GST for a service fee and display the final amount.
service_fee=1000
GST=15
gst_apply=service_fee*GST/100
final_amount=service_fee+gst_apply

print(f"The GST amount applied : {gst_apply}")
print(f"The Final Amount is : {final_amount}")
