# # # from collections import Counter
# # # dictionary={1:"chandu",2:"akhil",2:"mamam"}

# # # for char in dictionary.most_common(k)::
# # #     print(char)
# # s="[)"
# # stack=[]
# # main={"(":")","[":"]","{":"}"}
# # for char in s:
# #     if char in main.values():
# #         stack.append(char)
# #     elif char in main:
# #         stack.pop()
# # if len(stack)==0:
# #     print("true")
# # else:
# #     print("false")
    

# # print(stack)

# def balancingbrackets(s):
#     stack=[]
#     bal_map={")": "(", "]": "[", "}": "{"}
#     for char in s:
#         if char in bal_map.values():
#             stack.append(char)
#         elif char in bal_map:
#             if not stack or stack[-1]!=bal_map[char]:
#                 return False
#             stack.pop()
#         else:
#             return False
#     return len(stack)==0
# s="{[]}"
# print(balancingbrackets(s))


s="{]"
count=0
for ch in s:
    if ch=="[" or ch=="{":
        count+=1
    elif ch=="]" or ch=="}":
        count-=1
if count==0:
    print("True")
else:
    print("false")



  