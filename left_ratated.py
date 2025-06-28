# def array(nums,k):
#     k%=n
#     n=len(nums)
#     temp=[0]*n
#     temp1=nums[:]
#     for i in range(k):
#         temp[i]=nums[n-k+i]
#     for i in range(n-k):
#         temp[k+i]=temp1[i]
#     for i in range(n):
#         nums[i]=temp[i]
#     return nums




# nums=[1,2,3,4,5,6,7]
# k=2
# print(array(nums,k))
# # print(a)

class Solution:
    def left_rotated(self,arr):
        n=len(arr)
        temp=[0]*n
        for i in range(1,n):
            temp[i-1]=arr[i]
        temp[n-1]=arr[0]
        
        return temp



arr=[1,2,3,4,5]
obj=Solution()
print(obj.left_rotated(arr))

# logic behind this --> first take the temp arr 
# and later move the each position to the left by the i-1 position and 
# later at the last position add the arr[0] element only
# return and call it finally..
