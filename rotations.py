def rotations(nums:list[int]):
    n=len(nums)
    min=0
    for i in range(1,n):
        if nums[i]<nums[min]:
            min=i
    return min
            
           
nums=[3,4,5,1,2]
print(rotations(nums))


def rotations(nums: list[int]) -> int:
    min_index = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[min_index]:
            min_index = i
    return min_index
nums=[3,4,5,1,2]
print(rotations(nums))
