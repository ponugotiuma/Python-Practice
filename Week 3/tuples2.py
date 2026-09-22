#tuples OPerations
t = (10, 20, 30, 20, 40)
t[1]
t[1:4]
t + (50,)
t * 2
20 in t
len(t)
t.count(20)
t.index(30) 
t = t[:2] + (99,) + t[3:]
print(t)
