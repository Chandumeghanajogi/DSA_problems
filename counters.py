# # from collections import Counter
# # a="abdhjjjjd"
# # b=Counter(a)
# # c=b.most_common(1)
# # print(c[0][1])


# a = [16,17,4,3,5,2]
# final=[]
# for i in range(len(a)):
#     sum1=max(a[i:])
#     if sum1>a[i]:
#         final.append(sum1)
# print(final)



# # def find_leaders(arr):
# #     n = len(arr)
# #     leaders = []
# #     max_from_right = float('-inf')
    
# #     for i in reversed(range(n)):
# #         if arr[i] >= max_from_right:
# #             leaders.append(arr[i])
# #             max_from_right = arr[i]
    
# #     return leaders[::-1]  # reverse to maintain original order

# # # Example usage:
# # a = [16,17,4,3,5,2]
# # print(find_leaders(a))  

# print(round(5/10)*10)

# num=25
# rounded=round((num+5)/10)*10    #100---1    #5----90
# print(rounded)
# if rounded==0 or num%5==0:
#         num%5==0
#         rounded=10
#         print(100-rounded)
# elif num%5!=0:
#         print(100)
# else:
    
#     print(100-rounded)
import math
a=23
print(round(a/10)*10)
print(math.ceil(a/10))

num=5
if num%5==0:
    ans=math.ceil(num/10)*10
    rounded=100-ans
    print(rounded)
else:
    rounded=round(num/10)*10
    print(100-rounded)
