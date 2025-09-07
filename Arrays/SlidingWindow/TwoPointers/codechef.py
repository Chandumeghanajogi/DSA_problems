# # n,b=4,5
# # nums=[2, 3, 5, 10, 50, 80]
# # l=0
# # r=len(nums)-1
# # flag=False
# # nums.sort()   
# # print(nums)
# # while l<=r:
# #     if abs(nums[l]-nums[r])==b:
# #         flag=True
# #     else:
# #         r-=1
# #     l+=1
# # if flag:
# #     print(1)
# # else:
# #     print(0)

# # 1
# # 7 2
# # 
# nums=[2, 4, 8, 1, 2, 1, 8]

# l=0
# sum1=0
# k=2
# max1=float("-inf")
# for r in range(len(nums)):
#     sum1+=nums[r]
#     if r-l==k:
#         sum1-=nums[l]
#         l+=1
#     if r-l+1==k:
#         max1=max(max1,sum1)
# print(max1)

# # Input: nums = [2,3,-2,4]
# # Output: 6
# # Explanation: [2,3] has the largest product 6.
# # Example 2:

# # Input: nums = [-2,0,-1]
# # Output: 0
# # Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
nums = [0,2]
l=0
pro=1
max1=float("-inf")
for r in range(len(nums)):
    pro*=nums[r]
    if pro<=0:
        
        l+=1
    if pro>max1:
        max1=max(pro,max1)
        print(max1)
print(max1)
    
