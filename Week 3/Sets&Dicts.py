#SETS
##Find Common Elements
numbers1 = [10, 20, 30, 40, 50]
numbers2 = [30, 40, 50, 60, 70]

set1 = set(numbers1)
set2 = set(numbers2)

common = set1 & set2
print(common)

#DICTIONARIES
##Count Frequencies
numbers = [2, 3, 2, 5, 3, 2, 7, 5]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
