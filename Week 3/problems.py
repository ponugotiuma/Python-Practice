#Problem 1 - Write a Python program to calculate the total of all numerical values stored in a dictionary.
'''dict1={"a":10,"b":20}
total = sum(dict1.values())
print("Total:", total)'''

#Problem 2 - Write a Python program to count how many times each character appears in a given string, storing the results in a dictionary.
'''name = "Uma Ponugoti"
char_count = {}
for char in name:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)'''

#Key of Minimum Value - Problem Statement: Write a Python program to find the key associated with the smallest numerical value in a dictionary.
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
min_item = min(stock, key=stock.get)
print("item:", min_item)

