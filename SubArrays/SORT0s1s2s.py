# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


nums = [2,0,2,1,1,0]

#the better appraoch to sort the 0s 1s and 2s

count0=0
count1=0
count2=0
for num in nums:
    if num==0:
        count0+=1
    elif num==1:
        count1+=1
    else:
        count2+=1
for i in range(count0):
    nums[i]=0
for i in range(count0,count0+count1):
    nums[i]=1
for i in range(count0+count1,len(nums)):
    nums[i]=2
print(nums)

#the another approach is that the Dutch National Flag Algorithmns:

#RULES:
# 1.0 to low-1--->0   extreme left
# 2.low to mid-1--->1
# 3.high to n-1--> 2   extreme right

nums = [2,0,2,1,1,0]
[0,0,2,1,1,2]
low=0
mid=0
high=len(nums)-1
while mid<=high:
    if nums[mid]==0:
        nums[mid],nums[low]=nums[low],nums[mid]

        low+=1
        mid+=1
    elif nums[mid]==1:
        mid+=1
    else:
        nums[mid],nums[high]=nums[high],nums[mid]
        high-=1

print(nums)

