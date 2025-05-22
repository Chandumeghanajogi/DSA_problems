def linear(nums,element):
    for i in range(len(nums)):
        if element==nums[i]:
            return i
    
nums=[10,20,22,4,6]
print(linear(nums,4))

    