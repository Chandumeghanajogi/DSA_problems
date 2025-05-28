# freq={}
# nums=1,2,1,2,1
# for num in nums:
#     freq[num]=freq.get(num,0)+1
# print(freq)

# You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

# Examples:

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.

def array(arr):
    k=[]
    zeros=0
    for i in arr:
        if i!=0:
            k.append(i)
        else:
            zeros+=1

        
    k.extend([0]*zeros)
    return k

nums=[1,3,0,0,0,4]
print(array(nums))