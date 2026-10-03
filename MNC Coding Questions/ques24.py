# Find the second-largest number.
nums=[10,5,20,8,15]
nums=list(set(nums))
nums.sort()
if len(nums)>=2:
    print(nums[-2])
else :
    print("No second largest")
