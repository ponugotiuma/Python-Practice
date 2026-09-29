#LISTS
## append()
'''nums = [1, 2, 3]
nums.append(4)
print(nums)'''

##extend()
'''nums = [1, 2, 3]
nums.extend([4, 5])
print(nums)'''

##insert()
'''nums = [10, 20, 30]
nums.insert(1, 15)
print(nums)'''

##remove(value)
'''nums = [10, 20, 30, 20]
nums.remove(20)
print(nums)'''

##pop(index)
'''nums = [10, 20, 30]
x = nums.pop() ##defaultly deletes the last indexed element in the list. If index given , corresponding element pops up.
print(x)
print(nums)'''

##del
'''nums = [10, 20, 30]
del nums[1] ##based on index deletes elements.
print(nums)'''

##List Slicing
'''nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[:3])
print(nums[3:])
print(nums[2:5])
print(nums[::2])
print(nums[::-1])'''

##Problem 1 — Move Zeros to End
'''def move_zeros(nums):
    pos = 0
    for x in nums:
        if x != 0:
            nums[pos] = x
            pos += 1
    while pos < len(nums):
        nums[pos] = 0
        pos += 1
    return nums
print(move_zeros([0,1,0,3,12]))'''

##Problem 2 — Second Largest
'''def second_largest(nums):
    first = second = float('-inf')
    for x in nums:
        if x > first:
            second = first
            first = x

        elif first > x > second:
            second = x
    return None if second == float('-inf') else second
print(second_largest([10, 5, 10, 8, 3]))'''

##Problem 3 — Rotate List
'''def rotate(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums
print(rotate([1,2,3,4,5],2))'''

