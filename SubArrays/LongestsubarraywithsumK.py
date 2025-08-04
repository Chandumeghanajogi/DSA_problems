# nums = [10, 5, 2, 7, 1, 9]
# k=15

# l=0 
# n=len(nums)
# sum1=0
# temp=[]
# max_len=0
# for r in range(n): 
#     sum1+=nums[r]

#     if sum1>15:
#         sum1-=nums[l]
#         l+=1
#     max_len=max(max_len,r-l+1)
#     print(nums[l:r+1])
# print(max_len)
    


# # dry run:
# # l=1
# # r=2
# # sum1=10+5=15   15+2==17
# # temp=[5,15          ]
# # 10>15  False
# maxlen=3

def longestSubarray(nums, k):
    l=0
    sum1=0
    count=0
    for r in range(len(nums)):
        sum1+=nums[r]
        if sum1>k:
            sum1-=nums[l]
            l+=1
        count=max(count,r-l+1)
        if count==0:
            return 0
    return count

nums=[-3, 2, 1]
k=6
print(longestSubarray(nums,k))


#retyurn the longest subarrays with atmost k odd numbers;

def subarray(nums):
    l=0
    temp=0
    max1=float("-inf")
    for r in range(len(nums)):
        if nums[r]%2==1:
            temp+=1
        while temp>2:
            if nums[l]%2==1:
                temp-=1
            l+=1
        max1=max(max1,r-l+1)
    return max1
        



nums=[1,3,4,5,7]
print(subarray(nums))


# def mini(nums,target):
    



# nums = [2,3,1,2,4,3]
target = 7
    
rupees=70
discount=10
total=10*70//100
final=rupees-total
print(final)


s=["flower","flow","flight"]
start=s[0]
startlen=len(s)
for i in s[1:]:
    while start!=i[0:startlen]:
        startlen-=1
        

    start=i
print(i)