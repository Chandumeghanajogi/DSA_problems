# The Time Complexity of this Algorithmn is O(n**3)
# because using the three loops and those Iteration......



class Solution:
    def threeSum(self, nums):
        set1=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        
                        a=[nums[i],nums[j],nums[k]]
                        a.sort()
                        set1.add(tuple(a))

        return list(set1)
    
nums = [-1,0,1,2,-1,-4]
obj=Solution()
print(obj.threeSum(nums))

# trying out the optimal Solution

# --->sort the array
# --->check the i to avoid the duplicate start of the i
# --->Later start j and k initialization
# --->if nums = [-1,0,1,2,-1,-4]  if the sum<0 then incre the j Value
# ---> if sum>0  then incre the k value
# --> finally check the dupliactes
def threesumop(nums):
    a=[]
    nums.sort()
    n=len(nums)
    for i in range(n):
        if i!=0 and nums[i]==nums[i-1]:
            continue
        j=i+1
        k=n-1
        while j<k:
            temp=nums[i]+nums[j]+nums[k]
            if temp<0:
                j+=1
            elif temp>0:
                k-=1
            else:
                ans=[nums[i],nums[j],nums[k]]
                a.append(ans)
                j+=1
                k-=1
                while j<k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k]==nums[k-1]:
                    k-=1
    return a

nums=[-1,0,1,2,-1,-4]
print(threesumop(nums))
    