#Write a Python program to split a comma-separated list of product names into separate values.
product_list='FaceWash,Serum,FaceCream'
my_list=product_list.split(',')
for item in my_list:
    print(item.strip())

