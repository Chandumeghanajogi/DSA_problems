# a=[10,20,15]
# # a=[0,1,2,3,4,5,6]
# n=len(a)
# maxlen=0
# i=0
# while i<=n-1:
#     for j in range(1,n):    #j==5
#         if j==n-1:
#             ab=a[j]>a[j-1]
#             break
#         else:

#             if a[j]>a[i] and a[j]>a[j+1]:
               
#                 maxlen=max(maxlen,a[j])
#                 index=j
        

#     i+=1
# print(maxlen)
# print(index)
    

# # i=0 j=1 0<=6 if 2>1 and 2>3  maxlen=0
# # i=1 j=2  4>2 and 4>5     maxlen=0
# #i=3   j=4  5>4 and 5>7   maxlen=0
# #i=4   j=5  7>

nums = [1, 2, 3, 1]
# Output: 5
n=len(nums)
for i in range(0,len(nums)-1):
    if i==0 or nums[i-1]<nums[i] and i==n-1 or nums[i]>nums[i+1]:
        peak=i
print(peak)