def chandu(nums):
    mid=0
    low=0
    high=len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums


    



nums=[0,0,1,1,2,2,2,2,1,0]
print(chandu(nums))


#this is the dutch national flag algorithmns

# in addition to this we can use the count of ones,countof zeros and count og the twos


# the kadane algorithmn:

def kadane(nums):
    sum1=0
    min1=float("-inf")
    for i in range(len(nums)):
        sum1+=nums[i]
        if sum1>min1:
            min1=sum1
            
        if sum1<0:
            sum1=0
    return min1



nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane(nums))

dici={}
for i in range(1,10):
    dici[str(i)+"#"]=i
print(dici)

s= "10#11#12"
res=""
s1=s.split("#")
print(s1)
