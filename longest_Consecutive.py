#  Time Complexity = O(n)
# Because:

# You loop over the array once.

# You only build each sequence once (thanks to i - 1 not in s).

# And all your lookups (x + 1 in s) are in O(1) time due to the set.

# So even though there's a nested while loop, it doesn't run for every element — only once for each distinct sequence.


# def hello(nums,target):
#     dici={}
#     for i in range(len(nums)):
#         if nums[i] in dici:
#             return [dici[nums[i]],i]
#         else:
#             dici[target-nums[i]]=i

# nums = [2,7,11,15]
# target = 9
# print(hello(nums,target))


# def hello(nums,target):
#     nums.sort()
#     l=0
#     r=len(nums)-1
#     a=[]
#     print(nums)
#     while l<=r:
#         if nums[l]+nums[r]==target:
#             a.append([l,r])
#             l+=1
#             r-=1
#         elif nums[l]+nums[r]>target:
#             r-=1
#         else:
#             l+=1
#     return a
        
# nums = [2,7,11,15,1,8]
# target = 9
# print(hello(nums,target))


nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print([i,j])
        else:
            continue









