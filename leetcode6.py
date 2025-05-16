# Input: nums = [2,5,1,3,4,7], n = 3  
# Output: [2,3,5,4,1,7]

# # Explanation: 
# # x = [2,5,1], y = [3,4,7]
# # Interleave them: [2,3,5,4,1,7]

def array(nums,n):
    a=nums[:n]
    b=nums[n:]
    new=[]
    for i in range(n):
        new.append(a[i])
        new.append(b[i])
    return new
            

nums=[2,5,1,3,4,7]
n=3
print(array(nums,n))
