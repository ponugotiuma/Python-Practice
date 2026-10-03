#Find common keys between dictionaries.
dict1={101:"CSE",102:"ECE"}
dict2={102:"ECE"}
dict3={}
for keys in dict1:
    if keys in dict2:
        dict3[keys]=dict1[keys]
print(dict3)
        
