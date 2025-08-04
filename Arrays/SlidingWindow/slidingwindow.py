# arr=[5,9,1,8,7]
# n=len(arr)
# l=0
# sum1=0
# for r in range(n):
#     sum1+=arr[r]
#     if r-l==3:
#         sum1-=arr[l]
#         l+=1
#     if r-l+1==3:

#         print(sum1)
# s="00"
# dict1={"00":"A","01":"T","10":"C","11":"G"}
# result=""
# for i in range(0,len(s),2):
#     a=s[i:i+2]
#     result+=dict1[a]
#     print(result)
        

# # Input: s = "hello"

# # Output: 13

# # Explanation:

# # The ASCII values of the characters in 
# # s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. 
# # So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
    
# # def string(s):
# #     ans=0
# #     sum1=0
# #     for i in range(1,len(s)):
# #         ans=abs(ord(s[i])-ord(s[i-1]))
# #         sum1+=ans
# #     return sum1
        
# # s="zaz"
# # print(string(s))

# a=[5,9,1,8,7]
# l=0
# n=len(a)
# sum1=0
# abc=0
# for r in range(n):
#     sum1+=a[r]
#     if r-l==3:
#         sum1-=a[l]
#         l+=1
#     if (r-l+1==3):
#         abc=max(abc,sum1)
# print(abc)    

# s = "xyzzaz"
# l=0
# a=[]
# total=""

# for r in range(len(s)):
#     a.append(s[r])
#     if r-l==3:

# s = "aababcabc"
# a=[]
# count=0
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         a=(s[i:j+1])
#         if len(a)==3 and len(set(a))==3:
#             count+=1
# print(count)

# s = "xyzzaz"
# temp=[]
# ans=""
# l=0
# count=0
# for r in range(len(s)):
#     temp.append(s[r])
#     if r-l==3:
#         temp.remove(s[l])
#         l+=1
#     if r-l+1==3 and len(set(temp))==3:
#         count+=1
# print(count)

s = "xyzzaz"
dici={}
l=0
count=0
for r in range(len(s)):
    if s[r] in dici:
        dici[s[r]]+=1
    else:
        dici[s[r]]=1
    if r-l==3:
        dici[s[l]]-=1
        if dici[s[l]]==0:
            dici.pop(s[l])
        l+=1
    if len(dici)==3:
        count+=1
print(count)

        

# s="xyzzaz"
# l=0
# count=0
# dici={}
# for r in range(len(s)):
#     if s[r] in dici:
#         dici[s[r]]+=1
#     else:
#         dici[s[r]]=1
#     if r-l==3:
#         dici[s[l]]-=1
#         if dici[s[l]]==0:
#             dici.pop(s[l])
#         l+=1
#     if len(dici)==3:
#         count+=1
# print(count)


# longest subarray with atmost k odd numbers:

# def longest(arr,k):
#     l=0
#     temp=0
#     ans=float("-inf")
#     for r in range(len(arr)):
#         if arr[r]%2==1:
#             temp+=1
#         while temp>k:
#             if arr[l]%2==1:                                                                                                                                                
#                 temp-=1
#             l+=1
#         ans=max(ans,r-l+1)
#         print(arr[l:r+1])

#     return ans


# arr=[1,3,4,5,7]
# k=2
# print(longest(arr,k))


# return the number of subaarays with atmost k odd numbers

nums=[1,3,4,5,7]
l=0
temp=0
count=0
k=2
for r in range(len(nums)):
    if nums[r]%2==1:
        temp+=1
    while temp>k:
        if nums[l]%2==1:
            temp-=1
        l+=1
    count+=r-l+1
    print(nums[l:r+1])
    print(count)
print(count)










    
    
    
    




        
       
       

  
