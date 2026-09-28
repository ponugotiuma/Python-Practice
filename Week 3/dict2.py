#CRUD Operations on Dictionaries
## Read — bracket vs get
'''d = {"name": "Asha", "score": 92}
print(d["name"]) 
#d["age"] --> raises error 
#d.get("age") --> returns none'''

## Create / Update
'''d = {"a": 1}
d["b"] = 2 # add a new key
d["a"] = 99 # overwrite existing key
d.update({"c": 3, "a": 100})
print(d)'''

## Delete
'''d = {"a": 1, "b": 2, "c": 3}
del d["a"] # remove key 'a' (KeyError if absent)
v = d.pop("b") # remove & RETURN value (2); pop("z", None) for safe
k, v = d.popitem() # remove & return the LAST inserted pair (LIFO)
d.clear()
print(d)'''
