# Merge sorted array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

def merge(num1,num2,m,n):
    i=m-1
    j=n-1
    k=m+n-1
    while i>=0 and j>=0:
        if num1[i]>num2[j]:
            num1[k]=num1[i]
            i-=1
        else:
            num1[k]=num2[j]
            j-=1
        k-=1
    while j>=0:
        num1[k]=num2[j]
        j-=1
        k-=1
    return num1
    

num1 = [1,2,3,0,0,0]
m = 3
num2 = [2,5,6]
n = 3
nums1 = [1]
m = 1
nums2 = []
n = 0
print(merge(nums1,nums2,m,n))

# APPROACH TO MERGE SORT:

# Firstly,
# consider the i=m-1  because the valid elements 3 so values 0 1 2 and j=n-1  same 
# consider the value k for the inplace modidfications 
# k=m+n-1
# merge sort add elements according the ascending order then add them


    
    
  


    

                

