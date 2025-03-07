def array(nums,k):
    k%=n
    n=len(nums)
    temp=[0]*n
    temp1=nums[:]
    for i in range(k):
        temp[i]=nums[n-k+i]
    for i in range(n-k):
        temp[k+i]=temp1[i]
    for i in range(n):
        nums[i]=temp[i]
    return nums




nums=[1,2,3,4,5,6,7]
k=2
print(array(nums,k))
# print(a)